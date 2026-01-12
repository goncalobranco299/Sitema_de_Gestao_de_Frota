import tkinter as tk
from tkinter import messagebox
from veiculo import Veiculo, CarroEletrico # Importações verificadas

class Interface:
    def __init__(self, frota):
        self.frota = frota
        self.root = tk.Tk()
        self.root.title("SGF - Sistema de Gestão de Frotas")
        self.root.geometry("400x550")

        tk.Label(self.root, text="Gestão de Veículos", font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Campos de entrada
        tk.Label(self.root, text="Marca:").pack()
        self.entry_marca = tk.Entry(self.root)
        self.entry_marca.pack()

        tk.Label(self.root, text="Preço (€):").pack()
        self.entry_preco = tk.Entry(self.root)
        self.entry_preco.pack()

        tk.Label(self.root, text="Capacidade Bateria (opcional):").pack()
        self.entry_bateria = tk.Entry(self.root)
        self.entry_bateria.pack()

        # Botões
        tk.Button(self.root, text="Adicionar Veículo", bg="#4CAF50", fg="white", 
                  command=self.btn_adicionar).pack(pady=10, fill='x', padx=50)
        
        tk.Button(self.root, text="Aplicar 10% Desconto Geral", bg="#2196F3", fg="white",
                  command=self.btn_desconto).pack(pady=5, fill='x', padx=50)

        tk.Button(self.root, text="Exportar para TXT", bg="#FF9800", fg="white",
                  command=self.btn_exportar).pack(pady=5, fill='x', padx=50)

        # Lista
        self.listbox = tk.Listbox(self.root, height=10)
        self.listbox.pack(pady=10, fill='both', padx=20)
        self.atualizar_lista()

    def atualizar_lista(self):
        self.listbox.delete(0, tk.END)
        for v in self.frota.vehicles:
            self.listbox.insert(tk.END, str(v))

    def btn_adicionar(self):
        try:
            marca = self.entry_marca.get()
            preco = float(self.entry_preco.get())
            bateria = self.entry_bateria.get()

            # Lógica para decidir o tipo de objeto
            if bateria.strip():
                novo_v = CarroEletrico(marca, preco, int(bateria))
            else:
                novo_v = Veiculo(marca, preco)

            self.frota.add_vehicle(novo_v)
            self.atualizar_lista()
            messagebox.showinfo("Sucesso", f"{marca} adicionado com ID {novo_v.id}!")
            
            # Limpar campos
            self.entry_marca.delete(0, tk.END)
            self.entry_preco.delete(0, tk.END)
            self.entry_bateria.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Erro", "Insira valores numéricos válidos para preço/bateria.")

    def btn_desconto(self):
        self.frota.aplicar_desconto_frota(10)
        self.atualizar_lista()
        messagebox.showinfo("Promoção", "Desconto aplicado!")

    def btn_exportar(self):
        from exportacao import exportar_inventario
        if exportar_inventario(self.frota):
            messagebox.showinfo("Exportar", "Ficheiro 'inventario.txt' gerado!")

    def run(self):
        self.root.mainloop()