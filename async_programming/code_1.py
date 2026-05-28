import asyncio

#async def — defining a coroutine
#Any function prefixed with async def becomes a coroutine. You must await it to actually run it.
    
async def greet(name):
    await asyncio.sleep(5)
    print(f"Hello, {name}!")
#asyncio.run(greet("Alice"))  # runs the event loop

# 2. await — suspending a coroutine
# await pauses the current coroutine and gives control back to the event loop, which can run other 
# coroutines in the meantime.
async def fetch_data():
    print("Fetching...")
    await asyncio.sleep(2) # simulate I/O wait
    print("Done!")
    return {"status":"okay"}

#asyncio.run() — the entry point
#This creates a new event loop, runs the given coroutine until it completes, then closes the loop. 
# Use it once, at the top level of your program.
async def main():
    await greet("Bob")

if __name__ == '__main__':
    asyncio.run(main())