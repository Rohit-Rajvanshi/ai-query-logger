from sqlmodel import  Field , Session , create_engine , SQLModel
from typing import Annotated 
from fastapi import Depends



sqlite_url = f"sqlite:///database.db"
connect_args = {"check_same_thread" : False }
engine = create_engine(sqlite_url , connect_args = connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)



def get_session():
    with Session(engine) as session:
        yield session 

SessionDep = Annotated[Session , Depends(get_session)]

