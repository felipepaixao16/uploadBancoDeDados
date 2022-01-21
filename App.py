from Usuarios import Usuarios
from tkinter import *

class Application:

    def __init__(self):

        self.janela_principal = Tk()

        self.fonte = ("Verdana", "8")
        
        self.container1 = Frame(self.janela_principal, pady = 10)
        self.container1.pack()

        self.container2 = Frame(self.janela_principal, padx = 20, pady = 5)
        self.container2.pack()

        self.container3 = Frame(self.janela_principal, padx = 20, pady = 5)
        self.container3.pack()

        self.container4 = Frame(self.janela_principal, padx = 20, pady = 5)
        self.container4.pack()

        self.container5 = Frame(self.janela_principal, padx = 20, pady = 5)
        self.container5.pack()

        self.container6 = Frame(self.janela_principal, padx = 20, pady = 5)
        self.container6.pack()

        self.container7 = Frame(self.janela_principal, padx = 20, pady = 5)
        self.container7.pack()

        self.container8 = Frame(self.janela_principal, padx = 20, pady = 5)
        self.container8.pack()

        self.container9 = Frame(self.janela_principal, pady = 15)
        self.container9.pack()

        self.titulo = Label(self.container1, text = "Informe os dados: ")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.labelId = Label(self.container2, text="Id do usuário", font=self.fonte, width = 10)
        self.labelId.pack(side = LEFT)
        
        self.caixaId = Entry(self.container2, width = 10, font=self.fonte)
        self.caixaId.pack(side = LEFT)

        self.buscar = Button(self.container2, text="Buscar", font=self.fonte, width = 10, command = self.buscarUsuario)
        self.buscar.pack(side = RIGHT)

        self.labelNome = Label(self.container3, text="Nome", font=self.fonte, width = 10)
        self.labelNome.pack(side = LEFT)

        self.caixaNome = Entry(self.container3, width = 25, font=self.fonte)
        self.caixaNome.pack(side = LEFT)

        self.labelTelefone = Label(self.container4, width = 10, text="Telefone", font=self.fonte)
        self.labelTelefone.pack(side = LEFT)

        self.caixaTelefone = Entry(self.container4, width = 25, font=self.fonte)
        self.caixaTelefone.pack(side = LEFT)

        self.labelEmail = Label(self.container5, width = 10, text="Email", font=self.fonte)
        self.labelEmail.pack(side = LEFT)

        self.caixaEmail = Entry(self.container5, width = 25, font=self.fonte)
        self.caixaEmail.pack(side = LEFT)

        self.labelUsuario = Label(self.container6, width = 10, text="Usuário", font=self.fonte)
        self.labelUsuario.pack(side = LEFT)

        self.caixaUsuario = Entry(self.container6, width = 25, font=self.fonte)
        self.caixaUsuario.pack(side = LEFT)

        self.labelSenha = Label(self.container7, width = 10, text="Senha:", font=self.fonte)
        self.labelSenha.pack(side = LEFT)

        self.caixaSenha = Entry(self.container7, width = 25, font=self.fonte, show = "*")
        self.caixaSenha.pack(side = LEFT)

        self.insert = Button(self.container8, width = 12, text="Inserir", command = self.inserirUsuario, font=self.fonte)
        self.insert.pack(side = LEFT)

        self.update = Button(self.container8, width = 12, text="Alterar", command = self.alterarUsuario, font=self.fonte)
        self.update.pack(side = LEFT)

        self.delete = Button(self.container8, width = 12, text="Excluir", command = self.excluirUsuario, font=self.fonte)
        self.delete.pack(side = LEFT)

        self.mensagem = Label(self.container9, text="")
        self.mensagem["font"] = ("Verdana", "9", "italic")
        self.mensagem.pack()

        mainloop()

    def inserirUsuario(self):
        user = Usuarios()

        user.nome = self.caixaNome.get()
        user.telefone = self.caixaTelefone.get()
        user.email = self.caixaEmail.get()
        user.usuario = self.caixaUsuario.get()
        user.senha = self.caixaSenha.get()

        self.mensagem["text"] = user.insertUser()

        self.caixaId.delete(0, END)
        self.caixaNome.delete(0, END)
        self.caixaTelefone.delete(0, END)
        self.caixaEmail.delete(0, END)
        self.caixaUsuario.delete(0, END)
        self.caixaSenha.delete(0, END)

    def alterarUsuario(self):
        user = Usuarios()

        user.idusuario = self.caixaId.get()
        user.nome = self.caixaNome.get()
        user.telefone = self.caixaTelefone.get()
        user.email = self.caixaEmail.get()
        user.usuario = self.caixaUsuario.get()
        user.senha = self.caixaSenha.get()

        self.mensagem["text"] = user.updateUser()

        self.caixaId.delete(0, END)
        self.caixaNome.delete(0, END)
        self.caixaTelefone.delete(0, END)
        self.caixaEmail.delete(0, END)
        self.caixaUsuario.delete(0, END)
        self.caixaSenha.delete(0, END)

    def excluirUsuario(self):
        user = Usuarios()

        user.idusuario = self.caixaId.get()

        self.mensagem["text"] = user.deleteUser()

        self.caixaId.delete(0, END)
        self.caixaNome.delete(0, END)
        self.caixaTelefone.delete(0, END)
        self.caixaEmail.delete(0, END)
        self.caixaUsuario.delete(0, END)
        self.caixaSenha.delete(0, END)

    def buscarUsuario(self):
        user = Usuarios()

        idusuario = self.caixaId.get()

        self.mensagem["text"] = user.selectUser(idusuario)

        self.caixaId.delete(0, END)
        self.caixaId.insert(INSERT, user.idusuario)
        
        self.caixaNome.delete(0, END)
        self.caixaNome.insert(INSERT, user.nome)
        
        self.caixaTelefone.delete(0, END)
        self.caixaTelefone.insert(INSERT, user.telefone)
        
        self.caixaEmail.delete(0, END)
        self.caixaEmail.insert(INSERT, user.email)
        
        self.caixaUsuario.delete(0, END)
        self.caixaUsuario.insert(INSERT, user.usuario)
        
        self.caixaSenha.delete(0, END)
        self.caixaSenha.insert(INSERT, user.senha)

minhaInterface = Application()
