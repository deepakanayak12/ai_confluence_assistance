import random

from utils.logger import get_logger

logger = get_logger()

def confluenceservice():
    if random.choice([True, False]):
        raise Exception ("Failed to initialize Confluence Service")
    return "Confluence Service Initialized"