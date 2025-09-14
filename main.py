import subprocess
import os

while True:
    # pegar caminho atual
    caminho = os.getcwd()

    #pega comando do user
    comando = input(caminho + " >>> ")

    #pra sair do loop
    if comando.lower() == "sair":
        print("Encerrando...")
        break

    #se o comando for "cd...." vai pra essa condicional pra mudar o caminho
    if comando.startswith("cd "):
        try:
            novo_caminho = comando[3:].strip()
            os.chdir(novo_caminho)
        except FileNotFoundError:
            print("Diretório não encontrado:", novo_caminho)
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
        if resultado.stderr:
            print("Erro:", resultado.stderr.strip())

    #se der um erro no subprocess tbm trata
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
