import cherrypy
import cgi #For html escaping
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

        self.get_database()
        #load templates
        index_t = open('templates/index.tmpl', 'r')
        expand_t = open('templates/expand.tmpl', 'r')
        homepage_t = open('templates/homepage.tmpl', 'r')
        suggest_t = open('templates/suggest.tmpl', 'r')
        #string-ize
        self.expand_template = expand_t.read()
        self.index_template = index_t.read()
        self.homepage_template = homepage_t.read()
        self.suggest_template = suggest_t.read()

    def get_database(self):
        host= 'flame.mongohq.com'
        port = 27039
        dbName = 'posts_database'
        connection=Connection(host,port)
        #name of database
        self.db = connection[dbName]


    def suggest(self,message=None,time=None,room=None):
        extras = ""
        if cherrypy.request.method == 'POST':
            if not message:
                extras="No class name received."
            else:
                #adds a suggestion
                self.add_suggestion(message,time,room)
                extras="Thanks for your suggestion!"

        name_space = {'extra_text':extras}
        return str(Template(self.suggest_template, name_space))
    suggest.exposed = True

    def index(self, message=None):
        userID = 'admin'
        pwd = 'hackcu11'
        self.db.authenticate(userID, pwd)
        tmp = datetime.now()
#        self.courses = list(self.db.courses.find({"weekdays":tmp.weekday(), "hours" : {"$lte" : tmp.hour*100+tmp.minute,"$gte" : tmp.hour*100+tmp.minute}}))
        self.courses = list(self.db.courses.find())

        name_space={"courses" : self.courses}

        return str(Template(self.homepage_template, name_space))
    index.exposed = True


    def in_course_list(self,board):
        userID = 'admin'
        pwd = 'hackcu11'
        self.db.authenticate(userID, pwd)
        cur_time = datetime.now()
        return self.db.courses.find_one({"title":board,"weekdays":cur_time.weekday(), "hours" : {"$lte" : cur_time.hour*100+cur_time.minute,"$gte" : cur_time.hour*100+cur_time.minute}})

    def course(self,board):
        if cherrypy.request.method == 'POST':
            if not message:
                print('No message received')
                pass #Add to errors or something...
            else:
                #adds a post
                self.add_post(message)

        #Connect and load posts
                self.posts = p.get_posts(self.board_name)

        if not self.in_course_list(board):
#            return "whatever."
            pass
        self.board_name = board

        self.posts = p.get_posts(board)

        name_space = {'posts':self.posts,'course':board}
        return str(Template(self.index_template, name_space))
    course.exposed = True
    
    def expand(self, post_id, message=None):
        if not self.in_course_list(self.board_name):
#            return "whatever."
            pass
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

    def add_suggestion(self,message,time,room):
        userID = 'admin'
        pwd = 'hackcu11'
        self.db.authenticate(userID, pwd)
        suggests=self.db.suggestions
        suggests.insert({'class_name':cgi.escape(message),'time':cgi.escape(time),'room':cgi.escape(room)})
