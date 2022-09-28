from datetime import datetime

def log (tag="", message=""):
    formatted_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("log.txt", "a+") as log:
        log.write(f"{formatted_time}: {tag} - {message}\n")