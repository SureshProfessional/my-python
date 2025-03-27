import asyncio
import websockets

async def handle_connection(websocket, path):
    async for message in websocket:
        print(f"Received: {message}")
        await websocket.send(f"Echo: {message}")

async def main():
    async with websockets.serve(handle_connection, "localhost", 12345):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
