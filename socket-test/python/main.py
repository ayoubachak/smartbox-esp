import socket
import asyncio
import websockets

server_ip = socket.gethostbyname(socket.gethostname())
server_port = 3000
async def onWebSocketEvent(websocket, path):
    client_ip = websocket.remote_address[0]
    print(f"New connection from {client_ip}")
    async for message in websocket:
        print(f"Received message from {client_ip}: {message}")
        await websocket.send(message)

async def startWebSocketServer():
    # Use the websockets library to create a server that listens on all network interfaces on port 8080
    server = await websockets.serve(onWebSocketEvent, "0.0.0.0", server_port)
    # Print a message to indicate that the server has started successfully
    print(f"WebSocket server started on {server_ip}:{server_port}")
    # Use an asyncio.Future object to keep the server running indefinitely
    await asyncio.Future()  # Wait forever

if __name__ == "__main__":
    # Start the asyncio event loop and run the WebSocket server
    asyncio.run(startWebSocketServer())

