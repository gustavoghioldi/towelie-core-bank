import os
from logging import Handler
from newrelic_telemetry_sdk import Log, LogClient

log_client = LogClient(os.environ["NEW_RELIC_LICENSE_KEY"])
entity_name = os.environ['NEW_RELIC_APP_NAME']

class NRHandler(Handler):
    def handle(self, record):
        try:
            log = Log({"message":self.format(record),"entity.name":entity_name})
            self._get_log(log)
            
        except RecursionError:  # See issue 36272
            raise
        except Exception:
            self.handleError(record)
    
    def _get_log(self, log):
        log_client.send(log)        