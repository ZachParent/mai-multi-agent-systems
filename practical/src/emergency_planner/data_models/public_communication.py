from pydantic import BaseModel
from typing import List
from datetime import datetime

from .shared import Location, FireType
from .emergency_services import CallAssessment
from .firefighters import FirefightersResponseReport
from .medical_services import MedicalResponseReport


class EmergencyReport(BaseModel):
    call_assessment: CallAssessment
    firefighters_response_report: FirefightersResponseReport
    medical_response_report: MedicalResponseReport
    timestamp: datetime


# Search Related Cases Task
class RelatedCase(BaseModel):
    case_id: str
    location: Location
    fire_type: FireType
    summary: str


class RelatedCases(BaseModel):
    emergency_report: EmergencyReport
    related_cases: List[RelatedCase]


# Draft Initial Article Task
class DraftArticle(BaseModel):
    emergency_report: EmergencyReport
    title: str
    draft: str


# Integrate Additional Information Task
class IntegratedArticle(BaseModel):
    emergency_report: EmergencyReport
    draft: str
    integrated_sources: List[str]


# Review and Authorize Publication Task
class ReviewedArticle(BaseModel):
    emergency_report: EmergencyReport
    approved: bool
    comments: str
    report: str


# Provide Social Media Feedback Task
class SocialMediaFeedback(BaseModel):
    emergency_report: EmergencyReport
    feedback: str
    report: str
    approved: bool
    comments: str
