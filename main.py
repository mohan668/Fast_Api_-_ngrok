# main.py

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# Create FastAPI app instance
app = FastAPI()

# Define the Command model to handle the incoming JSON body
class Command(BaseModel):
    action: str

# POST endpoint to receive command and process it
@app.post("/command")
async def send_command(command: Command):
    print(f"Received command: {command.action}")  # Print the command received
    # Here you can add more code to perform actions based on the command
    if command.action == "on":
        # Perform action for 'on'
        print("Turning motor on...")
    elif command.action == "off":
        # Perform action for 'off'
        print("Turning motor off...")
    elif command.action == "clockwise":
        # Perform action for clockwise
        print("Rotating motor clockwise...")
    elif command.action == "anticlockwise":
        # Perform action for anticlockwise
        print("Rotating motor anticlockwise...")
    
    # Return a response confirming the received command
    return {"message": f"Command '{command.action}' received successfully"}

# To run the app with `uvicorn` when this file is executed directly
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
