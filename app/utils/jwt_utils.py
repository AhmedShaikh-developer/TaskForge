import jwt
from datetime import datetime, timedelta

SECRET_KEY = "axtwV4mCRoRXcrP4DC2e-KkPZi5vd2-GMpAtaCYJjZY"

def create_jwt(data: dict):
    payload = {**data, "exp": datetime.utcnow() + timedelta(hours=1)}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_jwt(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])