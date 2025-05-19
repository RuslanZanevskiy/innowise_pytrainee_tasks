import json

import logging 

logger = logging.getLogger(__name__)

class JsonReader():
    @staticmethod
    def read(file: str) -> dict:
        logger.info(f'reading json file {file}')
        return json.load(open(file, 'r', encoding='utf-8'))
