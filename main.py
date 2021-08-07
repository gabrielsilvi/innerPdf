import re
import inner
import PyPDF2

print("Digite quantos arquivos vai juntar...")
print("Ou digite 'ex' para cancelar")
nArquivos=int(input())
print(type(nArquivos))
if (type(nArquivos)==int):
    print("Escolhendo arquivos...")


elif(nArquivos=="ex"):
    print("Saindo...")
elif(type(nArquivos) != int):
    print("Entrada Invalida!...")


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
