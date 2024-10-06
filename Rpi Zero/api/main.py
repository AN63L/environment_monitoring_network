from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import health, metrics, notifications

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # you may want to update this for improved security
    # -> only your front-end should have access to this
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(health.router)

app.include_router(metrics.router)
app.include_router(notifications.router)
