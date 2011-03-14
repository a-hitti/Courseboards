import pymongo
from pymongo.objectid import ObjectId
from datetime import datetime

host = 'localhost'
port = 27017
db = 'CourseBoards'
user_id = ''
pwd = ''


connection = pymongo.Connection(host, port)
database = connection[db]
#database.authenticate(user_id, pwd)

#Note that ObjectId is idempotent, so it does not matter if key is type ObjectId or type String

class BoardNotFoundException(Exception):
    pass

def retrieve_board(key):
    board = database.boards.find_one({'_id': ObjectId(key)})
    if not board:
        raise BoardNotFoundException(key)
    else:
        return board

def retrieve_boards():
    return list(database.boards.find())

def retrieve_post(key):
    post = database.posts.find_one({'_id': ObjectId(key)})
    if not post:
        raise BoardNotFoundException(key)
    else:
        return post

def retrieve_posts():
    return list(database.posts.find())

def retrieve_posts_by_board(board_key):
    return list(database.posts.find({'board_key':ObjectId(board_key)}))

def new_board(board_name, location):
    #Expect board_name to be string
    return database.boards.insert({'board_name':board_name, 'location_key':location, 'post_keys':[]})

def new_post(board_key, message, author=None, timestamp=datetime.now()):
    #First line raises error for board not found
    board = retrieve_board(board_key)
                                   
    post = database.posts.insert({'board_key':ObjectId(board_key), 'message':message, 'replies':[], 'timestamp':timestamp, 'author':author})
    database.boards.update({'_id':ObjectId(board_key)}, {'$push': {'post_keys':post}})
        

def delete_board(key):
    board = retrieve_board(key)
    for post_key in board['post_keys']:
        delete_post(post_key)
    database.boards.remove({'_id': ObjectId(key)})
    

def delete_post(key):
    post = retrieve_post(key)
    board = retrieve_board(post['board_key'])
    database.boards.update({'_id':board['_id']}, {'$pull' : {'post_keys': post} })
    database.posts.remove({'_id': ObjectId(key)})


#Add new schedule time
    #start_time is a minute from 0 to 24*60
    #end_time > start_time in the same range
def new_schedule_item(board_key, weekday, start_time, finish_time):
    return database.schedules.insert({'board_key':ObjectId(board_key), 'weekday':weekday, 'start_time':start_time, 'finish_time':finish_time})
    
#Clear schedule for a class
def clear_schedule(board_key):
    database.schedules.remove({'board_key':ObjectId(board_key)})

