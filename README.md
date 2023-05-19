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
