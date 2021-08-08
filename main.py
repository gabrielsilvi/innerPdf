import PyPDF2

print("Digite quantos arquivos vai juntar...")
print("Ou digite 'ex' para cancelar")
nArquivos=int(input())
print("Escolhendo arquivos...")
merge = PyPDF2.PdfFileMerger()
if (type(nArquivos)==int):
    merge = PyPDF2.PdfFileMerger()
    contador = 1
    while(contador<=nArquivos):
        print("Escolhendo arquivo "+str(contador))
        arq=open(input(),'rb')
        merge.append(PyPDF2.PdfFileReader(arq))
        if(contador<nArquivos):
            merge.write(r'C:\Users\gabri\Desktop\novoArquivo.pdf')
        contador+=1

    print("Concluido!")


# for i in range(1,nArquivos+1):
#     local='arq'+str(i)

# elif(nArquivos=="ex"):
#     print("Saindo...")
# elif(type(nArquivos) != int):
#     print("Entrada Invalida!...")
#

# arq1=r'C:\Users\gabri\Desktop\teste.pdf'
# arq2=r'C:\Users\gabri\Desktop\teste2.pdf'
#
# arcpdf = PyPDF2.PdfFileReader(arq1)
# arcpdf2 = PyPDF2.PdfFileReader(arq2)
#
# merge = PyPDF2.PdfFileMerger()
#
# merge.append(arcpdf)
# merge.append(arcpdf2)
#
# merge.write(r'C:\Users\gabri\Desktop\novoArquivo.pdf')

#########Testes#########
# pag = arcpdf.getPage(0)
# pag1 = arcpdf.getPage(1)
# content = pag.extractText()+pag1.extractText()
# content = re.sub('\n','',content)
# print(content)
