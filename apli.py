# Definir función para validar el login y la clave
def validar_credenciales(login, clave):
    with open("login.txt", "r") as login_file, open("clave.txt", "r") as clave_file:
        logins = login_file.readlines()
        claves = clave_file.readlines()
        if login + "\n" in logins and clave + "\n" in claves:
            return True
        else:
            return False