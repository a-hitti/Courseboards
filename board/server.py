import cherrypy
import os
import sys
from board import Board
base = os.path.abspath(os.path.dirname(sys.argv[0]))
print(base)

#Server configuration
site_conf = \
    {'server.socket_host': '127.0.0.1',
     'server.socket_port': 80,
     'error_page.404': os.path.join(base, "static/error.html")
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
         },
    '/favicon.ico':
        {'tools.staticfile.on':True,
         'tools.staticfile.filename':os.path.join(base,'favicon.ico'),
         }
    }



cherrypy.quickstart(Board("FroSci"), '/', config=board_conf)
