import logging

logger = logging.getLogger(__name__)
def send_verification_email(user, uuid_signup):
    logging.debug("send verification email")
    