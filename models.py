from sqlmodel import SQLModel , Field 
from datetime import datetime 

class QueryBase(SQLModel):
    question : str = Field(min_length = 1 , max_length = 1000)

class Query(QueryBase , table = True):
    id : int | None = Field(default = None , primary_key = True)
    answer : str = Field (max_length = 10000)
    created_at : datetime = Field (default_factory = datetime.utcnow)

class QueryPublic (QueryBase):
    id : int 
    answer : str = Field (max_length = 10000)
    created_at : datetime 


class QueryCreate (QueryBase):
    pass 


