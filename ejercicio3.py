class Vehiculo:
    def __init__(self):
        print("Soy un Vehiculo")
    
    def Motor(self):
        print("Motor encendido")
      
      
class VehiculoTerrestre(Vehiculo):
    def __init__(self):
        Vehiculo.__init__(self)
        print("Soy un vehiculo Terrestre")
    
    def funcion(self):
        print("Yo ando")


class VehiculoAereo(Vehiculo):
    def __init__(self):
        Vehiculo.__init__(self)
        print("Soy un vehiculo Aereo")
        
    def funcion(self):
        print("Yo vuelo")



class Avion(VehiculoAereo):
    def __init__(self):
        VehiculoAereo.__init__(self)
        print("Soy un Avion")
        
        
class Helicoptero(VehiculoAereo):
    def __init__(self):
        VehiculoAereo.__init__(self)
        print("Soy un Helicoptero")



class Dron(VehiculoAereo):
    def __init__(self):
        VehiculoAereo.__init__(self)
        print("Soy un Dron")


class Auto(VehiculoTerrestre):
    def __init__(self):
        VehiculoTerrestre.__init__(self)
        print("Soy un Auto")


class Motocicleta(VehiculoTerrestre):
    def __init__(self):
        VehiculoTerrestre.__init__(self)
        print("Soy una Motocicleta")


class Bicicleta(VehiculoTerrestre):
    def __init__(self):
        VehiculoTerrestre.__init__(self)
        print("Soy una Bicicleta")
    
    
def main():
    h = Helicoptero()
    h.Motor()
    h.funcion()
#ejemplo cn la clase Helicoptero. Tiene metodos de la clase de VehiculoAereo y as u vez Metodos de la clase Vehiculo
#Esto debido a que la clase Vehiculo aereo tambien heredo los metodos de la clase vehiculo, y su subclase(Helicopter) por
#tanto tambien lo heredo
    
main()