import logging
import os

import dotenv

dotenv.load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

logging = logging.getLogger(__name__)

key = os.environ.get("fake_key")


def main():
    logging.info("Vlatipa un nouveau projet")


if __name__ == "__main__":
    main()
