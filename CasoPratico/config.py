import os

# Configuração do banco de dados a partir de variáveis de ambiente
DB_CONFIG = {
    'dbname': os.getenv('PGDATABASE'),
    'user': os.getenv('PGUSER'),
    'password': os.getenv('PGPASSWORD'),
    'host': os.getenv('PGHOST'),
    'port': os.getenv('PGPORT')
}

# Configuração do processamento em lote
BATCH_SIZE = 1000  # Número de logs para processar em um único lote
MAX_RETRIES = 3    # Número máximo de tentativas para operações no banco
RETRY_DELAY = 1    # Atraso entre tentativas em segundos