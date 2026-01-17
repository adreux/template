import logging

from src.logger import setup_logging

setup_logging()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def template_function():
    logger.info("Log depuis src")


if __name__ == "__main__":
    template_function()
