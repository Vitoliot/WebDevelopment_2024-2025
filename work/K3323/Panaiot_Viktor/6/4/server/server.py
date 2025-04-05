import socket
import threading
import logging

HOST = '0.0.0.0'
PORT = 65435

clients = {}
client_id_counter = 1
lock = threading.Lock()


def broadcast_message(message, sender_id):
    with lock:
        for client_id, client_socket in clients.items():
            if client_id != sender_id:
                try:
                    client_socket.sendall(f"Сообщение от {sender_id}: {message}\n".encode('utf-8'))
                except Exception as e:
                    logging.error("Ошибка отправки сообщения клиенту %s: %s", client_id, e)


def handle_client(client_socket, client_id):
    try:
        client_socket.sendall(f"Ваш ID: {client_id}\n".encode('utf-8'))
        while True:
            data = client_socket.recv(1024)
            if not data:
                logging.info("Клиент %s отключился", client_id)
                break
            message = data.decode('utf-8').strip()

            # Если сообщение не содержит ":", трактуем его как broadcast
            if ':' not in message:
                broadcast_message(message, client_id)
                client_socket.sendall("Сообщение отправлено всем.\n".encode('utf-8'))
                continue

            target_id_str, message_text = message.split(":", 1)
            target_id_str = target_id_str.strip()
            message_text = message_text.strip()
            try:
                target_id = int(target_id_str)
            except ValueError:
                client_socket.sendall("ID получателя должен быть числом.\n".encode('utf-8'))
                continue

            with lock:
                if target_id in clients:
                    target_socket = clients[target_id]
                    try:
                        target_socket.sendall(f"Сообщение от {client_id}: {message_text}\n".encode('utf-8'))
                        client_socket.sendall("Сообщение отправлено.\n".encode('utf-8'))
                    except Exception as e:
                        client_socket.sendall(f"Ошибка при отправке сообщения: {e}\n".encode('utf-8'))
                else:
                    client_socket.sendall(f"Клиент с ID {target_id} не найден.\n".encode('utf-8'))
    except Exception as e:
        logging.error("Ошибка у клиента %s: %s", client_id, e)
    finally:
        with lock:
            if client_id in clients:
                del clients[client_id]
        client_socket.close()
        logging.info("Клиент %s отключился", client_id)


def main():
    global client_id_counter
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    logging.info("Сервер запущен и слушает %s:%s", HOST, PORT)

    try:
        while True:
            client_socket, addr = server_socket.accept()
            with lock:
                assigned_id = client_id_counter
                client_id_counter += 1
                clients[assigned_id] = client_socket
            logging.info("Новое подключение от %s. Присвоен ID: %s", addr, assigned_id)
            thread = threading.Thread(target=handle_client, args=(client_socket, assigned_id), daemon=True)
            thread.start()
    except KeyboardInterrupt:
        logging.info("Сервер остановлен.")
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
