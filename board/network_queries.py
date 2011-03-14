import cherrypy
import cgi #For html escaping
import pymongo
from pymongo import Connection
from Cheetah.Template import Template
from post import Post
import post as p
from datetime import datetime

class Network:
    def get_database(self):
        host= 'flame.mongohq.com'
        port = 27039
        dbName = 'posts_database'
        connection=Connection(host,port)
        #name of database
        self.db = connection[dbName]

    def add_suggestion(self,message,time,room):
        userID = 'admin'
        pwd = 'hackcu11'
        self.db.authenticate(userID, pwd)
        suggests=self.db.suggestions
        suggests.insert({'class_name':cgi.escape(message),'time':cgi.escape(time),'room':cgi.escape(room)})


    def get_current_boards(self):
        userID = 'admin'
        pwd = 'hackcu11'
        self.db.authenticate(userID, pwd)
        tmp = datetime.now()
        self.courses = list(self.db.courses.find({"weekdays":tmp.weekday(), "hours" : {"$lte" : tmp.hour*100+tmp.minute,"$gte" : tmp.hour*100+tmp.minute}}))
        name_space={"courses" : self.courses}
        return str(Template(self.homepage_template, name_space))

    def request_schedule(self,board):
        userID = 'admin'
        pwd = 'hackcu11'
        self.db.authenticate(userID, pwd)
        tmp = self.db.courses
        return suggests.find_one({'board':board,"weekdays":tmp.weekday(), "hours" : {"$lte" : tmp.hour*100+tmp.minute,"$gte" : tmp.hour*100+tmp.minute},{"hours":1}))["hours"]

    #adds a reply atomicly
    def add_reply(self,new_reply,author=""):
        self.timestamp = time.time()
        self.replies.append({"reply-text":cgi.escape(new_reply),"timestamp":datetime.now(),"replies":[],"author":author})
        self.collection.update({'_id' : self.post_id},{"$set" : {"replies" :self.replies,"timestamp" : self.timestamp}})

    def get_posts(board):
        userID = 'admin'
        pwd = 'hackcu11'
        self.db.authenticate(userID, pwd)
        posts=self.db.posts
#        print [str(p['_id']) for p in posts.find({'board':board})] 
        return [Post(board,post_id=post['_id']) for post in posts.find({'board':board}).sort({'timestamp':-1}).limit(25)]

    def add_post(self,message):
        userID = 'admin'
        pwd = 'hackcu11'
        self.db.authenticate(userID, pwd)
        self.collection=self.db.posts
        self.board=board
        if post_id == "":
            self.timestamp=time.time()
            self.post_id=self.collection.insert({'message':cgi.escape(message),'board':self.board,'replies':[],'timestamp':self.timestamp,'author':author})
            tmp=self.collection.find().sort('timestamp')
            tmp=(list(tmp))
            if(len(tmp)>num_saved):
                self.collection.remove({'_id':tmp[0]['_id']})
            self.replies=[]
            self.author=author
        else:
            #needs ObjectId to string->weird objectid type for mongo
            dic = self.db.posts.find_one({'_id': ObjectId(post_id) })
            self.message = dic['message']
            self.replies = dic['replies']
            self.post_id = dic['_id']
            self.author = dic['author']
        self.min_repls=self.get_mini_replies()
