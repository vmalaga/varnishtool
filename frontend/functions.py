from varnish_admin_socket import VarnishAdminSocket

def conn_varnish():
    """
Conexion con varnish

    """
    varnish = VarnishAdminSocket()
    varnish.host = '127.0.0.1'
    varnish.port = 6082
    secret = open('/etc/varnish/secret')
    varnish.secret = secret.readline()

    varnish.connect()
    vclnow = varnish.command('vcl.show boot')

    return vclnow
