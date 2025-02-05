from db_manager import DatabaseManager
from utils import validate_log, chunk_list
import logging
from config import BATCH_SIZE, MAX_RETRIES, RETRY_DELAY
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LogProcessor:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def process_logs(self, logs):
        """Processa uma lista de logs em lotes"""
        try:
            # Valida logs
            valid_logs = [log for log in logs if validate_log(log)]

            if len(valid_logs) != len(logs):
                logger.warning(f"Filtrados {len(logs) - len(valid_logs)} logs inválidos")

            # Processa em lotes
            for batch in chunk_list(valid_logs, BATCH_SIZE):
                self._process_batch_with_retry(batch)

        except Exception as e:
            logger.error(f"Erro ao processar logs: {e}")
            raise
        finally:
            self.db_manager.close()

    def _process_batch_with_retry(self, batch):
        """Processa um lote de logs com lógica de retry"""
        for attempt in range(MAX_RETRIES):
            try:
                self.db_manager.batch_insert_logs(batch)
                break
            except Exception as e:
                if attempt == MAX_RETRIES - 1:
                    logger.error(f"Falha ao processar lote após {MAX_RETRIES} tentativas")
                    raise
                logger.warning(f"Tentativa {attempt + 1}/{MAX_RETRIES} após erro: {e}")
                time.sleep(RETRY_DELAY)

def process_log(logs):
    """Ponto de entrada principal para processamento de logs"""
    processor = LogProcessor()
    processor.process_logs(logs)