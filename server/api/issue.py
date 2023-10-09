from typing import Sequence
from uuid import UUID
from fastapi import APIRouter, Depends, Path, Body
from model.issue import BaseIssue, Issue
from model.response import CreateResponse, DeleteResponse, UpdateResponse
from dependency import issue_logic_dependency
from logic.issue import IssueLogic

router = APIRouter()

@router.get("/{id}", response_model=Issue)
async def read_issue(issue_logic: IssueLogic = Depends(issue_logic_dependency), id:UUID = Path(...)):
    return await issue_logic.read_issue(id)

@router.get("", response_model=Sequence[Issue])
async def read_issues(issue_logic: IssueLogic = Depends(issue_logic_dependency)):
    return await issue_logic.read_issues()

@router.post("", response_model=CreateResponse)
async def create_issue(issue_logic: IssueLogic = Depends(issue_logic_dependency), issue:BaseIssue = Body(...)):
    return await issue_logic.create_issue(issue)

@router.put("/{id}", response_model=UpdateResponse)
async def update_issue(issue_logic: IssueLogic = Depends(issue_logic_dependency), id:UUID = Path(...), issue:BaseIssue = Body(...)):
    return await issue_logic.update_issue(id, issue)

@router.delete("/{id}", response_model=DeleteResponse)
async def delete_issue(issue_logic: IssueLogic = Depends(issue_logic_dependency), id:UUID = Path(...)):
    return await issue_logic.delete_issue(id)