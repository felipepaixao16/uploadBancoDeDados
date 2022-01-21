from Banco import Banco

class Usuarios(object):

    def __init__(self):

        self.info = {}
        self.idusuario = 0
        self.nome = ""
        self.telefone = ""
        self.email = ""
        self.usuario = ""
        self.senha = ""

    def insertUser(self):

        banco = Banco()
        try:

            #cursor é um método que serve para manipular o banco de dados
            c = banco.conexao.cursor()

            #o conjunto das aspas serve para caracterizar o valor de cada item na coluna da tabela conforme a ordem abaixo
            c.execute("insert into usuarios(nome, telefone, email, usuario, senha) values('" + self.nome + "', '" +
                      self.telefone + "', '" + self.email + "', '" + self.usuario + "', '" + self.senha + "')")

            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"

        except:

            return "Ocorreu um erro na inserção do usuário"

    def updateUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            #aqui acontece a troca do valor de cada atributo
            c.execute("update usuarios set nome = '" + self.nome +"', telefone = '" + self.telefone +"', email = '" +
                      self.email + "', usuario = '" + self.usuario + "', senha = '" +
                      self.senha + "' where idusuario = " + self.idusuario + " ")
 
            banco.conexao.commit()
            c.close()

            return "Usuario atualizado com sucesso!"

        except:

            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from usuarios where idusuario = " + self.idusuario + " ")

            banco.conexao.commit()
            c.close()

            return "Usuario excluído com sucesso!"

        except:

            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, usuarioid):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from usuarios where idusuario = " + usuarioid + " ")

            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            c.close()

            return "Busca feita com sucesso!"

        except:

            return "Ocorreu um erro na busca do usuário"
