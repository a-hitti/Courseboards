import pymongo
import datetime
from pymongo import Connection
from pymongo.objectid import ObjectId
from pymongo.errors import OperationFailure

#Establish Connection
userID = 'admin'
pwd = 'hackcu11'
host = 'flame.mongohq.com'
port = 27039
dbName = 'posts_database'

connection = Connection(host, port)
db = connection[dbName]
db.authenticate(userID, pwd)

def auto_authenticate(f):
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except OperationFailure:
            db.authenticate(userID, pwd)
            return f(*args, **kwargs)
    return wrapper


#Board Queries
@auto_authenticate
def get_boards(current_time=None):
    import Board
    if not current_time:
        board_keys = db.courses.find({}, {'title':1})
    else:
        board_keys = db.courses.find(
            {
                "weekdays": current_time.weekday(),
                "hours" : {"$lte" : current_time.hour*100+current_time.minute,"$gte" : current_time.hour*100+current_time.minute},
             },            
            {'title':1}
            )
    b_keys = [b['title'] for b in board_keys]
    b_keys = set(b_keys)
    boards = [Board.Board(key=k) for k in b_keys]
    return boards

@auto_authenticate
def get_schedule(board_key):
    return list(db.courses.find({'title':board_key}, {"title":0, '_id':0}))

@auto_authenticate
def add_post(board_key, post_key):
    db.posts.update({'_id':ObjectId(post_key)}, {'$set':{'board':board_key}})

#Post queries
@auto_authenticate
def create_post(message):
    timestamp = datetime.datetime.now()
    pid = db.posts.insert({'timestamp':timestamp, 'replies':[], 'message':message})
    #Bad things will happen if you remove the next line. I don't know why. Stuff will get desynced.
    list(db.posts.find({'_id':pid}))
    return pid

@auto_authenticate
def get_posts(board_key):
    import Post
    post_ids = db.posts.find({'board':board_key}, {'_id':1}).sort('timestamp', pymongo.DESCENDING).limit(25)
    posts = [Post.Post(key=k['_id']) for k in post_ids]
    return posts[::-1]

@auto_authenticate
def get_message(post_key):
    query = db.posts.find({'_id': ObjectId(post_key)}, {'message':1})
    try:
        query[0]['message']
    except IndexError:
        raise Exception(str(post_key) + "??")
    return query[0]['message']

@auto_authenticate
def get_replies(post_key):
    query = db.posts.find({'_id': ObjectId(post_key)}, {'replies':1})
    return query[0]['replies']

@auto_authenticate
def format_reply(reply):
    timestamp = datetime.datetime.now()
    return {'timestamp':timestamp, 'reply-text':reply}

@auto_authenticate
def append_reply(post_key, reply):
    db.posts.update({'_id' : ObjectId(post_key)}, {"$push" : {"replies": reply}})
    #I don't know why we need to do this... But pymongo will lose data without it.
    list(db.posts.find({'_id': ObjectId(post_key)}))

@auto_authenticate
def get_timestamp(post_key):
    query = db.posts.find({'_id': ObjectId(post_key)}, {'timestamp':1})
    return query[0]['timestamp']

@auto_authenticate
def change_timestamp(post_key, timestamp):
    db.posts.update({'_id': ObjectId(post_key)}, {'$set':{'timestamp':timestamp}})
    #Sanity check
    q = db.posts.find({'_id':ObjectId(post_key)})
    q[0]['timestamp'] == timestamp, 'Timestamps not equal'
