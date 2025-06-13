from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse
import io
import pandas as pd
from app.api.deps import get_db, get_current_user
from app.crud.transaction import get_transactions

router = APIRouter()

@router.get("/csv")
def export_csv(db: Session = Depends(get_db), user=Depends(get_current_user)):
    transactions = get_transactions(db, user.id)
    data = [{
        "ID": t.id,
        "Amount": t.amount,
        "Description": t.description,
        "Timestamp": t.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    } for t in transactions]

    df = pd.DataFrame(data)
    stream = io.StringIO()
    df.to_csv(stream, index=False)
    response = StreamingResponse(
        iter([stream.getvalue()]),
        media_type="text/csv"
    )
    response.headers["Content-Disposition"] = "attachment; filename=transactions.csv"
    return response
