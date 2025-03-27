import asyncio
import websockets

async def send_messages():
    uri = "ws://localhost:12345"
    async with websockets.connect(uri) as websocket:
        while True:
            message = input("Enter a message: ")
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Received: {response}")

if __name__ == "__main__":
    asyncio.run(send_messages())
