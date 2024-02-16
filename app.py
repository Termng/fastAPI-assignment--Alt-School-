from fastapi import FastAPI, HTTPException
from uuid import uuid4

app = FastAPI()

student_dict = {}


student_data = {
    id: 0,
    "name": "",
    "age": 0,
    "sex": "",
    "height": 0.0
}


# Get all students
@app.get("/students/")  
def get_all_students():
    return student_dict


# Get student by id
@app.get("/students/{id}")
def get_student(id: int):
    if id not in student_dict:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return student_dict[id]


# Create Student 
@app.post("/students")
def create_student(name: str, age: int, sex: str, height: float):
    new_student = student_data.copy()
    new_student["id"] = str(uuid4())[:4] 
    new_student["name"] = name
    new_student["age"] = age
    new_student["sex"] = sex
    new_student["height"] = height
    
    student_dict[new_student["id"]] = new_student
    return {"message": "Added student Resource"}


# Update student
@app.put("/students/{id}")   
def update_student( id: str, name: str, age: int, sex: str, height: float):
    student = student_data.get(id)
    if id not in student_dict:
        raise HTTPException(status_code=404, detail="Student Resource not found")

    student["name"] = name
    student["age"] = age
    student["sex"] = sex
    student["height"] = height

    return {"message" : "The student resource has been updated"}

# Delete student
@app.delete("/students/{id}")
def delete_student(id: int):
    student = student_data.get(id)

    if student not in student_dict:
        raise HTTPException(status_code=404, detail="Student not found")

    del student_dict[student]
    return {"message": "Student deleted successfully"}