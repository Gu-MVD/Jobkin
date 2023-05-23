def verify(login: str, password: str) -> bool:
    if login == "admin" and password == "admin":
        return True
    return False
