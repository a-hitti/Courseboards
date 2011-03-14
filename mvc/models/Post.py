from magic import *

#Each Post object is responsible for providing methods to:
    #Give an up-to-date list of the post content and all responses
    #Add a new response

@ensure_single
class Post:
    def __init__(self, key=None):
        if not key:
            #Insert a new post into the database, get the key
        else:
            self.key = key

        #Get make database call to get replies and message for this key
        self.replies = DBList( ... )
        self._message = ...

    @property
    def message(self):
        return self._message

    @message.setter(self, value):
        self._message = value
        #Insert value into database
