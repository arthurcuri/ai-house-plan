"""
Database Configuration - SQLAlchemy database setup
Handles database connections, sessions, and initialization.
"""
import os
import logging

logger = logging.getLogger(__name__)

# Try to import SQLAlchemy, fallback to mock if not available
try:
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, Session
    from sqlalchemy.ext.declarative import declarative_base
    SQLALCHEMY_AVAILABLE = True
except ImportError:
    SQLALCHEMY_AVAILABLE = False
    logger.warning("SQLAlchemy not available - using mock database service")

if SQLALCHEMY_AVAILABLE:
    # Database configuration
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./auth.db")
    SQLITE_ECHO = os.getenv("SQLITE_ECHO", "false").lower() == "true"

    # Database engine configuration for SQLite
    engine = create_engine(
        DATABASE_URL, 
        connect_args={"check_same_thread": False},
        echo=SQLITE_ECHO,
    )

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
else:
    # Mock objects for when SQLAlchemy is not available
    engine = None
    SessionLocal = None
    Base = None
    Session = None


class DatabaseService:
    """Service for database operations"""
    
    @staticmethod
    def get_db():
        """Dependency to get database session"""
        if not SQLALCHEMY_AVAILABLE:
            return None
            
        db = SessionLocal()
        try:
            yield db
        except Exception as e:
            logger.error(f"Database session error: {e}")
            db.rollback()
            raise
        finally:
            db.close()

    @staticmethod
    def create_tables():
        """Create only the 'user' table in the database"""
        if not SQLALCHEMY_AVAILABLE:
            logger.warning("SQLAlchemy not available - skipping table creation")
            return

        try:
            # Import only the User model and create just its table
            try:
                from ..auth.models import User
                logger.info("Auth model 'User' imported successfully")
            except ImportError:
                logger.warning("Auth model 'User' not available - skipping table creation")
                return

            # Create only the User table (do not create any other tables)
            Base.metadata.create_all(bind=engine, tables=[User.__table__])
            logger.info("SQLite 'user' table created successfully")
        except Exception as e:
            logger.error(f"Error creating 'user' table: {e}")

    @staticmethod
    def init_db():
        """Initialize SQLite database"""
        if not SQLALCHEMY_AVAILABLE:
            logger.warning("SQLAlchemy not available - using mock database")
            return
            
        DatabaseService.create_tables()
        logger.info("SQLite database initialized for development")


# Legacy functions for backward compatibility
def get_db():
    """Legacy wrapper function"""
    if not SQLALCHEMY_AVAILABLE:
        return None
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"Database session error: {e}")
        db.rollback()
        raise
    finally:
        db.close()

def create_tables():
    """Legacy wrapper function"""
    return DatabaseService.create_tables()

def init_db():
    """Legacy wrapper function"""
    return DatabaseService.init_db()
    return DatabaseService.init_db()
    return DatabaseService.create_tables()

def init_db():
    """Legacy wrapper function"""
    return DatabaseService.init_db()
