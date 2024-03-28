import aiohttp
import asyncio

async def update_mirror() -> str:
    url = "https://raw.githubusercontent.com/MrIkso/hdrezka-fetcher/main/mirror.txt"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                value = await response.text()
                # Здесь можно добавить логику для обновления URL, аналогично self.urlToSearch = value в оригинале
                return value
            else:
                raise Exception(f"Ошибка запроса: HTTP статус {response.status}")

# Пример использования
async def main():
    try:
        mirror_url = await update_mirror()
        print(mirror_url)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    asyncio.run(main())
