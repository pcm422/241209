from pymongo import MongoClient
from datetime import datetime

# [문제 1: 특정 장르의 책 찾기] - 문제 설명
def insert_genre(db):
    books = {"title": "The Hobbit", "author": "J. R. R. Tolkien", "year": 1937, "genre" : "Fantasy"}
    
    db.books.insert_one(books)

# [문제 1: 특정 장르의 책 찾기] - 쿼리 작성 목표
def find_genre(db, name, genre):
    collection = db[name]
    query = {"genre": genre}
    
    for doc in collection.find(query, {"_id": 0, "title": 1, "author": 1}):
        print(doc)

# [문제 2: 감독별 평균 영화 평점 계산]
def average_derector(db, name):
    collection = db[name]
    
    pipeline = [
        {"$group" : {"_id" : "$director", "average" : {"$avg": "$rating"}}}
        ]
    
    collection.aggregate(pipeline)
    
    for doc in collection.aggregate(pipeline):
        print(doc)
        
# [문제 3: 특정 사용자의 최근 행동 조회]
def user_actionlist(db, name, user_id):
    collection = db[name]
    
    query = {"user_id": user_id}
    query2 = {"_id":0, "user_id":1, "action" : 1}
    sort = [{"timestamp", -1}]
    limit = 5
    
    for doc in collection.find(query, query2).sort(sort).limit(limit):
        print(doc)
        
# [문제 4: 출판 연도별 책의 수 계산]
def howmanybooks(db, name):
    collection = db[name]
    
    pipeline = [
        {"$group" : {"_id" : "$year", "booksCount" : {"$sum": 1}}},
        {"$sort" : {"booksCount" : -1}}
        ]
    
    collection.aggregate(pipeline)
    
    for doc in collection.aggregate(pipeline):
        print(doc)
        
# [문제 5: 특정 사용자의 행동 유형 업데이트]
def user_action_update(db, name, user_id):
    collection = db[name]
    query = {"user_id" : user_id, "action": "view", "timestamp": {"$lt" : datetime(2023, 4, 13)}}
    query2 = {"$set" : {"action":"seen"}}
    
    collection.update_many(query, query2)
    
if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017/')
    db = client.local  # 'local' 데이터베이스 사용
    
    # insert_genre(db) # [문제 1: 특정 장르의 책 찾기] - 문제 설명 호출
    # find_genre(db, "books", "Fantasy") # [문제 1: 특정 장르의 책 찾기] - 쿼리 작성 목표 호출
    
    # average_derector(db, "movies") # [문제 2: 감독별 평균 영화 평점 계산] 호출
    
    # user_actionlist(db, "user_actions", 1) # [문제 3: 특정 사용자의 최근 행동 조회] 호출
    
    # howmanybooks(db, "books") # [문제 4: 출판 연도별 책의 수 계산] 호출
    
    user_action_update(db, "user_actions", 1) # [문제 5: 특정 사용자의 행동 유형 업데이트] 호출
    
    client.close()