import socket
import threading
import logging

HOST = '127.0.0.1'
PORT = 65432

def handle_client(conn, addr):
    logging.info(f"Подключен клиент: {addr}")
    try:
        data = conn.recv(1024)
        if data:
            message = data.decode('utf-8')
            logging.info(f"Получено от клиента {addr}: {message}")
            if message == "Hello, server":
                response = "Hello, client"
                conn.sendall(response.encode('utf-8'))
    except Exception as e:
        logging.error(f"Ошибка при работе с клиентом {addr}: {e}")
    finally:
        conn.close()

def main():
    logging.basicConfig(level=logging.INFO)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        logging.info(f"Сервер запущен и прослушивает {HOST}:{PORT}")
        try:
            while True:
                conn, addr = server_socket.accept()
                client_thread = threading.Thread(target=handle_client, args=(conn, addr))
                client_thread.daemon = True
                client_thread.start()
        except KeyboardInterrupt:
            logging.info("Сервер остановлен вручную.")

if __name__ == '__main__':
    main()
