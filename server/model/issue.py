from uuid import UUID
from pydantic import BaseModel, Field

class BaseIssue(BaseModel):
    title: str = Field(..., title='reference_id')
    description: str = Field(..., title='reference_id')

class Issue(BaseIssue):
    id: UUID = Field(..., title='id of issue')

