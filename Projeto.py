'''
Jogo para prender ingles:
Acertar a tradução dando 4 opções
Se acerta ganha pontos e se perder, perde ponto
Com 10 acertos ganha 1 vida
começa o jogo com 5 vidas
Aumular 30 acertos para passar de nível
 os nivel são: facil, medio e dificil.
'''

import random
import matplotlib.pyplot as plt

# Dicionário com palavras em inglês e suas traduções em português
palavras_facil = {
    "Good morning.": "Bom dia.",
    "What a nice day.": "Que dia bonito.",
    "What time is it?": "Que horas são?",
    "Are you awake?": "Você está acordado?",
    "What day is it today?": "Que dia é hoje?",
    "I’m feeling sick today.": "Eu estou me sentindo doente hoje.",
    "I’m running a little late.": "Eu estou um pouco atrasado.",
    "What’s for breakfast today?": "O que tem para o café da manhã hoje?",
    "I didn’t sleep very well, I had a bad dream.": "Eu não dormi muito bem, eu tive um pesadelo.",
    "How was school today?": "Como foi a escola hoje?",
    "I took an exam and did well.": "Eu fiz uma prova e me saí bem.",
    "Could you set the table, please?": "Você poderia arrumar a mesa, por favor?",
    "I’m hungry.": "Estou com fome.",
    "Is lunch ready?": "O almoço está pronto?",
    "Do you want some water?": "Você quer um pouco de água?",
    "Could you help me wash the dishes?": "Você poderia me ajudar a lavar a louça?",
    "It’s too hot today!": "Está muito quente hoje!",
    "Would you like to come over and play some videogame?": "Você quer vir aqui e jogar um pouco de videogame?",
    "I have to go to the supermarket.": "Eu tenho que ir ao supermercado.",
    "Do you want to watch a movie?": "Você quer ver um filme?",
    "Can you switch the light on?": "Você pode ligar a luz?",
    "What would you like to do this evening?": "O que você gostaria de fazer esta noite?",
    "Have you fed the dog?": "Você alimentou o cachorro?",
    "How was your day?": "Como foi seu dia?",
    "I’ll be in my room.": "Eu estarei no meu quarto.",
    "Is there anything good on TV?": "Tem alguma coisa boa na TV?",
    "Are you up to anything this evening?": "Vai fazer alguma coisa esta noite?",
    "Do you want to order something to eat?": "Você quer pedir alguma coisa para comer?",
    "Let’s eat out tonight!": "Vamos comer fora hoje à noite!",
    "What would you like for dinner?": "O que você gostaria para o jantar?",
    "I’m taking a shower and going to bed.": "Eu vou tomar um banho e ir para a cama.",
    "I have to wake up at 7.": "Eu tenho que acordar às 7 horas.",
    "I’m too tired.": "Estou muito cansado(a).",
    "I’m going to bed.": "Eu vou para a cama.",
    "Good night. Sweet dreams.": "Boa noite. Bons sonhos.",
}

