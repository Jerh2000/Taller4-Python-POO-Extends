class Empleado:
    def __init__(self, id, tipo_id, cargo, sueldo, email, telefono, empresa):
        """Constructor de clase Empleado"""
        self.__id = id
        self.__tipo_id = tipo_id
        self.__cargo = cargo
        self.__sueldo = sueldo
        self.__email = email
        self.__telefono = telefono
        self.__empresa = empresa

    def __init__(self):
        pass

    # métodos get

    def getid(self):
        return self.__id

    def gettipo_id(self):
        return self.__tipo_id

    def getcargo(self):
        return self.__cargo

    def getSueldo(self):
        return self.__sueldo

    def getEmail(self):
        return self.__email

    def getTelefono(self):
        return self.__telefono

    def getEmpresa(self):
        return self.__empresa

    # métodos set

    def setid(self, id):
        self.__id = id

    def setTipo_id(self, tipo_id):
        self.__tipo_id = tipo_id

    def setcargo(self, cargo):
        self.__cargo = cargo

    def setSueldo(self, sueldo):
        self.__sueldo = sueldo

    def setEmail(self, email):
        self.__email = email

    def setTelefono(self, telefono):
        self.__telefono = telefono

    def setEmpresa(self, empresa):
        self.__empresa = empresa


class Pricipal(Empleado):
    pass


def main():


    p1 = Pricipal()
    print("hola!!! \n por favor, digite los siguientes datos")
    id = int(input("digite su id: "))
    tipo_id = input("digite el tipo de id: ")
    cargo = input("digite su cargo: ")
    sueldo = input("digite su sueldo")
    email = input("digite su email: ")
    telefono = input("digite su telefono: ")
    empresa = input("digite su empresa: ")

    p1.setid(id)
    p1.setTipo_id(tipo_id)
    p1.setcargo(cargo)
    p1.setSueldo(sueldo)
    p1.setEmail(email)
    p1.setTelefono(telefono)
    p1.setEmpresa(empresa)

    print(f"el id es: {p1.getid()} \n el tipo de id es: {p1.gettipo_id()} \n el cargo es: {p1.getcargo()} \n el sueldo es: {p1.getSueldo()} \n el email es: {p1.getEmail()} \n el telefono es: {p1.getTelefono()} \n la empresa es: {p1.getEmpresa()}")
    
main()
