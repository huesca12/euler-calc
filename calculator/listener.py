import os
import pymongo
from bson.json_util import dumps

client = pymongo.MongoClient(str(os.environ.get('MONGODB_URL')))
change_stream = client.terminal_rawrequest.watch()
for change in change_stream:
    print(dumps(change))
    print('') # for readability only
