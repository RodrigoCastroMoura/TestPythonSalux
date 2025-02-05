import pandas as pd

data = {
    'id': [1, 2, 3, 4, 5],
    'nome': ['Alice', 'Bob', 'Carlos', 'Daniel', 'Eva'],
    'idade': [25, 30, 35, 40, 45],
    'salario': [5000, 7000, 8000, 10000, 12000]
}

df = pd.DataFrame(data)

def media_salarial_acima_de_30(df):
    # Filtra os funcionários com idade > 30
    filtro = df[df['idade'] > 30]
    # Calcula a média dos salários
    media = filtro['salario'].mean()
    return media

print(media_salarial_acima_de_30(df)) 