import asyncio
import httpx
BASE_URL = "http://127.0.0.1:8000"

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL)

        print(f"Status Code: {response.status_code}")
        print(response.json())


if __name__ == '__main__':
    asyncio.run(main())


## python 0_