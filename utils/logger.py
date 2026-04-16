import logging
import json
import time
from functools import wraps
from flask import request

# Configuração básica de logging para saída padrão (stdout) no formato JSON
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("cinemaratona")

def log_request(f):
    """Decorator para logar detalhes da requisição e performance em formato JSON."""
    @wraps(f)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            response = f(*args, **kwargs)
            duration_ms = round((time.time() - start_time) * 1000)
            
            log_data = {
                "event": "request_success",
                "route": f.__name__,
                "method": request.method,
                "path": request.path,
                "duration_ms": duration_ms,
                "status": "ok"
            }
            logger.info(json.dumps(log_data))
            return response
        except Exception as e:
            duration_ms = round((time.time() - start_time) * 1000)
            log_data = {
                "event": "request_error",
                "route": f.__name__,
                "method": request.method,
                "path": request.path,
                "duration_ms": duration_ms,
                "error": str(e),
                "status": "error"
            }
            logger.error(json.dumps(log_data))
            raise
    return wrapper
