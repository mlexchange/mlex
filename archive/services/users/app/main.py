from fastapi import FastAPI, Depends, Body
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List, Optional
from pydantic import BaseModel, validator, Field
from enum import Enum

from users_db import (
    add_user,
    delete_user,
    retrieve_users,
)

node_db = {'1': 'vaughan'}
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


class User(BaseModel):
    username: str
    email: Optional[str] = None
    fullname: Optional[str] = None
    passwd_hash: str

    class Config:
        schema_extra = {
            "example": {
                'username': 'green',
                'email': 'green@lbl.gov',
                'fullname': 'Adam Green',
                'passwd_hash': 'mlexrunbigfast'
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message
    }


def ErrorResponseModel(error, code, message):
    return {'error': error, 'code': code, 'message': message}


class JobType(str, Enum):
    "users can enter either cpu or gpu (using the Enum class denotes a choice)"
    cpu = 'cpu'
    gpu = 'gpu'


class MLJob(BaseModel):
    job_id: int
    description: str
    job_type: JobType
    job_location: int
    docker_uri: str
    docker_cmd: str
    docker_cmd_args: List[str]


@app.get('/')
async def read_root():
    return{"message": "Manage Your MLExchange Users Here"}


@app.post("/us/v1/users")
async def create_user(user: User = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    return ResponseModel(new_user, "User added successfully")


@app.get("/us/v1/users")
async def list_users():
    users = await retrieve_users()
    if users:
        return ResponseModel(users, "User data retrieved succesfully")
    return ResponseModel(users, "Empty list returned")


@app.get("/cs/v1/nodes/{node_id}")
async def return_status():
    return('vaughan: running since 1999')


@app.post('/cs/v1/nodes/{node_id}/{job_id}')
async def launch_job(job: MLJob):
    return job
