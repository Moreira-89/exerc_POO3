__Nome__: Lucas M. A. Rodrigues

__Prof. Dr.__ Leandro Luque

## Prática 06: Orientado a Objeto

### O que temos que fazer? 
* Dados os requisitos seguintes, implemente uma solução orientada a objetos (e crie um diagrama de classes) seguindo o modelo discutido em sala de aula.
  * Você deve implementar uma solução que permita que sejam cadastradas festas e participantes. Cada festa tem um nome e uma descrição. Os participantes da festa tem um perfil, com respostas a perguntas do tipo SIM/NÃO. Exemplo: Gosta de chocolate? SIM etc. 
  * O A partir de uma festa e seus participantes, o sistema deve ser capaz de identificar quem é o 'match' de um determinado participante. O match é encontrado a partir do número de respostas iguais para as mesmas perguntas.
  * Em outras palavras, as duas pessoas que responderem mais perguntas de modo igual 'dão match'. Se houver empate, qualquer um dos empatados pode ser selecionado como match. Deve ser possível cadastrar quantas perguntas quiser. Cada participante da festa deve responder a todas as perguntas cadastradas.
***
### Minha Resolução 
Assim como no exercício anterior, nesse exercício eu quis resolvê-lo utilizando a linguagem de programação Python por eu ter mais facilidade com ela. 
A seguir mostrarei parte por parte do meu código: 

__Programa Principal (programa_principal.py)__
```
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
```
__Classe Festa (festa.py)__
```
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
```
__Classe Pergunta (pergunta.py)__
```
class Pergunta:
    def __init__(self, texto):
        self.texto = texto
```
__Classe Participante (participante.py)__
```
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
```
***
### Diagrama de Classe 
A seguir, irei mostrar o meu Diagrama de Classe da minha resolução: 
