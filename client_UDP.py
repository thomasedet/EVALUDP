# -*- coding: utf-8 -*-

import socket


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.settimeout(1.0)

sock.connect(???)
sock.send(???)


trameReponse, addr = sock.recvfrom(1024)

print "Réception de la trame de réponse", trameReponse.encode("hex")

code = ???

print code

