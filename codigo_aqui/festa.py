class Festa:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.perguntas = []
        self.participantes = []

    def cadastrar_pergunta(self, pergunta):
        self.perguntas.append(pergunta)

    def adicionar_participante(self, participante):
        self.participantes.append(participante)

    def encontrar_match(self, participante):
        match = None
        max_pontos = 0

        for p in self.participantes:
            if p != participante:
                pontos = 0
                for pergunta in self.perguntas:
                    resposta_participante = participante.respostas[pergunta]
                    resposta_p = p.respostas[pergunta]

                    if resposta_participante == resposta_p:
                        pontos += 1

                if pontos > max_pontos:
                    max_pontos = pontos
                    match = p

        return match

    def __repr__(self):
        return f"<Festa {self.nome}>"

    def __str__(self):
        return f"Festa {self.nome}: {self.descricao}"
