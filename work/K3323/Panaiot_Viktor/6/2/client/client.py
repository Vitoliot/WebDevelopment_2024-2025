import socket
import logging

HOST = '127.0.0.1'
PORT = 65433

def main():
    logging.basicConfig(level=logging.INFO)
    print("Выберите операцию:")
    print("1. Площадь трапеции")
    print("2. Площадь параллелограмма")
    print("3. Теорема Пифагора")
    print("4. Решение квадратного уравнения")
    choice = input("Введите номер операции: ")

    if choice == '1':
        operation = "trapezoid"
        base1 = input("Введите первую базу трапеции: ")
        base2 = input("Введите вторую базу трапеции: ")
        height = input("Введите высоту трапеции: ")
        message = f"{operation},{base1},{base2},{height}"
    elif choice == '2':
        operation = "parallelogram"
        base = input("Введите основание параллелограмма: ")
        height = input("Введите высоту параллелограмма: ")
        message = f"{operation},{base},{height}"
    elif choice == '3':
        operation = "pythagoras"
        a = input("Введите первый катет: ")
        b = input("Введите второй катет: ")
        message = f"{operation},{a},{b}"
    elif choice == '4':
        operation = "quadratic"
        a = input("Введите коэффициент a: ")
        b = input("Введите коэффициент b: ")
        c = input("Введите коэффициент c: ")
        message = f"{operation},{a},{b},{c}"
    else:
        print("Неверный выбор операции")
        return

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            client_socket.sendall(message.encode('utf-8'))
            data = client_socket.recv(1024)
            print("Ответ от сервера:", data.decode('utf-8'))
    except Exception as e:
        logging.error(f"Ошибка при соединении с сервером: {e}")

if __name__ == '__main__':
    main()
