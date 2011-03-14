from datetime import datetime
from pymongo import Connection

userID = 'admin'
pwd = 'hackcu11'
host = 'flame.mongohq.com'
port = 27039
dbName = 'posts_database'

connection = Connection(host, port)
db = connection[dbName]

def get_current_boards(self):
    db.authenticate(userID, pwd)
    tmp = datetime.now()
    courses = list(self.db.courses.find(
        {"weekdays":tmp.weekday(),
         "hours" : {"$lte" : tmp.hour*100+tmp.minute, "$gte" : tmp.hour*100+tmp.minute}
         }
        ))
    return courses

def request_schedule(self,board):
    db.authenticate(userID, pwd)
    tmp = db.courses
    return suggests.find_one(
        {'board':board,
         "weekdays":tmp.weekday(),
         "hours" : {"$lte" : tmp.hour*100+tmp.minute,"$gte" : tmp.hour*100+tmp.minute}
         },{"hours":1})["hours"]


def add_reply(self,new_reply,author=""):
    timestamp = time.time()
    replies.append({"reply-text":cgi.escape(new_reply),"timestamp":datetime.now(),"replies":[],"author":author})
    self.collection.update({'_id' : self.post_id},{"$set" : {"replies" :self.replies,"timestamp" : self.timestamp}})
