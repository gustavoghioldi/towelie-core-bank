import logging

logger = logging.getLogger(__name__)
def account_ledger_receiver_post_save(sender, instance , created, raw, using, update_fields, **kwargs):
        logger.debug("account_ledger_receiver_post_save")
        
def account_ledger_receiver_pre_save(sender, instance , created, raw, using, update_fields, **kwargs):
        logger.debug("account_ledger_receiver_pre_save")