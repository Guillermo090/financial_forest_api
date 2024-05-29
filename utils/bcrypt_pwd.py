import bcrypt

def hash_password(password: str) -> str:
    # Generar un salt
    salt = bcrypt.gensalt()
    # Encriptar la contraseña
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


def check_password(password: str, hashed_password: str) -> bool:
    try:
        hashed_password_bytes = hashed_password.encode('utf-8')
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password_bytes)
    except Exception as e:
        print(f"Error al verificar la contraseña: {e}")
        return False