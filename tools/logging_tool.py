import logging

logging.basicConfig(
    level=logging.INFO
)

logger = logging.getLogger(
    "bioacoustic_ai"
)

def log_message(message):

    logger.info(message)