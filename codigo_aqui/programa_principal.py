from festa import Festa
from participante import Participante
from pergunta import Pergunta

festa = Festa("Festa de Aniversário", "Venha comemorar!")

# Criando perguntas
pergunta1 = Pergunta("Gosta de chocolate?[S/N]: ")
pergunta2 = Pergunta("Gosta de dançar?[S/N]: ")
pergunta3 = Pergunta("Gosta de animais?[S/N]: ")

# Cadastrando perguntas na festa
festa.cadastrar_pergunta(pergunta1)
festa.cadastrar_pergunta(pergunta2)
festa.cadastrar_pergunta(pergunta3)

# Criando participantes
participante1 = Participante("Participante 1", {})
participante2 = Participante("Participante 2", {})
participante3 = Participante("Participante 3", {})

# Adicionando participantes à festa
festa.adicionar_participante(participante1)
festa.adicionar_participante(participante2)
festa.adicionar_participante(participante3)

# Registrando respostas dos participantes
participante1.responder_perguntas(festa.perguntas)
participante2.responder_perguntas(festa.perguntas)
participante3.responder_perguntas(festa.perguntas)

# Encontrando o match de um participante específico
match = festa.encontrar_match(participante1)
if match:
    print(f"O match de {participante1.nome} é {match.nome}")
else:
    print(f"Não foi encontrado um match para {participante1.nome}")
