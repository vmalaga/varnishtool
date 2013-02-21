from varnish_admin_socket import VarnishAdminSocket
import subprocess

def conn_varnish():
    varnish = VarnishAdminSocket()
    varnish.host = '127.0.0.1'
    varnish.port = 6082
    try:
        secret = open('/etc/varnish/secret')
        varnish.secret = secret.readline()
        varnish.connect()
        return varnish
    except IOError:
        varnish = "Error while reading varnish secret file, please # sudo chmod 644 /etc/varnish/secret"
        return varnish
        #sys.exit(255)

def varbanner():
    varnish = conn_varnish()
    banner = varnish.command('banner')
    return banner

def varnish_stats():
    try:
        varnish_stats = subprocess.check_output("varnishstat -1",stderr=subprocess.STDOUT, shell=True)
        return varnish_stats.splitlines()
    except subprocess.CalledProcessError:
        return "Error getting varnishstats on local machine"


def varnishVersion():
    try:
        varnish_version = subprocess.check_output("varnishd -V",stderr=subprocess.STDOUT, shell=True)
        return varnish_version.splitlines()[0][10:-1]
    except subprocess.CalledProcessError:
        return "Error getting varnishd version"
