import jwt
from datetime import datetime, timedelta


SECRET_KEY = "mysecretkey"


def generate_jwt_token(user_id):
    expiry_date = datetime.utcnow() + timedelta(days=30)

    header = {"typ": "JWT", "alg": "HS256"}
    payload = {"sub": str(user_id), "exp": expiry_date}

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256", headers=header)

    return token
