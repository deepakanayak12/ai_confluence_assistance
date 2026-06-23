from utils.logger import get_logger
import services.confluence as confluence
import time

logger = get_logger()

def main():
    logger.info("Starting Confluence Assistance Application")
    
    max_retries = 3

    for attempt in range(max_retries):
        try:
            service = confluence.confluenceservice()
            logger.info(service)
            break

        except Exception as e:
            logger.error(f"Attempt {attempt+1}: {str(e)}")

            if attempt < max_retries - 1:
                logger.info("Retrying...")
                time.sleep(2)
            else:
                logger.critical("All retries failed", exc_info=True)


if __name__ == "__main__":
    main()