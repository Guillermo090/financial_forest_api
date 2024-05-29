from jwt import encode, decode

SECRET_KEY="my_secret_key"

def create_token(data: dict) -> str:
    token: str = encode(payload=data, key=SECRET_KEY, algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    data: dict = decode(token, key=SECRET_KEY, algorithms=['HS256'])
    return data