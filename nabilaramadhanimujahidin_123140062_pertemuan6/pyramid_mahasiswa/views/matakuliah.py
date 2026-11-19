from pyramid.httpexceptions import (
    HTTPBadRequest,
    HTTPNotFound,
)
from pyramid.view import view_config

from ..models import Matakuliah

REQUIRED_FIELDS = ('kode_mk', 'nama_mk', 'sks', 'semester')


def _validate_positive_int(value, field):
    """Mengubah nilai menjadi integer positif atau melempar ValueError."""
    if isinstance(value, bool) or isinstance(value, float):
        raise ValueError(
            f'Field {field} harus berupa bilangan bulat!'
        )
    try:
        number = int(value)
    except (TypeError, ValueError):
        raise ValueError(
            f'Field {field} harus berupa bilangan bulat!'
        )
    if number <= 0:
        raise ValueError(
            f'Field {field} harus lebih besar dari 0!'
        )
    return number


def _missing_fields(json_data):
    """Mengembalikan daftar field wajib yang tidak diisi."""
    return [
        field for field in REQUIRED_FIELDS
        if field not in json_data
        or json_data[field] is None
        or json_data[field] == ''
    ]


# 1. READ ALL: Menampilkan daftar seluruh mata kuliah
@view_config(route_name='matakuliah_list', renderer='json')
def matakuliah_list(request):
    """View untuk mengambil semua data mata kuliah."""
    dbsession = request.dbsession
    matakuliahs = (
        dbsession.query(Matakuliah)
        .order_by(Matakuliah.id.asc())
        .all()
    )
    return {'matakuliahs': [mk.to_dict() for mk in matakuliahs]}


# 2. READ ONE: Menampilkan detail satu mata kuliah berdasarkan ID
@view_config(route_name='matakuliah_detail', renderer='json')
def matakuliah_detail(request):
    """View untuk melihat detail satu mata kuliah berdasarkan ID."""
    dbsession = request.dbsession
    matakuliah_id = request.matchdict['id']
    matakuliah = (
        dbsession.query(Matakuliah)
        .filter_by(id=matakuliah_id)
        .first()
    )

    if matakuliah is None:
        return HTTPNotFound(
            json_body={
                'error': (
                    f'Mata kuliah dengan ID {matakuliah_id} '
                    'tidak ditemukan'
                )
            }
        )

    return {'matakuliah': matakuliah.to_dict()}


# 3. CREATE: Menambahkan data mata kuliah baru
@view_config(
    route_name='matakuliah_add',
    request_method='POST',
    renderer='json',
)
def matakuliah_add(request):
    """View untuk menambahkan mata kuliah baru dari payload JSON."""
    try:
        json_data = request.json_body
    except (TypeError, ValueError):
        return HTTPBadRequest(
            json_body={'error': 'Payload JSON tidak valid'}
        )

    missing = _missing_fields(json_data)
    if missing:
        return HTTPBadRequest(
            json_body={'error': f'Field {missing[0]} wajib diisi!'}
        )

    try:
        sks = _validate_positive_int(json_data['sks'], 'sks')
        semester = _validate_positive_int(
            json_data['semester'], 'semester'
        )
    except ValueError as error:
        return HTTPBadRequest(json_body={'error': str(error)})

    dbsession = request.dbsession
    duplicate = (
        dbsession.query(Matakuliah)
        .filter_by(kode_mk=json_data['kode_mk'])
        .first()
    )
    if duplicate is not None:
        return HTTPBadRequest(
            json_body={
                'error': (
                    f"Kode mata kuliah {json_data['kode_mk']} "
                    'sudah terdaftar!'
                )
            }
        )

    matakuliah = Matakuliah(
        kode_mk=json_data['kode_mk'],
        nama_mk=json_data['nama_mk'],
        sks=sks,
        semester=semester,
    )

    dbsession.add(matakuliah)
    # Flush untuk mengeksekusi INSERT dan memperoleh nilai id
    dbsession.flush()

    return {'success': True, 'matakuliah': matakuliah.to_dict()}


# 4. UPDATE: Mengubah data mata kuliah yang sudah ada
@view_config(
    route_name='matakuliah_update',
    request_method='PUT',
    renderer='json',
)
def matakuliah_update(request):
    """View untuk mengupdate data mata kuliah berdasarkan ID."""
    dbsession = request.dbsession
    matakuliah_id = request.matchdict['id']

    matakuliah = (
        dbsession.query(Matakuliah)
        .filter_by(id=matakuliah_id)
        .first()
    )
    if matakuliah is None:
        return HTTPNotFound(
            json_body={
                'error': (
                    f'Mata kuliah dengan ID {matakuliah_id} '
                    'tidak ditemukan'
                )
            }
        )

    try:
        json_data = request.json_body
    except (TypeError, ValueError):
        return HTTPBadRequest(
            json_body={'error': 'Payload JSON tidak valid'}
        )

    if 'kode_mk' in json_data:
        duplicate = (
            dbsession.query(Matakuliah)
            .filter(
                Matakuliah.kode_mk == json_data['kode_mk'],
                Matakuliah.id != matakuliah.id,
            )
            .first()
        )
        if duplicate is not None:
            return HTTPBadRequest(
                json_body={
                    'error': (
                        f"Kode mata kuliah {json_data['kode_mk']} "
                        'sudah terdaftar!'
                    )
                }
            )
        matakuliah.kode_mk = json_data['kode_mk']

    if 'nama_mk' in json_data:
        matakuliah.nama_mk = json_data['nama_mk']

    try:
        if 'sks' in json_data:
            matakuliah.sks = _validate_positive_int(
                json_data['sks'], 'sks'
            )
        if 'semester' in json_data:
            matakuliah.semester = _validate_positive_int(
                json_data['semester'], 'semester'
            )
    except ValueError as error:
        return HTTPBadRequest(json_body={'error': str(error)})

    return {'success': True, 'matakuliah': matakuliah.to_dict()}


# 5. DELETE: Menghapus data mata kuliah
@view_config(
    route_name='matakuliah_delete',
    request_method='DELETE',
    renderer='json',
)
def matakuliah_delete(request):
    """View untuk menghapus mata kuliah berdasarkan ID."""
    dbsession = request.dbsession
    matakuliah_id = request.matchdict['id']

    matakuliah = (
        dbsession.query(Matakuliah)
        .filter_by(id=matakuliah_id)
        .first()
    )
    if matakuliah is None:
        return HTTPNotFound(
            json_body={
                'error': (
                    f'Mata kuliah dengan ID {matakuliah_id} '
                    'tidak ditemukan'
                )
            }
        )

    dbsession.delete(matakuliah)

    return {
        'success': True,
        'message': (
            f'Mata kuliah dengan ID {matakuliah_id} berhasil dihapus'
        ),
    }
