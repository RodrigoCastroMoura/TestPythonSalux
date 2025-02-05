# TestePythonSalux

## Questões Teóricas
As perguntas e resposntas do teste estão na pasta QuestoesTeoricas em PDF

## Questões Práticas:
Estão na pasta QuestoesTeoricas QuestoesPraticas em aquivos .py

## Caso Prático
Está na pasta QuestoesTeoricas CasoPratico em aquivos .py
Como Executar o teste no Visual Studio Code?

### 1. Preparação do Ambiente

1. Clone o repositório para sua máquina local
2. Abra o VSCode e instale as extensões recomendadas:
   - Python
   - PostgreSQL

### 2. Configuração do Python

1. Ative o ambiente virtual:
   - Windows:
   ```bash
   .\venv\Scripts\activate
   ```
   - Linux/Mac:
   ```bash
   source venv/bin/activate
   ```

2. Instale as dependências:
```bash
pip install psycopg2-binary python-dateutil
```
### 3. Configuração do Banco de Dados

1. Configure as variáveis de ambiente no arquivo `.env`:
```env
PGDATABASE=seu_banco
PGUSER=seu_usuario
PGPASSWORD=sua_senha
PGHOST=localhost
PGPORT=5432
```

2. Execute o script de criação das tabelas:
```bash
psql -U seu_usuario -d seu_banco -f schema.sql
```

### 4. Executando o Sistema

1. Crie um arquivo de teste `test.py`:

```python
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
    }
]

# Processa os logs de teste
process_log(test_logs)
```

3. Execute o arquivo de teste:
   - Clique com o botão direito no arquivo `test.py` no VSCode
   - Selecione "Run Python File in Terminal"
   ou
   - No terminal:
   ```bash
   python test.py
   ```

## Configurações

As configurações do sistema podem ser ajustadas no arquivo `config.py`:

- `BATCH_SIZE`: Número de logs processados por lote (default: 1000)
- `MAX_RETRIES`: Número máximo de tentativas para operações no banco (default: 3)
- `RETRY_DELAY`: Atraso entre tentativas em segundos (default: 1)

   ```sql
   -- Ver últimos logs inseridos
   SELECT * FROM logs ORDER BY timestamp DESC LIMIT 10;

   -- Ver contagem de logs por nível
   SELECT level, COUNT(*) as total FROM logs GROUP BY level;

   -- Ver logs de um período específico
   SELECT * FROM logs 
   WHERE timestamp >= NOW() - INTERVAL '1 hour'
   ORDER BY timestamp DESC;