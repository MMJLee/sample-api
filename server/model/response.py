from typing import List
from uuid import UUID
from pydantic import BaseModel, Field

class CreateResponse(BaseModel):
    id: List[UUID] = Field(..., title='created ids')
    created: int = Field(..., title='created count')

class UpdateResponse(BaseModel):
    id: List[UUID] = Field(..., title='updated ids')
    updated: int = Field(..., title='updated count')

class DeleteResponse(BaseModel):
    id: List[UUID] = Field(..., title='deleted ids')
    deleted: int = Field(..., title='deleted count')