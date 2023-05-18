from festa import Festa
from participante import Participante
from pergunta import Pergunta

# Criando festa
festa = Festa("Festa de Aniversário", "Venha comemorar!")

# Criando perguntas
pergunta1 = Pergunta("Gosta de chocolate? ")
pergunta2 = Pergunta("Gosta de dançar? ")
pergunta3 = Pergunta("Gosta de animais? ")

# Cadastrando perguntas na festa
festa.cadastrar_pergunta(pergunta1)
festa.cadastrar_pergunta(pergunta2)
festa.cadastrar_pergunta(pergunta3)

# Criando participantes
participante1 = Participante({})
participante2 = Participante({})
participante3 = Participante({})

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
print("O match de", participante1, "é", match)
