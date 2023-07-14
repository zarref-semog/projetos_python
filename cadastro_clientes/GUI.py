from tkinter import *

class Gui():
    """ Classe da Interface Gráfica
    """
    x_pad = 5
    y_pad = 3
    width_entry = 30
    
    #Criar janela
    window = Tk()
    window.wm_title("PYSQL versão 1.0")

    #Definição das variáveis que recebem os dados innseridos pelo user
    txtNome = StringVar()
    txtSobrenome = StringVar()
    txtEmail = StringVar()
    txtCPF = StringVar()

    #Criação dos objetos que farão parte das janelas
    lblnome = Label(window, text="Nome")
    lblsobrenome = Label(window, text="Sobrenome")
    lblemail = Label(window, text="Email")
    lblcpf = Label(window, text="CPF")
    entNome = Entry(window, textvariable=txtNome , width=width_entry)
    entSobrenome = Entry(window, textvariable=txtSobrenome , width=width_entry)
    entEmail = Entry(window, textvariable=txtEmail , width=width_entry)
    entCPF = Entry(window, textvariable=txtCPF , width=width_entry)
    listClientes = Listbox(window, width=100)
    scrollClientes = Scrollbar(window)
    btnViewAll = Button(window, text="Ver Todos")
    btnBuscar = Button(window, text="Buscar")
    btnInserir = Button(window, text="Inserir")
    btnUpdate = Button(window, text="Atualizar Selecionados")
    btnDel = Button(window, text="Deletar Selecionados")
    btnClose = Button(window, text="Fechar")

    #Criação do grid
    lblnome.grid(row=0, column=0)
    lblsobrenome.grid(row=1, column=0)
    lblemail.grid(row=2, column=0)
    lblcpf.grid(row=3, column=0)
    entNome.grid(row=0, column=1, padx=50, pady=50)
    entSobrenome.grid(row=1, colummn=1)
    entEmail.grid(row=2, column=1)
    entCPF.grid(row=3, column=1)
    listClientes.grid(row=0, column=2, rowspan=10)
    scrollClientes.grid(row=0, column=6, columnspan=2)
    btnViewAll.grid(row=4, column=0, columnspan=2)
    btnBuscar.grid(row=5, column=0, columnspan=2)
    btnInserir.grid(row=6, column=0, columnspan=2)
    btnUpdate.grid(row=7, column=0, columnspan=2)
    btnDel.grid(row=8, column=0, columnspan=2)
    btnClose.grid(row=9, column=0, columnspan=2)

    #União do scrollbar com a Listbox
    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)

    #Adicionar SWAG (aparência) à interface
    for child in window.window_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='WE')
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky="NS")
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')
    
    def run(self):
        Gui.window.mainloop()
