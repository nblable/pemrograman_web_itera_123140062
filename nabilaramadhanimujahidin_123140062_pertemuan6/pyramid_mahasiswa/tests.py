import os
import tempfile
import unittest

from sqlalchemy import create_engine
from webtest import TestApp

from . import main
from .models.meta import Base


class BaseFunctionalTest(unittest.TestCase):
    """Menyiapkan aplikasi Pyramid dengan database SQLite sementara."""

    def setUp(self):
        handle, self.db_path = tempfile.mkstemp(suffix='.sqlite')
        os.close(handle)

        self.database_url = (
            'sqlite:///' + self.db_path.replace('\\', '/')
        )
        self.settings = {
            'sqlalchemy.url': self.database_url,
            'retry.attempts': '3',
        }

        self.engine = create_engine(self.database_url)
        Base.metadata.create_all(self.engine)
        self.app = TestApp(main({}, **self.settings))

    def tearDown(self):
        session_factory = self.app.app.registry.get(
            'dbsession_factory'
        )
        if session_factory is not None:
            session_factory.kw['bind'].dispose()
        self.engine.dispose()
        if os.path.exists(self.db_path):
            try:
                os.remove(self.db_path)
            except PermissionError:
                pass


class TestHomeView(BaseFunctionalTest):

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_int, 200)
        self.assertIn('pyramid_mahasiswa', response.text)


class TestMahasiswaAPI(BaseFunctionalTest):

    payload = {
        'nim': '12345',
        'nama': 'Budi Santoso',
        'jurusan': 'Teknik Informatika',
        'tanggal_lahir': '2000-05-15',
        'alamat': 'Jl. Merdeka No. 123, Bandung',
    }

    def test_read_all_empty(self):
        response = self.app.get('/api/mahasiswa')
        self.assertEqual(response.status_int, 200)
        self.assertEqual(response.json, {'mahasiswas': []})

    def test_create_and_read_one(self):
        response = self.app.post_json('/api/mahasiswa', self.payload)
        self.assertEqual(response.status_int, 200)
        self.assertTrue(response.json['success'])

        mahasiswa = response.json['mahasiswa']
        self.assertEqual(mahasiswa['nim'], '12345')
        self.assertEqual(mahasiswa['tanggal_lahir'], '2000-05-15')

        detail = self.app.get('/api/mahasiswa/{0}'.format(
            mahasiswa['id']
        ))
        self.assertEqual(detail.json['mahasiswa']['nama'],
                         'Budi Santoso')

    def test_create_missing_required_field(self):
        response = self.app.post_json(
            '/api/mahasiswa',
            {'nama': 'Tanpa NIM', 'jurusan': 'Informatika'},
            expect_errors=True,
        )
        self.assertEqual(response.status_int, 400)
        self.assertEqual(response.json['error'],
                         'Field nim wajib diisi!')

    def test_create_invalid_date(self):
        payload = dict(self.payload, tanggal_lahir='15-05-2000')
        response = self.app.post_json(
            '/api/mahasiswa', payload, expect_errors=True
        )
        self.assertEqual(response.status_int, 400)

    def test_read_one_not_found(self):
        response = self.app.get(
            '/api/mahasiswa/999', expect_errors=True
        )
        self.assertEqual(response.status_int, 404)

    def test_update_and_delete(self):
        created = self.app.post_json(
            '/api/mahasiswa', self.payload
        ).json['mahasiswa']

        updated = self.app.put_json(
            '/api/mahasiswa/{0}'.format(created['id']),
            {'jurusan': 'Informatika Medis'},
        )
        self.assertEqual(updated.status_int, 200)
        self.assertEqual(
            updated.json['mahasiswa']['jurusan'],
            'Informatika Medis',
        )

        deleted = self.app.delete(
            '/api/mahasiswa/{0}'.format(created['id'])
        )
        self.assertTrue(deleted.json['success'])

        missing = self.app.get(
            '/api/mahasiswa/{0}'.format(created['id']),
            expect_errors=True,
        )
        self.assertEqual(missing.status_int, 404)


class TestMatakuliahAPI(BaseFunctionalTest):

    payload = {
        'kode_mk': 'IF2110',
        'nama_mk': 'Pemrograman Web',
        'sks': 3,
        'semester': 3,
    }

    def test_read_all_empty(self):
        response = self.app.get('/api/matakuliah')
        self.assertEqual(response.status_int, 200)
        self.assertEqual(response.json, {'matakuliahs': []})

    def test_create_and_read_one(self):
        response = self.app.post_json('/api/matakuliah', self.payload)
        self.assertEqual(response.status_int, 200)

        matakuliah = response.json['matakuliah']
        self.assertEqual(matakuliah['kode_mk'], 'IF2110')
        self.assertEqual(matakuliah['sks'], 3)

        detail = self.app.get(
            '/api/matakuliah/{0}'.format(matakuliah['id'])
        )
        self.assertEqual(detail.json['matakuliah']['nama_mk'],
                         'Pemrograman Web')

    def test_create_missing_required_field(self):
        response = self.app.post_json(
            '/api/matakuliah',
            {'kode_mk': 'IF2110', 'nama_mk': 'Pemrograman Web'},
            expect_errors=True,
        )
        self.assertEqual(response.status_int, 400)
        self.assertEqual(response.json['error'],
                         'Field sks wajib diisi!')

    def test_create_invalid_sks(self):
        for invalid_value in (0, -3, 'tiga', 2.5):
            payload = dict(self.payload, sks=invalid_value)
            response = self.app.post_json(
                '/api/matakuliah', payload, expect_errors=True
            )
            self.assertEqual(
                response.status_int, 400,
                msg='sks={0!r} seharusnya ditolak'.format(
                    invalid_value
                ),
            )

    def test_create_invalid_semester(self):
        payload = dict(self.payload, semester=0)
        response = self.app.post_json(
            '/api/matakuliah', payload, expect_errors=True
        )
        self.assertEqual(response.status_int, 400)

    def test_create_duplicate_kode_mk(self):
        self.app.post_json('/api/matakuliah', self.payload)
        response = self.app.post_json(
            '/api/matakuliah', self.payload, expect_errors=True
        )
        self.assertEqual(response.status_int, 400)
        self.assertIn('sudah terdaftar', response.json['error'])

    def test_read_one_not_found(self):
        response = self.app.get(
            '/api/matakuliah/999', expect_errors=True
        )
        self.assertEqual(response.status_int, 404)

    def test_update_and_delete(self):
        created = self.app.post_json(
            '/api/matakuliah', self.payload
        ).json['matakuliah']

        updated = self.app.put_json(
            '/api/matakuliah/{0}'.format(created['id']),
            {'sks': 4, 'semester': 5},
        )
        self.assertEqual(updated.status_int, 200)
        self.assertEqual(updated.json['matakuliah']['sks'], 4)
        self.assertEqual(updated.json['matakuliah']['semester'], 5)

        invalid = self.app.put_json(
            '/api/matakuliah/{0}'.format(created['id']),
            {'sks': -1},
            expect_errors=True,
        )
        self.assertEqual(invalid.status_int, 400)

        deleted = self.app.delete(
            '/api/matakuliah/{0}'.format(created['id'])
        )
        self.assertTrue(deleted.json['success'])

        missing = self.app.get(
            '/api/matakuliah/{0}'.format(created['id']),
            expect_errors=True,
        )
        self.assertEqual(missing.status_int, 404)
