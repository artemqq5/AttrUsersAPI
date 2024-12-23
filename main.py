import os
from datetime import time, datetime

from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from domain.UserService import UserService

app = FastAPI()
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "venv", ".env"))

# Налаштування CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("REDIRECT_DOMAIN")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/v1/users/adduser")
async def add_user(request: Request):
    try:
        data = await request.json()
        print(f"\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        print(f"(add_user) Received Data: {data}")

        # Виклик бізнес-логіки
        success = UserService.add_user(data)

        if success:
            return JSONResponse(status_code=200, content={"status": "success", "message": "User added"})
        else:
            return JSONResponse(status_code=400, content={"status": "error", "message": "Failed to add user"})
    except ValueError as ve:
        print(f"Validation error in add_user: {ve}")
        return JSONResponse(status_code=400, content={"status": "error", "message": str(ve)})
    except Exception as e:
        print(f"Error in add_user: {e}")
        return JSONResponse(status_code=500, content={"status": "error", "message": "Internal server error"})


@app.post("/v1/users/checkuser")
async def check_user(request: Request):
    try:
        data = await request.json()
        print(f"\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        print(f"(check_user) Received Data: {data}")

        # Виклик бізнес-логіки
        result = UserService.check_user(data)
        if result:
            return result

        raise HTTPException(status_code=404, detail="User not found")
    except ValueError as ve:
        print(f"Validation error in check_user: {ve}")
        return JSONResponse(status_code=400, content={"status": "error", "message": str(ve)})
    except Exception as e:
        print(f"Error in check_user: {e}")
        return JSONResponse(status_code=500, content={"status": "error", "message": "Internal server error"})
