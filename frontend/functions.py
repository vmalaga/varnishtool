from django.http import HttpResponse
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
        varnish_stats = subprocess.check_output("varnishstat -1",
            stderr=subprocess.STDOUT, 
            shell=True).splitlines()
        stats_dict = dict((line.split( )[0],line.split( )[1]) for line in varnish_stats)
        client_conn = stats_dict['client_conn'] # Client connections accepted
        client_req = stats_dict['client_req'] # Client requests received
        cache_hit = stats_dict['cache_hit'] # Cache hits
        cache_hitpass = stats_dict['cache_hitpass'] # Cache hits for pass
        cache_miss = stats_dict['cache_miss'] # Cache misses
        backend_conn = stats_dict['backend_conn'] # Backend conn. success
        backend_fail = stats_dict['backend_fail'] # Backend conn. failures
        backend_reuse = stats_dict['backend_reuse'] # Backend conn. reuses
        backend_toolate = stats_dict['backend_toolate'] # Backend conn. was closed
        backend_recycle = stats_dict['backend_recycle'] # Backend conn. recycles

        stats_response = {"Client Connections":client_conn,"Client Requests":client_req,
        'Cache Hits':cache_hit, 'Cache Misses':cache_miss, 'Cache Hit for pass':cache_hitpass}

        return stats_response
    except subprocess.CalledProcessError:
        return "Error getting varnishstats on local machine"


def varnishVersion():
    try:
        varnish_version = subprocess.check_output("varnishd -V",stderr=subprocess.STDOUT, shell=True)
        return varnish_version[10:23]
    except subprocess.CalledProcessError:
        return "Error getting varnishd version"
