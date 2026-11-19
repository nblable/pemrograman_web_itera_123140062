from pyramid.view import view_config


@view_config(
    route_name='home',
    renderer='../templates/mytemplate.jinja2',
)
def my_view(request):
    """Halaman utama sederhana yang tidak bergantung pada tabel contoh."""
    return {'project': 'pyramid_mahasiswa'}
