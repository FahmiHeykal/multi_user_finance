from sqlalchemy.orm import Session
from app.db.models.transaction import Transaction

def create_transaction(db: Session, user_id: int, amount: float, description: str):
    trx = Transaction(user_id=user_id, amount=amount, description=description)
    db.add(trx)
    db.commit()
    db.refresh(trx)
    return trx

def get_transactions(db: Session, user_id: int):
    return db.query(Transaction).filter(Transaction.user_id == user_id).all()
