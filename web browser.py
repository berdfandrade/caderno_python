import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n' .enconde()
mysock.send(cmd)

while True:
    data = mysock.rec(512)
    if (len(data)) < 1:
        break
    print(data.decoded())
mysock.close()
