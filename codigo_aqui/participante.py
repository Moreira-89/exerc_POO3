class Participante:
    def __init__(self, nome, respostas):
        self.nome = nome
        self.respostas = respostas

    def responder_perguntas(self, perguntas):
        for pergunta in perguntas:
            resposta = input(pergunta.texto + " [S/N]: ")
            if resposta.upper() == "S":
                self.respostas[pergunta] = True
            else:
                self.respostas[pergunta] = False

    def verificar_match(self, perfil):
        for pergunta, resposta in self.respostas.items():
            if resposta != perfil[pergunta]:
                return False
        return True

    def __repr__(self):
        return f"Participante({self.nome})"

    def __str__(self):
        return f"Participante {self.nome}"
