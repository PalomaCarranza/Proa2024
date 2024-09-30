class Personaje:
    # Atributo de clase
    estado = True # Vivo
    vida = 100
    # Constructor / Atributo de instancia
    def __init__(self, nombre, altura, velocidad, resistencia, fuerza):
        self.nombre = nombre
        self.altura = altura
        self.velocidad = velocidad
        self.resistencia = resistencia
        self.fuerza = fuerza
        self.estado = Personaje.estado
        self.vida = Personaje.vida

    
    def atacar(self, otro_personaje):
        if self.estado:
            danio = self.fuerza - (otro_personaje.resistencia)
            print(f"{self.nombre} ataca a {otro_personaje.nombre} causando {danio} de daño.")
            otro_personaje.recibir_danno(danio)
        else:
            print(f"{self.nombre} está muerto y no puede atacar.")

    def recibir_danno(self , cantidad):
        if self.estado:
            self.vida = self.vida - cantidad
            print(f"{self.nombre} recibe {cantidad} de daño. Le queda {self.vida} de vida.")
            if self.vida <= 0: # Si vida es igual o menor a 0 vida es igual a 0 para que no nos de números negativos
                self.vida = 0
                print(f"{self.nombre} ha muerto.")
        else:
            print(f"{self.nombre} ya está muerto.")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Estado: {self.estado}")
        print(f"Vida: {self.vida}")
        print(f"Resistencia: {self.resistencia}")
        print(f"Fuerza: {self.fuerza}")