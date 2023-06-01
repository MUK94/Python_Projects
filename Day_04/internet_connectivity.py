import socket

def check_internet_connection():
    try:
        # Attempt to connect to a reliable remote server
        socket.create_connection(("www.africaphageforum.com", 80))
        return True
    except OSError:
        pass
    return False

# Check internet connectivity
if check_internet_connection():
    print("Internet connection is available.")
else:
    print("Internet connection is not available.")
