class Veiculo:
    def __init__(self, marca, preco):
        self.marca = marca
        self.preco = preco

    def __str__(self):
        return f"{self.marca} - {self.preco}€"

class CarroEletrico(Veiculo):
    def __init__(self, marca, preco, capacidade_bateria):
        super().__init__(marca, preco)
        self.capacidade_bateria = capacidade_bateria  # em kWh

    def calcular_autonomia(self):
        return self.capacidade_bateria * 5  # Suposição: 1 kWh = 5 km de autonomia

    def __str__(self):
        return f"{super().__str__()} - Bateria: {self.capacidade_bateria} kWh"
