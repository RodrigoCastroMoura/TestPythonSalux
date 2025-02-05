import psycopg2
from psycopg2.extras import execute_values
import logging
from config import DB_CONFIG
import time
from contextlib import contextmanager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseManager:
    def __init__(self):
        self.config = DB_CONFIG
        self._conn = None

    @contextmanager
    def get_connection(self):
        """Gerenciador de contexto para conexões com o banco de dados"""
        if self._conn is None:
            try:
                self._conn = psycopg2.connect(**self.config)
            except psycopg2.Error as e:
                logger.error(f"Falha ao conectar ao banco de dados: {e}")
                raise

        try:
            yield self._conn
        except psycopg2.Error as e:
            if self._conn:
                self._conn.rollback()
            logger.error(f"Ocorreu um erro no banco de dados: {e}")
            raise

    @contextmanager
    def get_cursor(self):
        """Gerenciador de contexto para cursores do banco de dados"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            try:
                yield cursor
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise
            finally:
                cursor.close()

    def batch_insert_logs(self, logs):
        """Insere múltiplos logs usando execute_values"""
        if not logs:
            return

        query = """
            INSERT INTO logs (timestamp, level, message)
            VALUES %s
        """

        # Converte logs para formato de tupla para execute_values
        values = [(
            log['timestamp'],
            log['level'],
            log['message']
        ) for log in logs]

        with self.get_cursor() as cursor:
            try:
                execute_values(cursor, query, values, page_size=1000)
                logger.info(f"Inseridos {len(logs)} logs com sucesso")
            except psycopg2.Error as e:
                logger.error(f"Falha ao inserir logs: {e}")
                raise

    def close(self):
        """Fecha a conexão com o banco de dados"""
        if self._conn is not None:
            self._conn.close()
            self._conn = None