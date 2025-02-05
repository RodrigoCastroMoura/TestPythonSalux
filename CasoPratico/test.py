from log_processor import process_log
import datetime

# Logs de teste
test_logs = [
    {
        'timestamp': datetime.datetime.now().isoformat(),
        'level': 'INFO',
        'message': 'Mensagem de teste 1'
    },
    {
        'timestamp': datetime.datetime.now().isoformat(),
        'level': 'WARNING',
        'message': 'Mensagem de teste 2'
    },
    {
        'timestamp': datetime.datetime.now().isoformat(),
        'level': 'ERROR',
        'message': 'Mensagem de teste 3'
    }
]

# Processa os logs de teste
process_log(test_logs)
print('Processamento de logs concluído!')