palavras_medio = {
    "I’m running a little late.": "Eu estou um pouco atrasado.",
    "Are you up to anything tonight?": "Você vai fazer alguma coisa hoje à noite?",
    "You’ve got to be kidding me!": "Você só pode estar brincando comigo!",
    "There you go!": "Agora sim!",
    "It’s not worth it!": "Não vale a pena.",
    "Pull yourself together.": "Se controle, se acalme.",
    "You sold me!": "Você me convenceu!",
    "Take care!": "Se cuide!",
    "Do you want to order something to eat?": "Você quer pedir alguma coisa para comer?",
    "Don’t take it to heart": "Não leve para o lado pessoal.",
    "The most attractive accessory someone can have is confidence.": "O acessório mais atraente que alguém pode ter é a confiança.",
    "The best is yet to come.": "O melhor ainda está por vir.",
    "Say yes to new adventures.": "Diga sim a novas aventuras.",
    "A person that never made a mistake never did something new.": "Uma pessoa que nunca errou, nunca fez algo novo.",
    "The key to success is to focus on goals, not obstacles.": "A chave para o sucesso é focar nos objetivos, não nos obstáculos.",
    "Don’t be afraid to be who you are.": "Não tenha medo de ser quem você é.",
    "Life is not always easy, but it’s always worth it.": "A vida nem sempre é fácil, mas sempre vale a pena.",
    "You can quit. Or you can quit complaining.": "Você pode desistir. Ou você pode desistir de reclamar.",
    "Maybe the thing you are most scared of is exactly what you should do!": "Talvez a coisa que você mais tenha medo seja exatamente o que você deve fazer!",
    "You are stronger than you think you are.": "Você é mais forte do que imagina.",
    "Every picture tells a story.": "Toda foto conta uma história.",
    "Being happy never goes out of style.": "Ser feliz nunca sai de moda.",
    "Too lazy to think of a caption.": "Com preguiça demais para pensar em uma legenda.",
    "I was born to shine… and take selfies.": "Eu nasci para brilhar… e tirar selfies.",
    "Collect moments, not things.": "Colecione momentos, não coisas.",
    "Happiness is my partner in everything I do.": "A felicidade é minha parceira em tudo o que eu faço.",
    "Good times and tan lines!": "Bons tempos e marcas de bronzeado!",
    "Life is too short to wear boring clothes.": "A vida é muito curta para usar roupas sem graça.",
    "Take only memories, leave only footprints.": "Leve apenas memórias, deixe apenas pegadas.",
    "Those who do not travel only read one page.": "Aqueles que não viajam, leem apenas uma página.",
}

palavras_dificil = {
    "The power of imagination makes us infinite.": "O poder da imaginação nos torna infinitos.",
    "Life is like riding a bicycle. To keep your balance, you must keep moving.": "A vida é igual andar de bicicleta. Para manter o equilíbrio é preciso se manter em movimento.",
    "To plant a garden is to believe in tomorrow.": "Plantar um jardim é acreditar no amanhã.",
    "Where there is love, there is life.": "Onde há amor, há vida.",
    "A winner is a dreamer who never gives up.": "Um vencedor é um sonhador que nunca desiste.",
    "Success comes from having dreams that are bigger than your fears.": "O sucesso vem dos seus sonhos que são maiores do que os seus medos.",
    "Dare to think for yourself.": "Desafie-se a pensar por si mesmo.",
    "You must be the change you wish to see in the world.": "Você deve ser a mudança que deseja ver no mundo.",
    "All that glitters is not gold.": "Nem tudo que reluz é ouro.",
    "It’s not the years in your life that count. It’s the life in your years.": "Não são os anos da sua vida que contam. É a vida nos seus anos.",
    "I talk to myself because I love to talk to smart people.": "Eu falo sozinho porque adoro conversar com pessoas inteligentes.",
    "I tried to be normal once. It was the worst two minutes of my life.": "Eu tentei ser normal uma vez. Foram os piores dois minutos da minha vida.",
    "Don’t give up on your dreams, just keep sleeping.": "Não desista dos seus sonhos, continue dormindo.",
    "I put “happiness” on my GPS and now I’m on my way to find it.": "Coloquei “felicidade” no meu GPS e agora estou a caminho de encontrá-la.",
    "Life is a story. I’m trying to make mine a bestseller.": "A vida é uma história. Eu estou tentando fazer da minha um bestseller.",
    "I’m so good at sleeping, I can do it with my eyes closed.": "Eu sou tão bom em dormir que consigo fazer isso de olhos fechados.",
    "Yesterday I did nothing and today I’m finishing what I did yesterday.": "Ontem eu não fiz nada, e hoje estou terminando o que eu fiz ontem.",
    "I’m jealous of my parents, I’ll never have a kid as cool as theirs.": "Tenho inveja dos meus pais, eu nunca terei um filho tão legal quanto o deles.",
    "Life is short… smile while you still have teeth.": "A vida é curta… sorria enquanto você ainda tem dentes.",
    "I’m not lazy, I’m just in my energy saving mode.": "Eu não sou preguiçoso, só estou no meu modo de economia de energia.",
    "Sometimes you win, sometimes you learn.": "Às vezes você ganha, às vezes você aprende.",
    "Only one person can change your life: you.": "Só uma pessoa pode mudar a sua vida: você.",
    "What doesn’t kill you makes you stronger.": "O que não te mata, te torna mais forte.",
    "Don’t regret the past, just learn from it.": "Não se arrependa do passado, apenas aprenda com ele.",
    "The most valuable things in life are invisible to the eye.": "As coisas mais valiosas na vida são invisíveis aos olhos.",
    "Make every second count.": "Faça cada segundo valer a pena.",
    "Whatever you decide to do, make sure it makes you happy.": "O que quer que você decida fazer, certifique-se de que te faz feliz.",
    "Time is precious, waste it wisely.": "O tempo é precioso, gaste-o com sabedoria.",
    "Never stop believing.": "Nunca deixe de acreditar.",
    "Make plans that make you smile.": "Faça planos que te façam sorrir.",
    "Some hearts understand each other, even in silence.": "Alguns corações se entendem, mesmo em silêncio.",
    "Life is worth living because friends exist.": "A vida vale a pena ser vivida, porque existem amigos.",
}

