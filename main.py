from multiprocessing.util import get_logger
import services.confluence as confluence

logger=get_logger()

def main():
    logger.warning("Starting Confluence Assistance Application")
    confluence_service = confluence.confluenceservice()
    print(confluence_service)
if __name__ == "__main__":
    main()