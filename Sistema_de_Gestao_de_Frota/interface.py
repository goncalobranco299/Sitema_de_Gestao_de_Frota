import tkinter as tk
from tkinter import messagebox
from veiculo import Veiculo, CarroEletrico

CORES = {
    'bg': '#1e1e1e',       # Fundo preto/cinza muito escuro
    'fg': '#ffffff',       # Texto branco
    'box_bg': '#2d2d2d',   # Fundo da caixa de controle
    'entry_bg': '#404040', # Fundo dos inputs
    'entry_fg': '#ffffff', # Texto dos inputs
    'btn_add': '#4CAF50',  # Verde
    'btn_edit': '#2196F3', # Azul
    'btn_del': '#f44336',  # Vermelho
    'btn_exp': '#FF9800'   # Laranja
}

class Interface:
    def __init__(self, frota):
        self.frota = frota
        self.veiculo_selecionado = None # Guarda o objeto que está a ser editado

        self.root = tk.Tk()
        self.root.title("SGF")
        self.root.geometry("600x650")
        self.root.configure(bg=CORES['bg']) # Aplica fundo preto na janela

        # Título Principal
        tk.Label(self.root, text="SISTEMA DE GESTÃO DE FROTAS", 
                 font=('Arial', 16, 'bold'), bg=CORES['bg'], fg=CORES['fg']).pack(pady=15)

        # ======================================================
        # BOX DE CONTROLO (ADICIONAR / EDITAR / DELETAR / DESCONTO)
        # ======================================================
        self.box_frame = tk.Frame(self.root, bg=CORES['box_bg'], bd=2, relief="ridge")
        self.box_frame.pack(fill='x', padx=20, pady=10)

        tk.Label(self.box_frame, text="Painel de Controlo", 
                 bg=CORES['box_bg'], fg="#aaaaaa", font=('Arial', 10)).pack(pady=5)

        # Grid para Inputs dentro da Box
        input_frame = tk.Frame(self.box_frame, bg=CORES['box_bg'])
        input_frame.pack(pady=10)

        # Inputs (Label + Entry)
        self.entry_marca = self.criar_input(input_frame, "Marca:", 0)
        self.entry_preco = self.criar_input(input_frame, "Preço (€):", 1)
        self.entry_bateria = self.criar_input(input_frame, "Bateria (kWh):", 2)

        # Botões de Ação (CRUD)
        btn_frame = tk.Frame(self.box_frame, bg=CORES['box_bg'])
        btn_frame.pack(pady=15)

        self.btn_criar = tk.Button(btn_frame, text="✚ Adicionar", bg=CORES['btn_add'], fg='white', 
                                   command=self.acao_adicionar, width=12)
        self.btn_criar.grid(row=0, column=0, padx=5)

        self.btn_editar = tk.Button(btn_frame, text="✎ Atualizar", bg=CORES['btn_edit'], fg='white', 
                                    command=self.acao_editar, state=tk.DISABLED, width=12)
        self.btn_editar.grid(row=0, column=1, padx=5)

        self.btn_apagar = tk.Button(btn_frame, text="✖ Apagar", bg=CORES['btn_del'], fg='white', 
                                    command=self.acao_apagar, state=tk.DISABLED, width=12)
        self.btn_apagar.grid(row=0, column=2, padx=5)

        self.btm_desconto = tk.Button(btn_frame)

        # ======================================================
        # LISTA E FILTRO
        # ======================================================
        
        # Campo de Pesquisa
        frame_filtro = tk.Frame(self.root, bg=CORES['bg'])
        frame_filtro.pack(fill='x', padx=20, pady=(10, 0))
        tk.Label(frame_filtro, text="🔍 Pesquisar:", bg=CORES['bg'], fg=CORES['fg']).pack(side=tk.LEFT)
        
        self.entry_filtro = tk.Entry(frame_filtro, bg=CORES['entry_bg'], fg=CORES['entry_fg'], insertbackground='white')
        self.entry_filtro.pack(side=tk.LEFT, fill='x', expand=True, padx=10)
        self.entry_filtro.bind('<KeyRelease>', self.ao_filtrar)

        # Listbox Customizada
        self.listbox = tk.Listbox(self.root, bg=CORES['entry_bg'], fg=CORES['entry_fg'], 
                                  height=12, selectbackground=CORES['btn_edit'])
        self.listbox.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Evento: Quando clica num item da lista
        self.listbox.bind('<<ListboxSelect>>', self.selecionar_veiculo)

        # Botão Extra (Exportar)
        tk.Button(self.root, text="Exportar Dados", bg=CORES['btn_exp'], fg='white',
                  command=self.btn_exportar).pack(pady=10, fill='x', padx=50)

        self.atualizar_lista()

    # --- MÉTODOS AUXILIARES ---
    def criar_input(self, parent, texto, row):
        tk.Label(parent, text=texto, bg=CORES['box_bg'], fg=CORES['fg']).grid(row=row, column=0, padx=5, sticky='e')
        entry = tk.Entry(parent, bg=CORES['entry_bg'], fg=CORES['entry_fg'], insertbackground='white')
        entry.grid(row=row, column=1, padx=5, pady=2)
        return entry

    def limpar_formulario(self):
        self.entry_marca.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)
        self.entry_bateria.delete(0, tk.END)
        # Reseta o estado
        self.veiculo_selecionado = None
        self.btn_editar.config(state=tk.DISABLED)
        self.btn_apagar.config(state=tk.DISABLED)
        self.btn_criar.config(state=tk.NORMAL)

    def selecionar_veiculo(self, event):
        # Pega a seleção
        selection = self.listbox.curselection()
        if not selection:
            return

        # Identifica o objeto real (lógica simples baseada no índice da lista atual)
        # Nota: Em sistemas complexos, usaríamos o ID oculto, mas aqui usamos o índice
        index = selection[0]
        
        # Se estivermos filtrados, precisamos ter cuidado, mas vamos assumir lista completa por agora
        # ou pegar da lista que está a ser exibida.
        # Para simplificar a aula, vamos pegar da lista atual de exibição:
        texto_linha = self.listbox.get(index)
        id_veiculo = int(texto_linha.split("ID: ")[1].split(" |")[0])
        
        # Busca na frota pelo ID
        veiculo = next((v for v in self.frota.vehicles if v.id == id_veiculo), None)

        if veiculo:
            self.veiculo_selecionado = veiculo
            
            # Preenche o formulário
            self.entry_marca.delete(0, tk.END)
            self.entry_marca.insert(0, veiculo.marca)
            
            self.entry_preco.delete(0, tk.END)
            self.entry_preco.insert(0, str(veiculo.preco))
            
            self.entry_bateria.delete(0, tk.END)
            if hasattr(veiculo, 'capacidade_bateria'):
                self.entry_bateria.insert(0, str(veiculo.capacidade_bateria))

            # Habilita botões de edição/exclusão
            self.btn_criar.config(state=tk.DISABLED) # Desativa criar para evitar duplicados acidentais
            self.btn_editar.config(state=tk.NORMAL)
            self.btn_apagar.config(state=tk.NORMAL)

    # --- AÇÕES CRUD ---
    def acao_adicionar(self):
        try:
            marca = self.entry_marca.get()
            preco = float(self.entry_preco.get())
            bateria = self.entry_bateria.get()

            if bateria.strip():
                novo_v = CarroEletrico(marca, preco, int(bateria))
            else:
                novo_v = Veiculo(marca, preco)

            self.frota.add_vehicle(novo_v)
            self.atualizar_lista()
            self.limpar_formulario()
            messagebox.showinfo("Sucesso", "Veículo adicionado!")
        except ValueError:
            messagebox.showerror("Erro", "Verifique os valores numéricos.")

    def acao_editar(self):
        if not self.veiculo_selecionado: return
        
        try:
            self.frota.atualizar_veiculo(
                self.veiculo_selecionado,
                self.entry_marca.get(),
                self.entry_preco.get(),
                self.entry_bateria.get()
            )
            self.atualizar_lista()
            self.limpar_formulario()
            messagebox.showinfo("Sucesso", "Veículo atualizado!")
        except ValueError:
            messagebox.showerror("Erro", "Valores inválidos.")

    def acao_apagar(self):
        if not self.veiculo_selecionado: return
        
        if messagebox.askyesno("Confirmar", f"Tem a certeza que quer apagar o {self.veiculo_selecionado.marca}?"):
            self.frota.remove_vehicle(self.veiculo_selecionado)
            self.atualizar_lista()
            self.limpar_formulario()

    def ao_filtrar(self, event):
        termo = self.entry_filtro.get()
        v_filtrados = self.frota.filtrar_veiculos(termo)
        self.atualizar_lista(v_filtrados)

    def atualizar_lista(self, dados=None):
        self.listbox.delete(0, tk.END)
        lista = dados if dados is not None else self.frota.vehicles
        for v in lista:
            self.listbox.insert(tk.END, str(v))

    def btn_exportar(self):
        from exportacao import exportar_inventario
        if exportar_inventario(self.frota):
            messagebox.showinfo("Exportar", "Ficheiro guardado!")

    def run(self):
        self.root.mainloop()