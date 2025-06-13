from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.schemas.transaction import TransactionCreate, TransactionOut
from app.crud.transaction import create_transaction, get_transactions

router = APIRouter()

@router.post("/", response_model=TransactionOut)
def create(trx: TransactionCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return create_transaction(db, user.id, trx.amount, trx.description)

@router.get("/", response_model=list[TransactionOut])
def list_all(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return get_transactions(db, user.id)
