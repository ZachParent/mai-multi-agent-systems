from pydantic import BaseModel
from typing import List
from datetime import datetime

from .shared import FireSeverity, FireType
from .emergency_services import CallAssessment
from .firefighters import FirefightersResponseReport
from .medical_services import MedicalResponseReport


class EmergencyReport(BaseModel):
    call_assessment: CallAssessment
    firefighters_response_report: FirefightersResponseReport
    medical_response_report: MedicalResponseReport
    timestamp: datetime
    fire_type: FireType
    fire_severity: FireSeverity
    location_x: float
    location_y: float


# Search Related Cases Task
class RelatedCase(BaseModel):
    case_id: int
    fire_severity: FireSeverity
    location_x: float
    location_y: float
    summary: str


class RelatedCases(BaseModel):
    related_cases: List[RelatedCase]


# Draft Initial Article Task
class DraftArticle(BaseModel):
    title: str
    public_communication_report: str


# Integrate Additional Information Task
class IntegratedArticle(BaseModel):
    public_communication_report: str
    integrated_sources: List[str]


# Review and Authorize Publication Task
class ReviewedArticle(BaseModel):
    mayor_approved: bool
    mayor_comments: str


# Final Output
class PublicCommunicationReport(BaseModel):
    public_communication_report: str
    mayor_approved: bool
    mayor_comments: str
    social_media_feedback: str
