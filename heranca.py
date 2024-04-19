class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def frear(self):
        print(f"A {self.marca} já freio")
    def acelerar(self):
        print(f"A {self.marca} está acelerando")

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def abrir_porta(self):
        print(f"O {self.modelo} está abrindo a porta")

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def empinar(self):
        print(f"A {self.modelo} está empinando")

veiculos_geral = Veiculo("BMW", "depende do veículo")
carro1 = Carro("Fiat", "Pálio", "Azul")
moto1 = Moto("Yamaha", "Factor", "125")

veiculos_geral.frear()
veiculos_geral.acelerar()
carro1.abrir_porta()
moto1.empinar()