from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title="KN3AUX-CODE.CLOUD", description="Acode - A powerful code editor for Android")

# Serve the Acode web app from the www directory
app.mount("/static", StaticFiles(directory="www"), name="static")

@app.get("/")
def root():
    return FileResponse("www/index.html")

@app.get("/health")
def health():
    return {"status": "ok", "app": "KN3AUX-CODE.CLOUD"}
