from databases import Database
from fastapi import Depends
from starlette.requests import Request
from data.issue import IssueData
from logic.issue  import IssueLogic

def get_db(request: Request) -> Database:
    return request.app.state.database

def issue_data_dependency(db: Database = Depends(get_db)) -> IssueData:
    return IssueData(db=db)

def issue_logic_dependency(issue_data: IssueData = Depends(issue_data_dependency)) -> IssueLogic:
    return IssueLogic(issue_data=issue_data)