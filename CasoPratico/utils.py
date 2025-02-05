from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def validate_log(log):
    """Valida uma entrada de log"""
    required_fields = ['timestamp', 'level', 'message']

    # Verifica campos obrigatórios
    if not all(field in log for field in required_fields):
        logger.warning(f"Campos obrigatórios ausentes no log: {log}")
        return False

    # Valida timestamp
    try:
        if isinstance(log['timestamp'], str):
            datetime.fromisoformat(log['timestamp'].replace('Z', '+00:00'))
    except ValueError:
        logger.warning(f"Formato de timestamp inválido no log: {log}")
        return False

    # Valida nível do log
    valid_levels = {'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'}
    if log['level'] not in valid_levels:
        logger.warning(f"Nível de log inválido no log: {log}")
        return False

    # Valida mensagem
    if not isinstance(log['message'], str) or not log['message'].strip():
        logger.warning(f"Mensagem inválida no log: {log}")
        return False

    return True

def chunk_list(lst, chunk_size):
    """Divide uma lista em pedaços do tamanho especificado"""
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]