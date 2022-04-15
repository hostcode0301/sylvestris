from unicodedata import decimal
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import magic

# Create app instance

app = FastAPI()

# region CORS

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# endregion

# region Routes


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/hum", response_class=JSONResponse)
async def hum_detect(hum_file: UploadFile = File(..., description="Hum file to detect song")):
    # Check file extension
    if (hum_file.content_type not in ["audio/mpeg", "audio/mp3"]):
        raise HTTPException(400, detail="MP3 extension required")

    # Check MIME type
    # Rememer to install python-magic-bin in windows to use this OR libmagic1 in linux
    mime = magic.Magic(mime=True)
    flag = mime.from_buffer(hum_file.file.read(1024))
    if (flag not in ["audio/mpeg", "audio/mp3"]):
        raise HTTPException(400, detail="MP3 MIME type required")

    # Insert detect code here

    # Result
    return {"hum_name": hum_file.filename}

# endregion
