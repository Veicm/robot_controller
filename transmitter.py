import socket

class Transmitter:

    def __init__(self, port:int, target:str=None):
        self.HOST = target
        self.PORT = port

    def send_massage(self, massage, target=None):
        if target is None:
            target = self.HOST
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            connection.connect((target, self.PORT))
            connection.sendall(massage.encode())
        finally:
            connection.close()
        print(f"Massage: [{massage}] has been sended to [{target}].")

class TestTransmitter:
    def __init__(self, target=None, port=None):
        self.target = target


    def send_massage(self, massage, target=None):
        if target == None:
            target = self.target
        print(f"Massage: [{massage}] has NOT been sended to [{target}].")


if __name__ == "__main__":
    try:
        t = Transmitter(target="127.0.0.1", port=1234)
    except Exception as e:
        t = TestTransmitter(None, None)
    t.send_massage("debug")
