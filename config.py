import json
import logging
import os


class Config:
    # Configure logging module
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s' +
                                                    '- %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    # Bot specific settings.
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    with open('phrases.json', 'r') as file:
        PHRASES = json.load(file)
