import logging

logger = logging.getLogger(__name__)

class EmailService:
    def send(self):
        logger.debug(f"send {self}")