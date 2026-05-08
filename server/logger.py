import logging

def setup_logger(name="MedicalGPT"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Add formatter to handler
    ch.setFormatter(formatter)

    if not logger.hasHandlers():
        # Add handler to logger
        logger.addHandler(ch)

    return logger

logger = setup_logger()

logger.info("Logger initialized successfully.")
logger.debug("This is a debug message.")