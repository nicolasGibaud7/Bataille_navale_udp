import socket

def config_reseau():
    # Configuration réseau
    TCP_PORT = 12800

    # Création d'une socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # On écoute le socket
    sock.bind(('', TCP_PORT))

    # On limite le nombre de connexions simultanées à deux
    sock.listen(2)

    co_j1, infos_co_j1 = sock.accept()
    print("J1 connecté d'adresse IP " + infos_co_j1[0])
    co_j1.send(b"Bonjour J1")

    co_j2, infos_co_j2 = sock.accept()
    print("J2 connecté d'adresse IP " + infos_co_j2[0])
    co_j2.send(b"Bonjour J2")

    # Fermeture des différentes connexions
    co_j1.close()
    co_j2.close()
    sock.close()

config_reseau()