# Session

https://docs.sqlalchemy.org/en/13/orm/session_basics.html#when-do-i-construct-a-session-when-do-i-commit-it-and-when-do-i-close-it

## create session
```py
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from fastapi import Depends

# create engine
url = sa.engine.url.URL.create(**cfg)
engine = sa.create_engine(url, **kwargs)

# create session
LocalSession = sessionmaker(bind=engine)
def get_session():
    session = LocalSession()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
        
@router.post('/get', response_model=Union[MyClass, None])
def get_task(session: Session = Depends(get_session)) -> Optional[MyClass]:
    return api.get_task(session)
```  

## separate session from method and class
```py
from contextlib import contextmanager

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

def run_my_program():
    with session_scope() as session:
        my_func(session)
        my_class().query(session)
```
