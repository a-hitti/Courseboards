#This class attaches database calls to a normal list
    #User must supply the actions db_append, and db_delete, which both take in an object to be appended/deleted
class DBList:
    def __init__(self, post_list, db_append, db_format=None):
        self.list = post_list
        self.db_append = db_append
        #the format method is needed if you want to add some metadata like timestamp
        #The use case is to change db_format as needed
        self.db_format = db_format

    def __len__(self):
        return len(self.list)

    def __getitem__(self, i):        
        return self.list[i]

    def append(self, item):
        if self.db_format:
            item = self.db_format(item)
            
        self.db_append(item)
        #Add the thing to the server
        self.list.append(item)

    def __str__(self):
        return self.list.__str__()

    def __repr__(self):
        return self.list.__repr__()
