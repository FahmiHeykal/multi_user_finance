from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api.routes import auth, transactions, export

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])
app.include_router(export.router, prefix="/export", tags=["Export"])
