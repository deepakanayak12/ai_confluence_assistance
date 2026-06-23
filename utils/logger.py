import logging
import os

log_dir = "logs"

def get_logger():
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger("confluence_app")
    logger.setLevel(logging.INFO)

    if not logger.handlers:  #prevents duplicate handlers
        log_file = os.path.join(log_dir, "application.log")

        # File handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger