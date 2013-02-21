from varnish_admin_socket import VarnishAdminSocket
import subprocess

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

def varnish_stats():
    varnish = conn_varnish()
    varnish_stats = subprocess.check_output("varnishstat -1",stderr=subprocess.STDOUT, shell=True)
    return varnish_stats.splitlines()


def varnishVersion():
    varnish_version = subprocess.check_output("varnishd -V",stderr=subprocess.STDOUT, shell=True)
    return varnish_version.splitlines()[0][10:-1]