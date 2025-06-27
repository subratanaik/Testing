import socket
import threading
import random

COUNTRIES = [
    "USA", "Canada", "Mexico", "Brazil", "Argentina",
    "UK", "France", "Germany", "Italy", "Spain",
    "China", "Japan", "India", "Russia", "Australia"
]
PORT = 2000


def handle_client(conn, addr):
    try:
        conn.sendall(b"Welcome to the Countries Memory Game!\n")
        conn.sendall(b"Match the countries to win.\n")
        shuffled = COUNTRIES[:]
        random.shuffle(shuffled)
        for i, country in enumerate(shuffled):
            conn.sendall(f"{i+1}. {country}\n".encode())
        conn.sendall(b"Type the number of the matching countries (e.g., 1 2):\n")
        data = conn.recv(1024)
        conn.sendall(b"You entered: " + data + b"\n")
        # Add game logic here
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", PORT))
        s.listen()
        print(f"Python server running on port {PORT}")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    main()
