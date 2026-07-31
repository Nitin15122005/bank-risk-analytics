from fastapi import FastAPI

app = FastAPI(
    title="Bank Risk Analytics API",
    description="Backend API for Banking Risk Analytics Platform",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Bank Risk Analytics API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }