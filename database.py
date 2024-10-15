from os import environ
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists


def get_required_env_variable(name: str) -> str:
    variable = environ.get(name)
    if variable is None:
        raise EnvironmentError(f"Environment variable {name} is not set")
    return variable


DATABASE_HOST = get_required_env_variable("DATABASE_URL")
DATABASE_PORT = get_required_env_variable("DATABASE_PORT")
DATABASE_USERNAME = get_required_env_variable("DATABASE_USERNAME")
DATABASE_PASSWORD = get_required_env_variable("DATABASE_PASSWORD")
DATABASE_NAME = get_required_env_variable("DATABASE_NAME")

DATABASE_URL: str = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

if not database_exists(DATABASE_URL):
    create_database(DATABASE_URL)

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# add citext extension
with Session() as session:
    session.execute(text("CREATE EXTENSION IF NOT EXISTS citext;"))
    session.commit()
