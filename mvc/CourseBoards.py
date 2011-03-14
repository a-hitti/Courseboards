from models import network_queries as db
from models.Post import Post
from models.Board import Board
import datetime
from threading import Timer
import time
from Cheetah.Template import Template
#Populate active boards every 5 minutes
active_boards = {}

def check_boards():
    global active_boards
    current_time = datetime.datetime.now()
    for board in db.get_boards():
        replacements = dict()
        replacements[board.key] = board
        active_boards = replacements
        
    Timer(600.0, check_boards).start()

check_boards()
    

#Controller code
def auto_render(f):
    template_name = f.__name__
    #Get the template
    t_module = __import__('views.%s' % template_name, fromlist=[template_name])
    t = getattr(t_module, template_name)
    def wrapper(*args, **kwargs):
        #Expect that the decorated function returns a namespace
        name_space = f(*args, **kwargs)
        #Return the completed page
        return str(t(searchList=name_space))
    return wrapper

@auto_render
def view_boards():
    #sort by board name
    boards = sorted(active_boards.values(), key=lambda x: x.board_name)
    return {'boards':boards}
view_boards.exposed = True

@auto_render
def view_board(board_key):
    board = active_boards[board_key]

    #Attach postnums so that an individual post knows where it is in the board structure
        #This is helpful for setting up a view to reply to a specific post
    for i in range(len(board.posts)):
        board.posts[i].postnum = i
        
    sorted_posts = sorted(board.posts, key=lambda x: x.timestamp, reverse=True)
    for p in sorted_posts:
        print(p.timestamp)
    return {'sorted_posts':sorted_posts, 'board':board}
view_board.exposed = True

@auto_render
def view_post(board_key, post_num):
    post_num = int(post_num)
    board = active_boards[board_key]
    post = board.posts[post_num]
    return {'board':board, 'post_num':post_num}
view_post.exposed = True

@auto_render
def new_post(board_key, message):
    pid = db.create_post(message)
    new_post = Post(pid)
    #Do we need to lock active_boards here?
    post_num = len(active_boards[board_key].posts)
    active_boards[board_key].posts.append(new_post)
    #End lock?
    return {'url':'/view_post/%s/%s' % (board_key, post_num)}
new_post.exposed = True

@auto_render
def new_reply(board_key, post_num, reply_text):
    post_num = int(post_num)
    #TODO: Sanitize reply_text
    active_boards[board_key].posts[post_num].replies.append(reply_text)
    return {'url': '/view_post/%s/%s' % (board_key, post_num)}
new_reply.exposed = True

def index():
    return view_boards()
index.exposed = True
