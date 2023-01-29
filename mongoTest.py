import pymongo



# Connect to MongoDB client
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select the database and collection
db = client["watchlist"]
collectionMovies = db["movies"]
collectionShows = db['shows']

print(f'\n### {collectionMovies.count_documents({})} Movies #######################################\n')
for m in collectionMovies.find().sort('title'):
    print (f"{m['title']} => {m['guid']}")
           
print(f'\n### {collectionShows.count_documents({})} Shows #######################################\n')
for m in collectionShows.find().sort('title'):
    print (f"{m['title']} => {m['guid']}")
