import socket

def check_conn(url):
    try:
        socket.create_connection((url, 80))
        return True
    except OSError:
        pass
    return False

check_conn_site = check_conn("https://africaphageforum.org/")
if check_conn_site:
    print("Internet connection is available.")
else:
    print("Internet connection is not available.")