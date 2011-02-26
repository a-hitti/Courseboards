#This class attaches database calls to a normal list
    #User must supply the actions db_append, and db_delete, which both take in an object to be appended/deleted
class DBList:
    def __init__(self, post_list, db_append, db_delete):
        self.list = post_list
        self.db_delete = db_delete
        self.db_append = db_append

    def __len__(self):
        return post_list.len(self.post_list)

    def __getitem__(self, i):        
        return self.list[i]

    def __delitem__(self, i):
        #Delete the item from the database
        self.db_delete(self.list[i])
        del self.list[i]
        #Delete the item from the server

    def append(self, item):
        self.db_append(item)
        #Add the thing to the server
        self.list.append(item)

    def __str__(self):
        return self.list.__str__()

    def __repr__(self):
        return self.list.__repr__()
