from fastapi import FastAPI, UploadFile
from util import pipeline

uvicorn main: app --port 5500

# Initializing App
app = FastAPI()

# Allowing Cross Origins
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Schema For Request
from pydantic import BaseModel
class Schema(BaseModel):
	# img_base64:str
    img: UploadFile

print(" ........... App Started ........... ")

# Endpoints

@app.get("/")
def index():
	return "This is the API for EHospital Webpage"
      
@app.post("/predict")
def endpoint_face_analytics(img: UploadFile):
	response =  pipeline(img)
	return response

# @app.post("/predict")
# def endpoint_face_analytics(req: Schema):
# 	response =  pipeline(req.img_base64)
# 	return response
