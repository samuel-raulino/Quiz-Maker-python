import os

def input2(str):
    input()
    os.system("cls")

class File:
    def __init__(self, dir_file):
        self.dir_file = dir_file
    
    def create(self):
        with open(self.dir_file, "a") as file:
            pass
        return file 
    
    #editar
    def append(self, addition):
        with open(self.dir_file, "a") as file:
            file.write("\n")
            file.write(addition)
    def append_line(self, linha, addition):
        with open(self.dir_file, "r") as reader_file:
            all_lines = reader_file.readlines()
        
        if linha - 1 < len(all_lines):
            all_lines[linha - 1] = all_lines[linha - 1].strip() + addition + '\n'
        else:
            raise IndexError("A linha que você ta tentando adicionar não existe")
        
        with open(self.dir_file, "w") as writer_file:
            writer_file.writelines(all_lines)
    #ler
    def replace(self, linha, addition):
        with open(self.dir_file, "r") as reader_file:
            all_lines = reader_file.readlines()
        
        if linha - 1 < len(all_lines):
            all_lines[linha - 1] = addition + '\n'
        else:
            raise IndexError("A linha que você ta tentando adicionar não existe")
        
        with open(self.dir_file, "w") as writer_file:
            writer_file.writelines(all_lines)
    def all_lines(self):
        with open(self.dir_file, "r") as file:
            return file.readlines()
    
    def read_line(self, linha):
        with open(self.dir_file, "r") as reader_file:
            all_lines = reader_file.readlines()
        
        if linha - 1 < len(all_lines):
            return all_lines[linha - 1]
        else:
            raise IndexError("A linha que você ta tentando pegar não existe")
    def line_numbers(self):
        with open(self.dir_file, "r") as reader_file:
            all_lines = reader_file.readlines()
        cont = 0
        for x in all_lines:
            cont +=1
        return cont

if __name__ == "__main__":
    print("bem vindo ao programa")
    input2("clique enter para iniciar")
    arquivo = File("main") #cria a classe, e nomeia ela como "arquivo"
    print("cria a classe, e nomeia ela como 'arquivo'")

    input2("clique enter para prosseguir")
    arquivo.create()
    print("cria o arquivo")

    
    input2("clique enter para prosseguir")
    arquivo.append("-"*10,"")#acrescenta 10 vezes o "-" sem quebra de linha
    print("acrescenta 10 vezes o '-' sem quebra de linha")
    
    input2("clique enter para prosseguir")
    arquivo.append("Bem vindo ao módulo.","")
    print("acrescenta uma iniciativa sem quebra de linha")

    input2("clique enter para prosseguir")
    arquivo.append("-"*10,"")
    print("acrescenta 10 vezes o '-' sem quebra de linha")

    input2("clique enter para prosseguir")
    arquivo.append("a","\n") 
    print("acrescenta ao arquivo a letra 'a' com quebra de linha")

    input2("clique enter para prosseguir")
    arquivo.append("b","\n")
    print("acrescenta ao arquivo a letra 'b' com quebra de linha")

    input2("clique enter para prosseguir")
    arquivo.append("c","\n")
    print("acrescenta ao arquivo a letra 'c' com quebra de linha")

    input2("clique enter para prosseguir")
    arquivo.append("d","\n")
    print("acrescenta ao arquivo a letra 'd' com quebra de linha")

    input2("clique enter para prosseguir")
    arquivo.append_line(5, " 2")
    print("acrescenta ao arquivo o numero em string '2' na quinta linha")
    input2("clique enter para deletar o arquivo e finalizar o programa...")
    os.remove("main.txt") #remove o arquivo
    print("deleta o arquivo e finaliza o programa.")


