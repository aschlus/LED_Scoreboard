import sys
import threading
import server
import socket

def launch(server_socket):
    print("App Started")

    server_thread = threading.Thread(target=server.start_server, args=[server_socket])
    server_thread.daemon = True
    server_thread.start()

    while True:
        continue


if __name__ ==  "__main__":
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        launch(server_socket)
    except KeyboardInterrupt:
        print("Exiting...")
        server_socket.close()
        print("Socket Closed")
        sys.exit(0)