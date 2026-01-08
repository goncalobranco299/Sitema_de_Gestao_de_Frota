import tkinter as tk
from frota import Frota
from veiculo import Veiculo

class Interface:
    def __init__(self, frota):
        self.frota = frota
        self.window = tk.Tk()
        self.window.title("Gestão de Frotas")

        # Adicionar veículo
        self.marca_label = tk.Label(self.window, text="Marca")
        self.marca_label.pack()
        self.marca_entry = tk.Entry(self.window)
        self.marca_entry.pack()

        self.preco_label = tk.Label(self.window, text="Preço")
        self.preco_label.pack()
        self.preco_entry = tk.Entry(self.window)
        self.preco_entry.pack()

        self.add_button = tk.Button(self.window, text="Adicionar Veículo", command=self.adicionar_veiculo)
        self.add_button.pack()

        # Exportar inventário
        self.export_button = tk.Button(self.window, text="Exportar Inventário", command=self.exportar_inventario)
        self.export_button.pack()

    def adicionar_veiculo(self):
        marca = self.marca_entry.get()
        preco = float(self.preco_entry.get())
        veiculo = Veiculo(marca, preco)
        self.frota.add_vehicle(veiculo)

    def exportar_inventario(self):
        from exportacao import exportar_inventario
        exportar_inventario(self.frota)

    def run(self):
        self.window.mainloop()
