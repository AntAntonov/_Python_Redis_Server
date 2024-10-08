# Uncomment this to pass the first stage
import socket

pong = "+PONG\r\n"
def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    conn, addr = server_socket.accept() # wait for client

    print("Connection =", conn)
    print("address =", addr)


    with conn:
       while conn.accept:
       
            conn.recv(1024)
            conn.send(pong.encode())
    

if __name__ == "__main__":
    main()
