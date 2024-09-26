from SimpleFile import *
estudos = ["Nematodeos","Platelmintos","Poriferos","Cnidarios"]
while(True):
    texto = "qual tema você deseja: " + str(estudos)+ "\n"
    estudo = input(texto)
    if estudo in estudos:
        file = File(estudo + ".txt")
        break 
    print("tente novamente mais tarde")
for x in range(1,len(file.all_lines()),9):
    if x < 45:
        for y in range(0,6):
            print(file.read_line(x+y))
        resposta = input("qual é a correta: ")
        correta = file.read_line(x+6).strip()
        if correta == resposta:
            print("acertou")
            input()
        else:
            print("errou")
            input()
    
