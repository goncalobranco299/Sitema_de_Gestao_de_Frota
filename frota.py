from decoradores import log_operacao

class Frota:
    def __init__(self):
        self.vehicles = []
        self.proximo_id = 1  # Contador para gerar IDs automáticos

    @log_operacao
    def add_vehicle(self, veiculo):
        # Atribui o ID ao veículo antes de adicionar à lista
        veiculo.id = self.proximo_id
        self.vehicles.append(veiculo)
        self.proximo_id += 1 # Incrementa para o próximo veículo

    @log_operacao
    def remove_vehicle(self, veiculo):
        self.vehicles.remove(veiculo)

    def pesquisar_por_marca(self, marca):
        return [v for v in self.vehicles if v.marca.lower() == marca.lower()]

    def aplicar_desconto_frota(self, percentagem_desconto):
        taxa = (100 - percentagem_desconto) / 100
        # Uso de Lambda e Map conforme os requisitos
        precos_atualizados = list(map(lambda v: v.preco * taxa, self.vehicles))
        
        for i, novo_preco in enumerate(precos_atualizados):
            self.vehicles[i].preco = novo_preco