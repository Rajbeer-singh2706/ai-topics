
import asyncio

# asyncio.gather()
# Runs multiple coroutines concurrently — all start immediately, and you wait for all to finish.

async def task(n):
    await asyncio.sleep(n)
    return f"done in {n}s"

async def main():
    results = await asyncio.gather(
        task(1),
        task(2),
        task(3),
    )
    print(results)
    # takes -3s total, not 6s

if __name__ == '__main__':
    asyncio.run(main())