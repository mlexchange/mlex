from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List, Optional
from pydantic import BaseModel, validator, Field
from enum import Enum


node_db = {'1': 'vaughan'}
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


class User(BaseModel):
    username: str
    email: Optional[str] = None
    fullname: Optional[str] = None
    passwd_hash: str

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



@app.get("/cs/v1/nodes")
async def list_nodes():
    return node_db


@app.get("/cs/v1/nodes/{node_id}")
async def return_status():
    return('vaughan: running since 1999')


@app.post('/cs/v1/nodes/{node_id}/{job_id}')
async def launch_job(job: MLJob):
    return job
