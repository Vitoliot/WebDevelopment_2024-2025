import socket
import logging

HOST = '127.0.0.1'
PORT = 65432

def main():
    logging.basicConfig(level=logging.INFO)
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            message = "Hello, server"
            client_socket.sendall(message.encode('utf-8'))
            data = client_socket.recv(1024)
            logging.info(f"Получено от сервера: {data.decode('utf-8')}")
    except Exception as e:
        logging.error(f"Ошибка соединения с сервером: {e}")

if __name__ == '__main__':
    main()
