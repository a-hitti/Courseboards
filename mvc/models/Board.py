from magic import *
import collections
import network_queries as db
from DBList import DBList

#Each Board object is responsible for providing methods to:
    #Give an up-to-date list of all posts
    #Add a new post

#Have a list of Board objects that have been instantiated
#If someone tries to create a duplicate, return the already existing Board object

@ensure_single
class Board:
    def __init__(self, key):
        self.key = key
        #Populate info about this board:
        self.board_name = key
        #Schedule should be a dictionary of Weekday->List of Ints (0 to 24*60)
        self.board_schedule = db.get_schedule(key)
        #Posts should be a list of Post objects

        def insert_post(post):
            post_key = post.key
            db.add_post(key, post_key)
        
        self.posts = DBList(db.get_posts(key), insert_post)
