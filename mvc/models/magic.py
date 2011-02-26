#Magical python decorators here:

#Allow a key string to be associated with only one unique object in the process memory
#Intercept future attempted instantiations with the same key, and return the original object with that key
def ensure_single(C):
    try:
        ensure_single.records
    except AttributeError:
        ensure_single.records = dict()

    def wrapper(key, *args):
        if (C.__name__, key) in ensure_single.records:
            #Check if an object with this key has been created before
            return ensure_single.records[(C.__name__, key)]
        else:
            print(not (C.__name__, key) in ensure_single.records)
            try:
                newC = C(key=key, *args)
            except:
                raise TypeError("To use the ensure_single decorator, your class must accept a keyword argument 'key'.")
            #Keep track of this new object
            ensure_single.records[(C.__name__, key)] = newC
            return newC
    return wrapper
