from Aluno import Aluno

turma = []

while (True):

    try:
        opcao = int(input("Turma BSI " + "\n" + "1) Cadastro Aluno"
                      + "\n" + "2) Imprimir Turma" + "\n" + "3) Sair " + "\n"))

        if (opcao == 3):
            print("Obrigado por utilizar o nosso sistema! Volte Sempre :)")
            break

        if (opcao <= 0 or opcao > 3):
            print("Opção inválida! Digite um número válido referente as opções oferecidas no menu... ")
            continue

        if (opcao == 1):
            a = Aluno()
            a.matricula = input("Informe a matricula do Aluno: ")
            a.nome = input("Informe o nome do Aluno: ")
            a.nota1 = float(input("Informe a nota da VA1 (de 0 a 100) : "))
            a.nota2 = float(input("Informe a nota da VA2: (de 0 a 100) "))
            a.notaTrabalho = float(input("Informe a nota do Trabalho: (de 0 a 100) "))
            a.media = (((a.nota1 * 2.5) + (a.nota2 * 2.5) + (a.notaTrabalho * 2))/7)
            if (a.media > 6):
                a.status = "Aprovado"
            else:
                a.status = "Reprovado"
            turma.append(a)

        if (opcao == 2):
            for aluno in turma:
                print(" | Aluno : " + aluno.nome + " | Matricula : "
                    + aluno.matricula + " | Nota Av1: " + str(aluno.nota1)
                    + " | Nota Av2: " + str(aluno.nota2) + " | Trabalho: " + str(aluno.notaTrabalho)
                    + " | Media: " + str(round(aluno.media, 2)) + " | Resultado: " + str(aluno.status)
                    )
    except:
        print("Entradas de texto são inválidas no menu! Digite o número referente a opção desejada... ")