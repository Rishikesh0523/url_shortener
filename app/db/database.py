import os
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError
from app.core.config import settings

MAX_RETRIES = 10
WAIT_SECONDS = 2

# Use the test database URL if the TESTING environment variable is set to "true"
database_url = settings.test_database_url if os.getenv("TESTING", "").lower() == "true" else settings.database_url

for attempt in range(MAX_RETRIES):
    try:
        engine = create_engine(database_url)
        # Test connection immediately
        connection = engine.connect()
        connection.close()
        break
    except OperationalError as e:
        print(f"[DB INIT] Attempt {attempt + 1}/{MAX_RETRIES} - Database not ready: {e}")
        time.sleep(WAIT_SECONDS)
else:
    raise Exception("Database is not available after several retries.")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()