# Inicialização do jogo
vidas = 5
acertos = 0
nivel = 1
dificuldade = "facil"

# Gerar uma pergunta
def gerar_pergunta():
    if dificuldade == "facil":
        palavra_ingles = random.choice(list(palavras_facil.keys()))
    elif dificuldade == "medio":
        palavra_ingles = random.choice(list(palavras_medio.keys()))
    else:
        palavra_ingles = random.choice(list(palavras_dificil.keys()))
    traducoes = list(palavras_facil.values()) + list(palavras_medio.values()) + list(palavras_dificil.values())
    traducoes.remove(eval("palavras_" + dificuldade)[palavra_ingles])
    opcoes = random.sample(traducoes, 3)
    opcoes.append(eval("palavras_" + dificuldade)[palavra_ingles])
    random.shuffle(opcoes)
    return palavra_ingles, opcoes

# Verificar se a resposta está correta
def verificar_resposta(palavra_ingles, resposta):
    if dificuldade == "facil":
        if resposta == palavras_facil[palavra_ingles]:
            return True
    elif dificuldade == "medio":
        if resposta == palavras_medio[palavra_ingles]:
            return True
    else:
        if resposta == palavras_dificil[palavra_ingles]:
            return True
    return False

# Atualizar o gráfico
def atualizar_grafico():
    plt.clf()
    plt.bar(["Vidas", "Acertos"], [vidas, acertos])
    plt.xlabel("Categoria")
    plt.ylabel("Quantidade")
    plt.title("Jogo de Inglês")
    plt.pause(0.1)

# Loop do jogo
while True:
    palavra_ingles, opcoes = gerar_pergunta()
    print(f"Traduzir \033[0;30;42m'{palavra_ingles}\033[m para português:")
    for i, opcao in enumerate(opcoes):
        print(f"{i+1} \033[0;30;43m{opcao}\033[m")
    resposta = input("Digite o número da resposta certa: ")
    resposta = opcoes[int(resposta) - 1]
    if verificar_resposta(palavra_ingles, resposta):
        print ("\033[0;30;41m Parabéns, você acertou!\033[m")
        acertos += 1
        if acertos % 10 == 0:
            vidas += 1
    else:
        print(f"\033[0;30;41m Errou!\033[m A resposta certa é {eval('palavras_' + dificuldade)[palavra_ingles]}.")
        vidas -= 1
    atualizar_grafico()
    if vidas == 0:
        print("Você perdeu todas as vidas! Game over.")
        break
    if acertos >= 30:
        print("Parabéns, você passou de nível!")
        nivel += 1
        acertos = 0
        if nivel == 2:
            dificuldade = "medio"
        elif nivel == 3:
            dificuldade = "dificil"