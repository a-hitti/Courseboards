import cherrypy
import pymongo
from pymongo import Connection
from Cheetah.Template import Template
from post import Post
import post as p
from datetime import datetime

#This class connects the backend with the frontend by accessing data and filling the templates
class Board:
    def __init__(self,board_name="FroSci"):
        self.board_name = board_name
        #Connect and load posts
        self.posts = p.get_posts(self.board_name)

        #load templates
        index_t = open('templates/index.tmpl', 'r')
        expand_t = open('templates/expand.tmpl', 'r')
        homepage_t = open('templates/homepage.tmpl', 'r')
        #string-ize
        self.expand_template = expand_t.read()
        self.index_template = index_t.read()
        self.homepage_template = homepage_t.read()

    def index(self, message=None):
        userID = 'admin'
        pwd = 'hackcu11'
        host= 'flame.mongohq.com'
        port = 27039
        dbName = 'posts_database'
        connection=Connection(host,port)
        #name of database
        db = connection[dbName]
        db.authenticate(userID, pwd)

        self.courses=list(db.courses.find())

        name_space={"courses" : self.courses}

        return str(Template(self.homepage_template, name_space))
#        return "whatever"
    index.exposed = True


    def course(self, board ,message=None):
        if cherrypy.request.method == 'POST':
            if not message:
                print('No message received')
                pass #Add to errors or something...
            else:
                #adds a post
                self.add_post(message)

        #Connect and load posts
                self.posts = p.get_posts(self.board_name)

        self.board_name = board

        self.posts = p.get_posts(self.board_name)

        name_space = {'posts':self.posts}
        return str(Template(self.index_template, name_space))
    course.exposed = True
    
    def expand(self, post_id, message=None):
        post = Post(self.board_name, post_id=post_id)
        if cherrypy.request.method == 'POST':
            if not message:
                print('Message was empty')
                pass #Add to errors or something...
            else:
                post.add_reply(message)
        post.update()
        #display the post and responses for post_id
        post = Post(self.board_name, post_id=post_id)
        #Render the page
           
        name_space = {'post':post}
        return str(Template(self.expand_template, name_space))
    expand.exposed = True

    def add_post(self,message):
        post = Post(self.board_name, message=message)
        
