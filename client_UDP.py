#!/usr/bin/env python                ####on est en langage python
# _*_ coding: utf-8 _*_             ###on peut utiliser des signes et lettre du clavier fr

import socket #on importe la librairie socket


UDP_IP="192.168.0.202" #ip du serveur 
UDP_PORT=5005 #port utilisé
MESSAGE = "cinema" #message qui sera envoyé
sock = socket.socket(socket.AF_INET, # Internet + définition de la socket AF_inet = internet et DGRAM = utilisation de UDP
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP,UDP_PORT)) #envoie du message au port et a l'adresse suivante définit précédemment 
print "message =", MESSAGE #commande non obligatoire, juste pour savoir si le message envoyé est bien celui défini






trame_reponse,addr = sock.recvfrom (1024) #ligne de décodage des trames. 1024 correspond
print "Réception de la trame de réponse", trame_reponse.encode("hex")#Elle sert à voir si le message est bien envoyé dans sa totalité
code = (int)(ord(trame_reponse[3])<<24) #le code correspond à un entier et est la 4éme case du tableau décalé de 24 bits
code = code +(ord(trame_reponse[2])<<16)#le code correspond à un entier et est la 3éme case du tableau décalé de 16 bits + la valeur de la variable code qui précède
code = code +(ord(trame_reponse[1])<<8)#le code correspond à un entier et est la 2éme case du tableau décalé de 8 bits + la valeur de la variable code qui précède
code = code + ord(trame_reponse[0])#le code correspond à un entier et est la 1éme case + la valeur de la variable code qui précède
print "le code est:" , code #afficher le code est + la variable code


###code tester valide 3.
