import PyPDF2
from tkinter import filedialog, messagebox, Tcl

print("Digite quantos arquivos vai juntar...")
print("Ou digite 'exit' para cancelar")
nArquivos=int(input()) #quantidade de arquivos para juntar, forcando o user a usar tipos int
print("Escolhendo arquivos...")
merge = PyPDF2.PdfFileMerger() #chamada da funcao que faz o merge na lib pypfd2
if (type(nArquivos)==int):
    contador = 1
    quest = messagebox.showinfo(title='message', message='Escolha os Arquivos!')  # messagebox para selecao
    while(contador<=nArquivos): #loop onde usa como condicao a nArquivos para finalizar
        print("Escolhendo arquivo "+str(contador))

        arq=filedialog.askopenfilename() #escolhendo os arquivos

        merge.append(PyPDF2.PdfFileReader(arq)) #adicionado os arquivos escolhidos
        if(contador==nArquivos):
            quest=messagebox.showinfo(title='Destino', message='Escolha o destino!')
            localArq=filedialog.askdirectory() #escolhendo local onde novo arquivo sera salvo
            print(localArq+ "/novoarquivo.pdf")
            merge.write(localArq+"/novoarquivo.pdf")
        contador+=1

    print("Concluido!")
