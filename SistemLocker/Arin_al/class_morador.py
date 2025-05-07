class Sindico:
    def __init__(self, nome, apartamento, senha = "0000"):
        self.__nome = nome
        self.__apartamento = apartamento
        if type(self) is Sindico:
            self.__senha_universal = senha
    # def get_apt(self):
    #     return self.__apartamento

class Morador(Sindico):
    def __init__(self, nome, apartamento, senha_geral):
        super().__init__(nome, apartamento)
        self.__senha_geral = senha_geral

    # def get_apartamento(self):
    #     return self._Sindico__apartamento
    #     # return self.get_apt()

    @property
    def apt(self):
        return self._Sindico__apartamento

    @apt.setter
    def apt(self, apt):
        self._Sindico__apartamento = apt


m = Morador("Juca", "103", "1919")
m.apt = "203"
print(m.apt)


# class Morador():
#     def __init__(self, nome, apartamento, senha_geral):
#         self.nome = nome
#         self.apartamento = apartamento
#         self.senha_geral = senha_geral
#
#     def get_apartamento(self):
#         return self.apartamento
#
#
