import socket
import threading
import logging

HOST = '0.0.0.0'
PORT = 65434


def handle_client(client_connection, client_address):
    logging.info(f"Подключение от: {client_address}")
    try:
        request_data = client_connection.recv(1024)
        request_text = request_data.decode('utf-8')
        logging.info(f"Получен запрос:\n{request_text}")

        # Простейший анализ HTTP-запроса
        request_line = request_text.splitlines()[0]
        method, path, _ = request_line.split()
        if method != 'GET' or path != '/':
            status_line = "HTTP/1.1 405 Method Not Allowed\r\n"
            response_body = "<html><body><h1>405 Method Not Allowed</h1></body></html>"
        else:
            try:
                with open('index.html', 'r', encoding='utf-8') as file:
                    response_body = file.read()
                status_line = "HTTP/1.1 200 OK\r\n"
            except FileNotFoundError:
                response_body = "<html><body><h1>404 Not Found</h1></body></html>"
                status_line = "HTTP/1.1 404 Not Found\r\n"

        response_headers = (
            "Content-Type: text/html; charset=utf-8\r\n"
            f"Content-Length: {len(response_body.encode('utf-8'))}\r\n"
            "\r\n"
        )
        response = status_line + response_headers + response_body
        client_connection.sendall(response.encode('utf-8'))
    except Exception as e:
        logging.error(f"Ошибка при обработке запроса от {client_address}: {e}")
    finally:
        client_connection.close()
        logging.info(f"Соединение с {client_address} закрыто.")


def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        logging.info(f"HTTP сервер запущен и слушает {HOST}:{PORT}")

        try:
            while True:
                client_connection, client_address = server_socket.accept()
                client_thread = threading.Thread(target=handle_client, args=(client_connection, client_address))
                client_thread.daemon = True
                client_thread.start()
        except KeyboardInterrupt:
            logging.info("Сервер остановлен вручную.")


if __name__ == '__main__':
    main()
