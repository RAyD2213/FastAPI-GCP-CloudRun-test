# FastAPI Implementation Test
##  Final Result
jinja2templates  https://fastapi-gcp-cloudrun-test.du.r.appspot.com/

FASTAPI  https://fastapi-gcp-cloudrun-test.du.r.appspot.com/random

Also,you can use FastAPI‘s **swagger UI** to check
https://fastapi-gcp-cloudrun-test.du.r.appspot.com/docs
and https://fastapi-gcp-cloudrun-test.du.r.appspot.com/redoc



# Objective

This test aims to evaluate the proficiency of aspiring engineers in developing a basic web application using **FastAPI** and **Google Cloud**.

# Development Process 

##  Create a Virtual Environment
To create a directory named "ENV" in the current directory,

    py -m venv env
Activate the Virtual Environment
	  

 - WINDOWS


     .\[envname]\Scripts\activate
 - Linux，Mac

    source [envname]/bin/activate

## FASTAPI
follow https://fastapi.tiangolo.com/ step by step

### Install
    pip install fastapi
    pip install "uvicorn[standard]"

### Example 

  Create a file  `main.py`  with:


    from typing import Union
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
### Run it

    uvicorn main:app --reload

### Check it
Open your browser at [http://127.0.0.1:8000/items/5
You will see the JSON response as:

> {"item_id": 5, "q": "somequery"}


## Code Writing

 1. Using FASTAPI TEMPLATES with Jinja2Templates to style pages and generate random numbers；
 2. To write a GET request for generating random data using FASTAPI

## Deploy on Google Cloud Platform

 1. Install GOOGLE CLOUD SDK
 2. To create a project on the web and enable App Engine
 3. Run GOOGLE CLOUD SDK

Login

    gcloud anth login
Change PATH to APP
Deploy

    gcloud app deploy

**IF ERROR**

    gcloud app logs tail -s default

