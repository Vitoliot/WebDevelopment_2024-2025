import socket
import threading
import logging
import math

HOST = '127.0.0.1'
PORT = 65433

def handle_client(conn, addr):
    logging.info(f"Клиент подключен: {addr}")
    try:
        data = conn.recv(1024)
        if data:
            message = data.decode('utf-8')
            logging.info(f"Получено сообщение от {addr}: {message}")
            parts = message.split(',')
            if len(parts) < 2:
                response = "Ошибка: недостаточно параметров"
            else:
                operation = parts[0].strip().lower()
                try:
                    if operation == "trapezoid":
                        if len(parts) != 4:
                            response = "Ошибка: для трапеции нужны 3 параметра (база1, база2, высота)"
                        else:
                            base1, base2, height = map(float, parts[1:4])
                            area = ((base1 + base2) * height) / 2
                            response = f"Площадь трапеции: {area}"
                    elif operation == "parallelogram":
                        if len(parts) != 3:
                            response = "Ошибка: для параллелограмма нужны 2 параметра (основание, высота)"
                        else:
                            base, height = map(float, parts[1:3])
                            area = base * height
                            response = f"Площадь параллелограмма: {area}"
                    elif operation == "pythagoras":
                        if len(parts) != 3:
                            response = "Ошибка: для теоремы Пифагора нужны 2 параметра (катеты)"
                        else:
                            a, b = map(float, parts[1:3])
                            c = math.sqrt(a**2 + b**2)
                            response = f"Гипотенуза: {c}"
                    elif operation == "quadratic":
                        if len(parts) != 4:
                            response = "Ошибка: для квадратного уравнения нужны 3 параметра (a, b, c)"
                        else:
                            a, b, c = map(float, parts[1:4])
                            discriminant = b**2 - 4 * a * c
                            if discriminant < 0:
                                response = "Нет вещественных корней"
                            elif discriminant == 0:
                                x = -b / (2 * a)
                                response = f"Один корень: {x}"
                            else:
                                x1 = (-b + math.sqrt(discriminant)) / (2 * a)
                                x2 = (-b - math.sqrt(discriminant)) / (2 * a)
                                response = f"Два корня: {x1} и {x2}"
                    else:
                        response = "Ошибка: неизвестная операция"
                except Exception as e:
                    response = "Ошибка при обработке параметров: " + str(e)
            conn.sendall(response.encode('utf-8'))
    except Exception as e:
        logging.error(f"Ошибка при работе с клиентом {addr}: {e}")
    finally:
        conn.close()
        logging.info(f"Соединение с {addr} закрыто.")

def main():
    logging.basicConfig(level=logging.INFO)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        logging.info(f"Сервер запущен и слушает {HOST}:{PORT}")
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
