print("Hello module imported")
def do_GET(handler): 
    handler.wfile.write(f"Hello from hello module...I mean...just hello".encode("utf-8"))