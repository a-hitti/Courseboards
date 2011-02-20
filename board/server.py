import cherrypy
import os
import sys
from board import Board
base = os.path.dirname(os.path.abspath(__file__))

#Server configuration
site_conf = \
    {'server.socket_host': '127.0.0.1',
     'server.socket_port': 80,
    }

cherrypy.config.update(site_conf)

#App configuration
board_conf = \
    {
    #The key 'database' is for book keeping and as of now doesnt effect anything
    'database': 
        {'type': 'mongodb',
         'host': 'localhost',
         'port': 0000,
        },
    '/static':
        {'tools.staticdir.on':True,
        'tools.staticdir.dir':os.path.join(base, 'static'),
         'tools.staticdir.content_types': {'png': 'image/png',
                                           'css': 'text/css',
                                           'js':'application/javascript',}
         }
    }

def error_page_404(status, message, traceback, version):
    return "Error %s - Well, I'm very sorry but you haven't paid!" % status
cherrypy.config.update({'error_page.402': error_page_404})



cherrypy.quickstart(Board("FroSci"), '/', config=board_conf)
