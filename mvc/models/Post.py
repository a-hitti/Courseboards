from magic import *
import network_queries as db
from DBList import DBList
import datetime

#Each Post object is responsible for providing methods to:
    #Give an up-to-date list of the post content and all responses
    #Add a new response


@ensure_single
class Post:
    #When Post object is appended to a Board object, it will be added to the database
    def __init__(self, key):
        self.message = db.get_message(key)
        self.key = key
        replies = db.get_replies(self.key)
        self.timestamp = db.get_timestamp(self.key)
        def append_reply(reply):
            #Update timestamp
            current_time = datetime.datetime.now()
            print("\n\tupdate timestamp to: %s\n!!!!!\n\n" % current_time)
            self.timestamp = current_time
            #Sync with database
            db.append_reply(self.key, reply)
            db.change_timestamp(self.key, current_time)
        self.replies = DBList(replies, append_reply, db.format_reply)

 

    
