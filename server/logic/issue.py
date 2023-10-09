from typing import Optional, Sequence
from uuid import UUID
from data.issue import IssueData
from model.issue import Issue, BaseIssue
from model.response import CreateResponse, UpdateResponse, DeleteResponse

class IssueLogic:
    def __init__(self, issue_data: IssueData) -> None:
        self.issue_data = issue_data

    async def read_issue(self, id: UUID) -> Optional[Issue]:
        return await self.issue_data.read_issue(id)

    async def read_issues(self) -> Sequence[Optional[Issue]]:
        return await self.issue_data.read_issues()
    
    async def create_issue(self, issue: BaseIssue) -> CreateResponse:
        return await self.issue_data.create_issue(issue)

    async def update_issue(self, id: UUID, issue: BaseIssue) -> UpdateResponse:
        return await self.issue_data.update_issue(id, issue)
    
    async def delete_issue(self, id: UUID) -> DeleteResponse:
        return await self.issue_data.delete_issue(id)