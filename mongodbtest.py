import pymongo
client = pymongo.MongoClient("mongodb+srv://Harsha:datarock24@cluster0.2y6afby.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
     "name" : "sudhanshu",
     "email" : "harsha@gmail.com" ,
     "surname" : "kumar"
}
db1 = client['mongodb']
coll = db1['test']
coll.insert_one(d)