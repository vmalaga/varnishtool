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

class varnish_stats():
    """Varnish stats class"""
    def get_stats(self):
        try:
            varnishStats = subprocess.check_output("varnishstat -1",
                stderr=subprocess.STDOUT,
                shell=True).splitlines()

            self.stats_dict = dict((line.split( )[0],line.split( )[1]) for line in varnishStats)
            self.stats_dict2 = dict(( ' '.join(line.split( )[3:]) ,line.split( )[1] ) for line in varnishStats)
            return self.stats_dict2

            #varnish_stats = subprocess.check_output("varnishstat -1",
            #    stderr=subprocess.STDOUT,
            #    shell=True).splitlines()

            #self.stats_dict = dict((line.split( )[0],line.split( )[1]) for line in varnish_stats)

        except subprocess.CalledProcessError:
            return "Error getting varnishstats on local machine"

    def client_st(self):
        self.client_stats = {"Client_Connections": self.stats_dict['client_conn'],
        "Client_Requests": self.stats_dict['client_req']}
        return self.client_stats

    def cache_st(self):
        try:
            hitrate = int(self.stats_dict['cache_hit']) * 100 / int(self.stats_dict['client_req'])
        except ZeroDivisionError:
            hitrate = 0

        self.cache_stats = {"Cache_Hits": self.stats_dict['cache_hit'],
        "Cache_Misses": self.stats_dict['cache_miss'],
        "Cache_Hit_for_pass": self.stats_dict['cache_hitpass'],
        "Client_Requests": self.stats_dict['client_req'],
        "Hitrate": hitrate}
        return self.cache_stats

    def backend_st(self):
        self.backend_stats = {"Backend Connections": self.stats_dict['backend_conn'],
        "Backend Connections Fails": self.stats_dict['backend_fail'],
        "Backend Reuse": self.stats_dict['backend_reuse'],
        "Backend Connections close": self.stats_dict['backend_toolate'],
        "Backend Connections recycle": self.stats_dict['backend_recycle']}
        return self.backend_stats

    def memory_st(self):
        self.mem_stats = {
        "MBytes_available": (int(self.stats_dict['SMA.s0.g_space'])/1024/1024),
        "MBytes_allocated": (int(self.stats_dict['SMA.s0.c_bytes'])/1024/1024)
        }
        return self.mem_stats

def varnishVersion():
    try:
        varnish_version = subprocess.check_output("varnishd -V",stderr=subprocess.STDOUT, shell=True)
        return varnish_version[10:23]
    except subprocess.CalledProcessError:
        return "Error getting varnishd version"

def getVcl():
    varnish = conn_varnish()
    vcltext = varnish.command('vcl.show boot')
    return vcltext

def varbanner():
    varnish = conn_varnish()
    banner = varnish.command('banner')
    return banner
