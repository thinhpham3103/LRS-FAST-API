from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from lrs.ipp import IPP_VPSX
import os
import uvicorn
import shutil
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

vpsx_url    = 'http://HW09971.lrsinc.org:631'
uri         = 'ipp://HW09971.lrsinc.org:631/PPQ';    # uri must start with http:// or ipp:// and PPQ of your choice

@app.get("/", response_class=HTMLResponse)
async def upload(request: Request):
   return templates.TemplateResponse("uploadfile.html", {"request": request})

@app.post("/upload")
async def create_upload_file(file: UploadFile = File(...)):
    ## Create a folder that contains of submitted jobs
    folder = r'C:\Users\e7024\Downloads\REST\app\SubmittedJobs\\' #This folder path needs to be changed based on user's working station
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    ## Write the submitted job onto a new file within the SubmittedJobs folder to send it to VPSX
    print_job = folder + file.filename
    with open(print_job, "wb") as buffer:
      shutil.copyfileobj(file.file, buffer)

    ## Create a VPSX client instance
    vpsx = IPP_VPSX( url=vpsx_url )
    # vpsx.EnableSSL(1)

    ## High level API : Print Job & Initialize PrintJob request
    vpsx.PrintJob(uri, os.path.abspath(print_job));
    vpsx.Submit()

    if vpsx.Error():
        return("There was an error",
                "Error code       : " + vpsx.ErrorCode(),
                "ErrorStatusCode  : " + vpsx.ErrorStatusCode(),
                "ErrorDescription : " + vpsx.ErrorDescription())
        exit(12)

    return ("Job created!",
            "Job URI = " + vpsx.GetJobURI(1),
            "Job ID  = " + vpsx.GetJobID(1),
            "Filepath = " + os.path.abspath(print_job))

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000,reload=True)
