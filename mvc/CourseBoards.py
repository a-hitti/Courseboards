#Populate active boards every 5 minutes
active_boards = {}

def check_boards():
    global active_boards
    for board_key in db.board_list(current_time):
        replacements = dict()
        replacements[board_key] = Board(board_key)
        active_boards = replacements
    Timer(600.0, check_boards).start()

check_boards()

#Controller code

def view(board_key):
    #Pass this variable to the view code
    active_boards[board_key]

def view_post(board_key, post_num):
    return active_boards[board_key].posts[post_num]

def new_post(board_key, message):
    new_post = Post()
    new_post.message = message
    active_boards[board_key].posts.append(new_post)

def new_reply(board_key, post_num, reply_text):
    active_boards[board_key].posts[post_num].append(reply_text)
