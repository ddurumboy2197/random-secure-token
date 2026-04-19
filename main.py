import secrets

def generate_secure_token(length=32):
    return secrets.token_urlsafe(length)

print(generate_secure_token())
