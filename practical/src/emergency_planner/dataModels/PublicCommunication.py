from pydantic import BaseModel
from typing import List, Tuple

class ReceiveReportOutput(BaseModel):
    report_id: str
    location: Tuple[float,float]
    fire_type: str
    timestamp: str
    markdown_content: str

class RelatedCase(BaseModel):
    case_id: str
    location: Tuple[float,float]
    fire_type: str
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

