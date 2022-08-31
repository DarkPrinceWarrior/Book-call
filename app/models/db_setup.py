from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import config
from deta import Deta  # Import Deta
from config import deta_project_key  # project key for deta

engine = create_engine(f'postgresql://postgres:'
                       f'{config.password}@localhost:{config.port}/{config.db_name}')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()

# Initialize with a Project Key
deta = Deta(deta_project_key)


# create the db
def init_db():
    from app.models.entities import Role
    from app.models.entities import Users
    Base.metadata.create_all(engine)
