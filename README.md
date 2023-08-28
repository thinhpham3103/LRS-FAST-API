# LRS FAST API for job submission
## DOCS & GUIDES:
Official guide for FASI API: https://fastapi.tiangolo.com/ \
LRS Python library source: https://eomhbbuild01.lrsinc.org/RemotePyInstaller/Documentation 

## Requirements:
Python/pip for Windows\
Code editor: VS Code or Notepad++ 

## Directions:
Extract LRS-FAST-API-main.zip.\
In file explorer, Go to directory of the script is installed, type cmd to open up the CLI.\
pip install "uvicorn[standard]".\
pip install LRS Python library using the link above.\
pip install jinja2 to use Jinja2Templates for user interface.\
Modify vpsx_url and uri (line 15 & 16) to your VPSX server.\
Modify the SubmittedJobs folder directory by copying the path where this script is installed and add "\SubmittedJobs\\" at the end. ex: r'C:\Users\e7024\Downloads\REST\app\SubmittedJobs\\'.\
After editing the code, save it and run "python main.py" in the CLI.\
Open the web browser and direct to the url: http://127.0.0.1:8000, there you will be able to upload a file.\
Once the file is submitted, the submitted job should be automatically in your PPQ.\
Ctrl + C to terminate the server.
