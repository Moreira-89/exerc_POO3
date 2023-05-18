class Participante:
    def __init__(self, perfil):
        self.perfil = perfil

    def responder_perguntas(self, perguntas):
        for pergunta in perguntas:
            resposta = input(pergunta.texto)
            self.perfil[pergunta.texto] = resposta

    def calcular_match(self, outro_participante):
        respostas_iguais = 0
        for pergunta, resposta in self.perfil.items():
            if resposta == outro_participante.perfil.get(pergunta):
                respostas_iguais += 1
        return respostas_iguais
