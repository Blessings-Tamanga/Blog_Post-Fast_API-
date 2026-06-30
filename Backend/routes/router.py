from fastapi import APIRouter
from tasks.crud import *

router = APIRouter()

@router.post("/posts")
def create_post():
    pass

@router.put("/posts/{id}")
def update_post():
    pass

@router.get("/posts")
def get_posts():
    pass

@router.get("/posts/{id}")
def get_post():
    pass

@router.delete("/posts/{id}")
def delete_post():
    pass

