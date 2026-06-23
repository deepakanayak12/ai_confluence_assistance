from utils.logger import get_logger

logger = get_logger()

def confluenceservice():
    message = "Confluence Service Initialized"
    logger.info(message)
    return message