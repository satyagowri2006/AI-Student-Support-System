from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["student_support"]

students = db["students"]
programs = db["programs"]
applications = db["applications"]
courses = db["courses"]
fees = db["fees"]
scholarships = db["scholarships"]
hostel = db["hostel"]
transport = db["transport"]
counseling = db["counseling"]
queries = db["queries"]