import socket
import threading
import logging

HOST = '127.0.0.1'
PORT = 65435

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                logging.info("Соединение с сервером потеряно.")
                break
            print(data.decode('utf-8').strip())
        except Exception as e:
            logging.error("Ошибка при получении сообщения: %s", e)
            break

def main():
    logging.basicConfig(level=logging.INFO)
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            logging.info("Подключено к серверу %s:%s", HOST, PORT)

            thread = threading.Thread(target=receive_messages, args=(client_socket,), daemon=True)
            thread.start()

            while True:
                msg = input()
                if msg.lower() == 'exit':
                    logging.info("Выход из чата.")
                    break
                client_socket.sendall(msg.encode('utf-8'))
    except Exception as e:
        logging.error("Ошибка клиента: %s", e)

if __name__ == "__main__":
    main()
