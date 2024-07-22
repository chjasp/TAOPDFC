from fastapi import FastAPI, File, UploadFile, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from google.cloud import storage
from typing_extensions import Annotated
from .config import settings

app = FastAPI()
templates = Jinja2Templates(directory="templates")

print(settings.gcp_bucket_name)

storage_client = storage.Client(project=settings.gcp_project_id)

async def validate_pdf(pdf_file: Annotated[UploadFile, File()]):
    if pdf_file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    return pdf_file

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.html")



@app.post("/upload")
async def upload_pdf(pdf_file: UploadFile = Depends(validate_pdf)):
    return {"name": pdf_file.filename, "content_type": pdf_file.content_type}

