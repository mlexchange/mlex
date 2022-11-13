# comments
# missing update data bucket database after uploading the files

# libraries
import datetime
from typing import List, Optional
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
# import dvc.api.open
from datetime import datetime
import uuid
import os


# classes
class DataBucket(BaseModel):
    name: str                           # filename
    type: str                           # type of file (e.g. csv)
    description: Optional[str] = None   # description of the file


# global variables
MODEL_PATH = 'model.pkl'
REPO_URL = 'https://github.com/mlexchange/dvc_registry'     # path to dvc repository
HOST_PATH = '/Users/tanchavez/Documents/Data/'                     # path to host
DATABASE_PATH = '/Users/tanchavez/Documents/Database/'             # path to database
HEADER = 'Project name, Type of data, Date, Time\n'     # header of data base file

# main body
app = FastAPI()


# API calls
# Requests creation of the data bucket in the host (local computer) as a directory and
# creates a new data bucket entry with metadata in the data base
# Returns data bucket ID to agent
@app.post("/ds/v1/data_buckets/")
async def creat_bucketID(databucket: DataBucket):
    bucketID = uuid.uuid1()             # creates a random bucket ID
    path = os.path.join(HOST_PATH, str(bucketID))
    os.makedirs(path)                   # creates directory in HOST_PATH, named after bucket ID
    f = open(DATABASE_PATH+databucket.name+".txt", "w+")        # creates the data base file
    now = datetime.now()
    f.write(HEADER+databucket.name+","+databucket.type+","+now.strftime("%m/%d/%Y, %H:%M:%S"))
    # with dvc.api.open(DATABASE_PATH+MODEL_PATH, REPO_URL) as fd:
    #     model = pickle.load(fd)
    return bucketID


# Uploads data to the data bucket directory and updates data bucket database
# Returns confirmation message
@app.post("/ds/v1/data_buckets/{bucketID}")
async def upload_file(bucketID, files: List[UploadFile] = File(...)):
    path = os.path.join(HOST_PATH, str(bucketID))
    for file in files:
        contents = await file.read()
        open(HOST_PATH + bucketID + '/' + file.filename, 'wb').write(contents)
    return {"Files uploaded successfully"}
