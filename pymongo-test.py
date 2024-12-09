from pymongo import MongoClient

# MongoDB 인스턴스에 연결
client = MongoClient('mongodb://localhost:27017/')
# client = MongoClient('mongodb://username:password@localhost:27017/')

# 데이터베이스 선택 (없으면 자동 생성)
db = client['example_db']

# 콜렉션 선택 (없으면 자동 생성)
collection = db['example_collection']

# # 새 문서 삽입
# example_document = {"name": "John", "age": 30, "city": "New York"}
# collection.insert_one(example_document)

# 모든 문서 조회
for doc in collection.find():
    print(doc)

# # 조건에 맞는 문서 조회
# query = {"name": "John"}
# for doc in collection.find(query):
#     print(doc)

# # 하나의 문서 업데이트
# collection.update_one({"name": "John"}, {"$set": {"age": 31}})

# # 여러 문서 업데이트
# collection.update_many({"name": "John"}, {"$set": {"age": 32}})

# # 하나의 문서 삭제
# collection.delete_one({"name": "John"})

# # 여러 문서 삭제
# collection.delete_many({"name": "John"})

# # 콜렉션 삭제
# db.drop_collection("example_collection")

# # 데이터베이스 삭제
# client.drop_database("example_db")