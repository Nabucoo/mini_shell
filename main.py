import subprocess
import os

#inicializa histórico de comandos, obs: só os comandos bem-sucedidos no momento que executados estarão na lista
comandos = []


def sair():
    print("Encerrando!")
    exit()

def limpar_tela():
    os.system("cls")

def listar_historico(comandos):
    if comandos:
        for i, comando in enumerate(comandos):
            print(f"comando nº {i + 1}: {comando}")
    else:
        print("Histórico de comandos vázio!")

def rodar_comando_n(comandos, n):
    return comandos[n - 1]

def rodar_ultimo_comando(comandos):
    return comandos[-1]


while True:
    # pegar caminho atual
    caminho = os.getcwd()

    #pega comando do user
    comando = input(caminho + " >>> ")
    
    #pra sair do loop
    if comando.lower() == "sair":
        sair()

    #pra mostrar o histórico de comandos
    if comando.lower() == "history":
        listar_historico(comandos)
        continue

    #quando o comando comeca com "!" entra na condicional de rodar o comando n do hitórico
    if comando[0] == "!":
        #tenta transformar o que o usuario escreveu depois de ! em inteiro, caso nao de erro ele rod o comando n
        #caso de erro ele checa o tamanho do comando é 2 caracterees e o segundo é ! tambem, caso seja, ele roda o ultimo comando
        #do histórico, como pedido no exercício do projeto, caso não cumpra essas condicionais, cospe um erro para o usuário
        try:
            i = int(comando[1:])
            comando = rodar_comando_n(comandos, i)
        except Exception as e:
            if len(comando) == 2 and comando[1] == "!":
                comando = rodar_ultimo_comando(comandos)
            else:
                print("Erro ao resgatar comando!")
                continue

    #comando de limpar tela
    if comando.lower() == "cls":
        limpar_tela()
    
    #se o comando for "cd...." vai pra essa condicional pra mudar o caminho
    if comando.startswith("cd "):
        try:
            novo_caminho = comando[3:].strip()
            os.chdir(novo_caminho)
            comandos.append(comando)
        except FileNotFoundError:
            print("Erro ao encontrar diretório")
        except Exception as e:
            print("Erro:", e)
        continue
        
    #roda o comando com o subprocess
    try:
        resultado = subprocess.run(
            comando,
            shell=True,
            capture_output=True,
            text=True
        )

    #printa o resultado em caso de erro ou nao
        if resultado.stdout:
            print(resultado.stdout.strip())
            comandos.append(comando)
        elif resultado.stderr:
            print("Erro:", resultado.stderr.strip())
        else:
            comandos.append(comando)
        

    #se der um erro no subprocess tbm trata
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    


