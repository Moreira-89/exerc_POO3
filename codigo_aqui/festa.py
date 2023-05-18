class Festa:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.perguntas = []

    def adicionar_participante(self, participante):
        self.participante = participante

    def cadastrar_pergunta(self, pergunta):
        self.perguntas.append(pergunta)

    def encontrar_match(self, participante):
        melhor_match = None
        max_respostas_iguais = -1

        for p in self.participantes:
            if p != participante:
                respostas_iguais = participante.calcular_match(p)
                if respostas_iguais > max_respostas_iguais:
                    max_respostas_iguais = respostas_iguais
                    melhor_match = p

        return melhor_match
