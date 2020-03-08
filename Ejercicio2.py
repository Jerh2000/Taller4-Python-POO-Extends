class Estudiante:
    def __init__(self, id, tipo_id, nombres, programa, semestre, institucion):
        """Constructor de clase Empleado"""
        self.__id = id
        self.__tipo_id = tipo_id
        self.__nombres = nombres
        self.__programa = programa
        self.__semestre = semestre
        self.__institucion = institucion

    def __init__(self):
        pass

    # métodos get

    def getid(self):
        return self.__id

    def gettipo_id(self):
        return self.__tipo_id

    def getNombres(self):
        return self.__nombres

    def getPrograma(self):
        return self.__programa

    def getSemestre(self):
        return self.__semestre

    def getInstitucion(self):
        return self.__institucion

    # métodos set

    def setid(self, id):
        self.__id = id

    def setTipo_id(self, tipo_id):
        self.__tipo_id = tipo_id

    def setNombres(self, nombres):
        self.__nombres = nombres

    def setPrograma(self, programa):
        self.__programa = programa

    def setSemestre(self, semestre):
        self.__semestre = semestre

    def setInstitucion(self, institucion):
        self.__institucion = institucion


class Pricipal(Estudiante):
    pass


def main():

    p1 = Pricipal()
    print("hola!!! \n por favor, digite los siguientes datos")
    id = int(input("digite su id: "))
    tipo_id = input("digite el tipo de id: ")
    nombres = input("digite su nombre: ")
    programa = input("digite su programa academico: ")
    semestre = input("digite su semestre: ")
    instituto = input("digite su instituto: ")

    p1.setid(id)
    p1.setTipo_id(tipo_id)
    p1.setPrograma(programa)
    p1.setNombres(nombres)
    p1.setSemestre(semestre)
    p1.setInstitucion(instituto)
    print("\n****************************************\n Informacion del estudiante")
    print(f"el id es: {p1.getid()} \n el tipo de id es: {p1.gettipo_id()} \n el nombre es: {p1.getNombres()} \n el programa es: {p1.getPrograma()} \n el semestre es: {p1.getSemestre()} \n el instituto es: {p1.getInstitucion()}")


main()
