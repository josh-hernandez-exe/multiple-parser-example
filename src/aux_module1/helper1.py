import logging

logger = logging.getLogger(__name__)

def helper_function1(*args, **kwargs):
    logger.critical("This is a critical message from helper_function1")
    logger.error("This is an error message from helper_function1")
    logger.warning("This is a warning message from helper_function1")
    logger.debug("This is a debug message from helper_function1")
    logger.info("This is a debug message from helper_function1")

    logger.info("args: %s", args)
    logger.info("kwargs: %s", kwargs)
