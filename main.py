from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import sentry_sdk
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

from routes.einwand import router as einwand_router

# Configure Sentry
sentry_sdk.init(
    dsn="https://12e57a7f1b5254337bf92ed44434fcfa@o81097.ingest.us.sentry.io/4508164901634048",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

# Initialize FastAPI app
app = FastAPI(
    title="Access Bridge 2.0",
    description="Your App Description",
    version="Last Update - 2024.12.12"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Define a simple test route
@app.get("/")
def home():
    return {"message": "Hello from FastAPI on Render!"}

# Include all routers
app.include_router(einwand_router)

@app.get("/")
def home():
    return {"message": "Hello from FastAPI on Render!"}

# Main entry point
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "10000"))  # Render provides PORT dynamically
    uvicorn.run(app, host="0.0.0.0", port=port)
