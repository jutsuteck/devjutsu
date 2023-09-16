import requests

from fastapi import HTTPException, Header


def get_current_user(authorization: str = Header(None)) -> dict:
    response = requests.get(
        "http://auth_service:8000/users/me",
        headers={"Authorization": authorization})

    if response.status_code == 200:
        return response.json()

    raise HTTPException(status_code=401, detail="Invalid token")
