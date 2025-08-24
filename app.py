from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import io

app = FastAPI()

# Allow your Wix domain (replace with your real domain before deploying)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://harborautomation.com",
    ],
    allow_methods=["GET","POST","OPTIONS"],
    allow_headers=["*"],
)

@app.post("/submit")
async def submit(name: str = Form(...)):
    # Your logic goes here. For now we return both styles:

    # Example 1: JSON response
    # return JSONResponse({"message": f"Hello {name}!"})

    # Example 2: File download
    content = f"Hello {name}!\nThis is your generated file."
    buf = io.BytesIO(content.encode("utf-8"))
    return StreamingResponse(
        buf,
        media_type="text/plain",
        headers={"Content-Disposition": "attachment; filename=hello.txt"},
    )
