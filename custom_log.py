from datetime import datetime
from fastapi.requests import Request


def log (tag="App", message="", request: Request = None):
    formatted_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("log.txt", "a+") as log:
        log.write(f"{formatted_time}: {tag} {message}\n")
        log.write(f"{formatted_time}: {request.url}")