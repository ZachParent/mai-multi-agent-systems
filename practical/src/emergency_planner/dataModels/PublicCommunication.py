from pydantic import BaseModel
from typing import List
from datetime import datetime

from .shared import Location, FireType

class ReceiveReport(BaseModel):
    report_id: str
    location: Location
    fire_type: FireType
    timestamp: datetime
    markdown_content: str

class RelatedCase(BaseModel):
    case_id: str
    location: Location
    fire_type: FireType
    summary: str

class SearchRelatedCasesOutput(BaseModel):
    related_cases: List[RelatedCase]
    total_cases: int

class DraftArticleOutput(BaseModel):
    title: str
    draft: str

class IntegratedArticleOutput(BaseModel):
    draft: str
    integrated_sources: List[str]

class ReviewOutput(BaseModel):
    approved: bool
    comments: str
    report: str

class SocialMediaFeedbackOutput(BaseModel):
    feedback: str
    report: str
    approved: bool
    comments: str

