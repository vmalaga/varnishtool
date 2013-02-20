from varnish_admin_socket import VarnishAdminSocket

def conn_varnish():
    varnish = VarnishAdminSocket()
    varnish.host = '127.0.0.1'
    varnish.port = 6082
    secret = open('/etc/varnish/secret')
    varnish.secret = secret.readline()
    varnish.connect()
    return varnish

def varbanner():
    varnish = conn_varnish()
    banner = varnish.command('banner')
    return banner
