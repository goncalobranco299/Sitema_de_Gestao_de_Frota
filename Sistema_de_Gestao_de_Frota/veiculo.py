class Veiculo:
    def __init__(self, marca, preco, id_veiculo=None):
        self.id = id_veiculo 
        self.marca = marca
        self.preco = float(preco)

    def __str__(self):
        return f"ID: {self.id} | {self.marca.upper()} | Preço: {self.preco:.2f}€"

class CarroEletrico(Veiculo):
    def __init__(self, marca, preco, capacidade_bateria, id_veiculo=None):
        super().__init__(marca, preco, id_veiculo)
        self.capacidade_bateria = capacidade_bateria

    def __str__(self):
        return f"{super().__str__()} | Bateria: {self.capacidade_bateria}kWh"