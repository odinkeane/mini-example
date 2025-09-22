from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from settings import Settings
from service import StudentService




app = FastAPI(
    title = Settings.get_api_title()
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[Settings.get_frontend_url()],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы
    allow_headers=["*"],  # Разрешить все заголовки
)


@app.get('/')
async def index():
    print("data succesfully send")
    return {"data": {"message": "hello!", "data": 123}}



@app.get('/students')
async def get_students():
    print("students send successfuly")
    return {"students": StudentService.get_students()}

@app.get('/students/{id}')
async def get_student_by_id(id:int):
    return {"student": StudentService.get_student_by_id(id)}

