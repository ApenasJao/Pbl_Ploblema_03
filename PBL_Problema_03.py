
qst_1={"Assunto": "Geografia",
       "Pontos":10,
       "Questão":"O ciclo da água é o mecanismo responsável por proporcionar o reabastecimento da água no planeta, sabendo disso, determine abaixo qual das alternativas possui ciclo correto.",
       "Opção 1": "Precipitação, evaporação, condensação, ebulição, transpiração. ",
       "Opção 2": "Transpiração, condensação, dessalinização, infiltração, evaporação.",
       "Opção 3": "Condensação, hidrólise, precipitação, evaporação, infiltração. ",
       "Opção 4": "Evaporação, precipitação, transpiração, infiltração, condensação.",
       "Opção 5": "Chuvas, transpiração, infiltração, ebulição.",
       "Resposta Correta": "Evaporação, precipitação, transpiração, infiltração, condensação.",
        "Explicação": [
    # "Ebulição é um processo que ocorre em temperaturas altas enão faz parte do ciclo natural de água.",
    #                   "Dessalinização é usado para tornar a água do mar potável e não faz parte do ciclo da água.",
    #                   "Hidrólise é uma reação química de divisão de moléculas em presença de água, não faz parte do ciclo natural da água.",
                      "Esta alternativa descreve corretamente o ciclo da água, todos os processos citados são naturais.",
                    #   "Ebulição é um processo que ocorre em temperaturas altas enão faz parte do ciclo natural de água."
                    ],
       "Dica":["A hidrólise é a reação química em que uma molécula se divide em partes menores pela presença de água."]}
qst_2={"Assunto": "Geografia",
       "Pontos":10,
       "Questão":"Qual dos continentes listados abaixo possui mais oceanos ao seu redor?",
       "Opção 1": "África.",
       "Opção 2": "América Central.",
       "Opção 3": "América do Norte.",
       "Opção 4": "América do Sul.",
       "Opção 5": "Ásia.",
       "Resposta Correta": "Ásia.",
       "Explicação": [
        #    "A África é cercada por apenas dois oceanos: Atlântico e Índico. Já a Ásia é cercada por 3.",
        #               "A América Central é cercada por apenas 2 oceanos: Pacífico e Atlântico. Já a Ásia possui 3.",
        #               "A América do Norte é cercada por 3 oceanos: Atlântico, Pacífico e Ártico, porém, não é o continente com mais oceanos ao seu redor. A Ásia possui mais.",
        #               "A América do Sul é cercada por 2 oceanos: Atlântico e Pacífico. Já a Ásia é cercada por 3.",
                      "A Ásia é cercada por 3 oceanos: Pacíficoa, Índico e Ártico. Sendo o continente com maior número de oceanos ao seu redor."],
        "Dica":["Este continente é banhado por 3 oceanos.","É banhado pelos oceanos Índico, Pacífico e Ártico."]}
qst_3={"Assunto": "Geografia",
       "Pontos":10,
       "Questão":"A ação das ondas e marés tem o poder de moldar o relevo costeiro. Determine qual formação abaixo é ocasionado dessa ação?",
       "Opção 1": "Cadeias montanhosas",
       "Opção 2": "Planaltos",
       "Opção 3": "Dunas",
       "Opção 4": "Falésias",
       "Opção 5": "Morros",
       "Resposta Correta": "Falésias",
        "Explicação": [
                        # "Cadeias montanhosas são formadas por processos tectônicos e orogênese, não pela ação das ondas e marés.",
                    #   "Planaltos são formados pela erosão e processos tectônicos, mas não pela ação das ondas e marés.",
                    #   "Dunas são formadas pela ação do vento, mas não pela ação das ondas e marés.",
                      "Esta alternativa descreve corretamente a formação gerada pela erosão da costa devido à ação contínua das ondas e marés. São paredões rochosos e íngremes.",
                    #   "Morros são formadas por processos de erosão e sedimentação, mas não pela ação das ondas e marés"
                        ],
        "Dica":["Paredões íngremes e rochosos"]}
qst_4={"Assunto": "Geografia",
       "Pontos":10,
       "Questão":"Qual é o principal processo responsável pela formação das montanhas?",
       "Opção 1": "Erosão",
       "Opção 2": "Sedimentação",
       "Opção 3": "Orogênese",
       "Opção 4": "Intemperismo",
       "Opção 5": "Vulcanismo",
       "Resposta Correta": "Orogênese",
       "Explicação": ["A orogênese é o processo de formação de montanhas por conta do movimento e choque de placas tectônicas.","","","",""],
        "Dica":["Responsável pela elevação do solo. ","Pode levar milhões de anos para ocorrer."]}
qst_5={"Assunto": "Geografia",
       "Pontos":10,
       "Questão":"Qual é o principal responsável pela erosão das regiões áridas, possuindo a capacidade de modelar o seu relevo? ",
       "Opção 1": "Água",
       "Opção 2": "Sol",
       "Opção 3": "Gelo",
       "Opção 4": "O clima",
       "Opção 5": "Vento",
       "Resposta Correta": "Vento",
       "Explicação": ["Em áreas áridas, o vento é o principal agente de erosão, transportando areia e moldando formações como dunas.","","","",""],
        "Dica":["Essas regiões possuem muita areia."]}
qst_6={"Assunto": "Geografia",
       "Pontos":10,
       "Questão":"Caracterizado por possuir temperaturas altas e chuvas constantes durante todo o ano, sendo presente na região da Floresta Amazônica, qual das alternativas abaixo possui essas características?",
       "Opção 1": "Clima Subtropical",
       "Opção 2": "Clima Mediterrâneo",
       "Opção 3": "Clima Semiárido",
       "Opção 4": "Clima Equatorial",
       "Opção 5": "Clima Árido",
       "Resposta Correta": "Clima Equatorial",
       "Explicação": ["O clima equatorial tem temperaturas elevadas e chuvas constantes ao longo do ano, sendo típico da região amazônica."],
        "Dica":["Este clima cobre a Colômbia, Equador, Guiana, Guiana Francesa, Venezuela, Bolívia e o norte do Brasil."]}

lista_Q=[qst_1,qst_2,qst_3,qst_4,qst_5,qst_6]

with open('Questoes.txt','w',encoding='utf8') as arq:
    for e in range(len(lista_Q)):    
        for k,v in (lista_Q[e].items()):
            arq.write(f"{str(k)} : ")
            arq.write(f"{str(v)}\n")
        arq.write('\n')
    arq.close()

with open('Questoes.txt','r',encoding='utf8')as arq:
    for v in arq:
        print(v,end="")