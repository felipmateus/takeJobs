
import asyncio
import websockets

connected_clients = set()  # Track connected clients

async def handle_websocket(websocket, path):
    # Add client to the connected clients set
    connected_clients.add(websocket)
    try:
        while True:
            try:
                message = await websocket.recv()
                
                # Process the received message as needed
                print("Received message:", message)
                
                # Send the received message to all connected clients
                for client in connected_clients:
                    await client.send(message)

            except websockets.exceptions.ConnectionClosedError:
                break
    finally:
        # Remove client from the connected clients set
        connected_clients.remove(websocket)

start_server = websockets.serve(handle_websocket, "0.0.0.0" , 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
