from veiculo import Veiculo

class Frota:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, veiculo):
        self.vehicles.append(veiculo)

    def remove_vehicle(self, veiculo):
        self.vehicles.remove(veiculo)

    def pesquisar_veiculos(self, marca):
        return [v for v in self.vehicles if v.marca == marca]
