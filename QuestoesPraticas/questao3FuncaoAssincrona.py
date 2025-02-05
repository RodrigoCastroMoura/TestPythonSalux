import asyncio
import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def fetch_urls(urls: list):

    tasks = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

urls = [
    'https://www.example.com',
    'https://www.python.org',
    'https://www.github.com'
]

# Executa a função assíncrona
async def main():
    contents = await fetch_urls(urls)
    for content in contents:
        print(content[:100])  # Imprime os primeiros 100 caracteres de cada resposta

# Roda o loop de eventos
asyncio.run(main())