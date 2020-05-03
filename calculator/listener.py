import os
import pymongo

client = str(os.environ.get('MONGODB_URL'))
change_stream = client.changestream.collection.watch()
for change in change_stream:
    print(dumps(change))
    print('') # for readability only
