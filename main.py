# from fastapi import FastAPI
# import json

# app = FastAPI()

# def load_data():
#     with open('students.json', 'r') as f:
#         data = json.load(f)
#     return data

# @app.get("/")
# def hello():
#     return "Hello LPU"

# @app.get("/about")
# def about():
#     return "LPU is good place to live"

# @app.get('/view')
# def view():
#     data = load_data()
#     return data

# @app.get('/students/{students_id}')
# def view_students(students_id: str):
#     data = load_data()

#     if students_id in data:
#         return data[students_id]    
#     return {'error': 'person not found'}

from fastapi import FastAPI
from routes.TodoRoute import router as TodoRouter

app = FastAPI(title="CRUD APP")

app.include_router(TodoRouter)

@app.get("/", tags=["Main"])
def indexView():
    return {
        "message": "Server is Running"
    }