from utils.logger import get_logger
import services.confluence as confluence
import time
import database.db as db

logger = get_logger()

def main():
    logger.info("Starting Confluence Assistance Application")
    db.create_tables()
    
    max_retries = 3

    for attempt in range(max_retries):
        try:
            service = confluence.confluenceservice()
            try:
                db.insert_data(service)
            except Exception as db_e:
                logger.error(f"Failed to write success to DB: {db_e}")

            logger.info(service)
            break

        except Exception as e:
            try:
                db.insert_error_log(str(e))
            except Exception as db_e:
                logger.error(f"Failed to write error to DB: {db_e}")

            logger.error(f"Attempt {attempt+1}: {str(e)}")

            if attempt < max_retries - 1:
                logger.info("Retrying...")
                time.sleep(2)
            else:
                logger.critical("All retries failed", exc_info=True)


if __name__ == "__main__":
    main()