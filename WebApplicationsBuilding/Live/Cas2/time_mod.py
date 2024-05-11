import datetime
print("Time module imported")
def do_GET(handler):
    current_time = datetime.datetime.now()
    handler.wfile.write(f"{current_time}".encode("utf-8"))