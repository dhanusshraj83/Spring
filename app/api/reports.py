from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas import ReportCreate, ReportOut
from app.db import models
from app.api.auth import get_current_user
from app.services.ml_service import predict_phishing

router = APIRouter(prefix="/reports", tags=["reports"])

@router.post("/", response_model=ReportOut)
def create_report(report_in: ReportCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    label, score = predict_phishing(report_in.payload)
    report = models.Report(
        url=report_in.url,
        source=report_in.source,
        payload=report_in.payload,
        prediction=label,
        score=str(score),
        owner_id=current_user.id
    )
    db.add(report)
    db.commit()
    db.refresh(report)
    return report

@router.get("/", response_model=list[ReportOut])
def list_my_reports(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    reports = db.query(models.Report).filter(models.Report.owner_id == current_user.id).all()
    return reports

@router.get("/{report_id}", response_model=ReportOut)
def get_report(report_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    report = db.query(models.Report).get(report_id)
    if not report or report.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Report not found")
    return report
