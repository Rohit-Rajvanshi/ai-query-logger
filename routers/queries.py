from fastapi import APIRouter , HTTPException , Query as FastAPIQuery
from models import *
from database import SessionDep
from llm import ask_query
from typing import Annotated
from sqlmodel import Session , select 


router = APIRouter(
    prefix = "/queries"
)

@router.post("/" , response_model = QueryPublic)
def post_query(query : QueryCreate , session : SessionDep):
    question_query = query.question
    answer_text = ask_query(question_query)
    db_query = Query(answer = answer_text , question = query.question )
    session.add(db_query)
    session.commit()
    session.refresh(db_query)
    return db_query

@router.get("/{query_id}" , response_model = QueryPublic)
def get_query(query_id : int , session : SessionDep ):
    db_query = session.get(Query , query_id )

    if db_query is None:
        raise HTTPException(status_code = 404 , detail = "Query not found")

    return db_query

@router.delete("/{query_id}")
def delete_query(query_id : int , session : SessionDep ):
    db_query = session.get(Query , query_id )

    if not db_query:
        raise HTTPException(status_code = 404 , detail = "Query not found")

    session.delete(db_query)
    session.commit()

    return{"deleted" : True }

@router.get("/" , response_model = list[QueryPublic])
def get_queries(session : SessionDep ,
    offset : int = 0 ,
    limit : Annotated[int , FastAPIQuery(le = 100) ] = 100):
    queries = session.exec(select(Query).offset(offset).limit(limit)).all()
    return queries 



