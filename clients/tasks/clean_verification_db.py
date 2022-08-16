import logging
from datetime import datetime, timedelta
from app.settings import CLIENT_VERIFICATION_EMAIL_TIME
from clients.models.signup import Signup

logger = logging.getLogger(__name__)

def run():
    logging.debug("clean_verification_db")
    now_plus = datetime.now()+timedelta(hours=CLIENT_VERIFICATION_EMAIL_TIME)
    signup_to_delete = Signup.objects.filter(expires_at__lt=now_plus)
    signup_to_delete.delete()
    
        