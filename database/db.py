from mongoengine import connect
from config import config

def initialize_db():
    """
    Initialize the connection to the MongoDB database.
    """
    # Assuming your config function returns a dictionary or object containing database configurations
    db_config = config()

    connect(
        db=db_config.get('DB_NAME', 'watch'),
        host=db_config.get('DB_HOST', '127.0.0.1'),
        port=db_config.get('DB_PORT', 27017),
        username=db_config.get('DB_USER', 'admin'),
        password=db_config.get('DB_PASS', 'DSFgTRgvrtGBSEgeregSFvt3t34Ve347ui8i8752gDSGDBdsfsd6f216f1as6f1vfervgegRhe5'),
        authentication_source='admin',  # حتما روی admin باشه
    )

