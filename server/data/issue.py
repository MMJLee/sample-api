from uuid import UUID
from databases import Database
from model.issue import BaseIssue
from data.utils import build_insert_statement, build_update_statement

class IssueData:
    def __init__(self, db: Database) -> None:
        self._db = db
    
    async def read_issue(self, id: UUID):
        record = await self._db.fetch_one(query=f"SELECT * FROM issue WHERE id = :id", values = {'id': id})
        return record

    async def read_issues(self):
        records = await self._db.fetch_all(query=f"SELECT * FROM issue ORDER BY updated_on DESC")
        return records
    
    async def create_issue(self, issue: BaseIssue):
        mapped_dict = issue.dict()
        fields, values = build_insert_statement(mapped_dict)
        query=f'''WITH insert as (INSERT INTO issue({fields}) VALUES({values}) RETURNING *)
                SELECT array_agg(id), count(id) as inserted from insert;'''
        record = await self._db.fetch_one(query=query, values=mapped_dict)
        return record
    
    async def update_issue(self, id: UUID, issue: BaseIssue):
        mapped_dict = issue.dict()
        values = build_update_statement(mapped_dict)
        mapped_dict['id'] = id
        query=f'''WITH update as (UPDATE issue SET {values} WHERE id = :id RETURNING *)
                SELECT array_agg(id), count(id) as updated from update;'''
        record = await self._db.fetch_one(query=query, values=mapped_dict)
        return record
    
    async def delete_issue(self, id: UUID):
        query=f'''WITH delete as (DELETE FROM issue WHERE id = :id RETURNING *)
            SELECT array_agg(id), count(id) as deleted from delete;'''
        record = await self._db.fetch_one(query=query, values={'id': id})
        return record