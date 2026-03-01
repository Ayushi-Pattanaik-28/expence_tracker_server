from fastapi import FastAPI
from app.routes import authRoutes, expenseRoutes
from app.db.authDb import create_indexes
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_indexes()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(expenseRoutes.router)
app.include_router(authRoutes.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def welcome():
    return {"msg": "server is running"}