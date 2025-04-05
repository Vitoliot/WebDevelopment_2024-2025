import socket
import logging

HOST = '127.0.0.1'
PORT = 65434

def main():
    logging.basicConfig(level=logging.INFO)
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            request = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(HOST)
            client_socket.sendall(request.encode('utf-8'))

            response = b""
            while True:
                chunk = client_socket.recv(1024)
                if not chunk:
                    break
                response += chunk
            print(response.decode('utf-8'))
    except Exception as e:
        logging.error(f"Ошибка при соединении с сервером: {e}")

if __name__ == '__main__':
    main()
