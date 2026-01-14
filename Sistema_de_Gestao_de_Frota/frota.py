from decoradores import log_operacao

class Frota:
    def __init__(self):
        self.vehicles = []
        self.proximo_id = 1

    @log_operacao
    def add_vehicle(self, veiculo):
        veiculo.id = self.proximo_id
        self.vehicles.append(veiculo)
        self.proximo_id += 1

    @log_operacao
    def remove_vehicle(self, veiculo):
        if veiculo in self.vehicles:
            self.vehicles.remove(veiculo)

    # --- NOVA OTIMIZAÇÃO: ATUALIZAR DADOS (EDITAR) ---
    @log_operacao
    def atualizar_veiculo(self, veiculo_alvo, nova_marca, novo_preco, nova_bateria=None):
        """
        Atualiza os atributos de um veículo existente.
        Otimização: Altera o objeto diretamente na memória.
        """
        veiculo_alvo.marca = nova_marca
        veiculo_alvo.preco = float(novo_preco)
        
        # Verifica se é elétrico para atualizar bateria
        if hasattr(veiculo_alvo, 'capacidade_bateria') and nova_bateria:
            veiculo_alvo.capacidade_bateria = int(nova_bateria)

    def filtrar_veiculos(self, termo_pesquisa=None):
        if not termo_pesquisa:
            return self.vehicles
        termo = termo_pesquisa.lower()
        return [
            v for v in self.vehicles 
            if termo in v.marca.lower() or termo == str(v.id)
        ]

    def aplicar_desconto_frota(self, percentagem_desconto):
        taxa = (100 - percentagem_desconto) / 100
        for v in self.vehicles:
            v.preco *= taxa