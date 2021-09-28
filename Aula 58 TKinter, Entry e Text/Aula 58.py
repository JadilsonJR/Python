from tkinter import *

janela=Tk()
janela.title("CFB Cursos")
janela.geometry("500x300")
janela.configure(background="#dde")

Label(janela, text="Nome",background="#dde",foreground="#009",anchor=W).place(x=10,y=10,width=100,height=20)

#anchor: Ancora serve para 
# valores para Ancora 
# N = Norte, S=Sul, E=Leste, W=Oeste 
# NE= Norodeste, SE= Sudeste, SO= Sudoeste, NO=Noroeste

vnome=Entry(janela)
vnome.place(x=10,y=30,width=200,height=20)

Label(janela, text="Telefone",background="#dde",foreground="#009",anchor=W).place(x=10,y=60,width=100,height=20)
vfone=Entry(janela)
vfone.place(x=10,y=80,width=100,height=20)


Label(janela, text="E-mail",background="#dde",foreground="#009",anchor=W).place(x=10,y=110,width=100,height=20)
vemail=Entry(janela)  # Entry é um componente para linha simples 
vemail.place(x=10,y=130,width=300,height=20)


Label(janela, text="Obs:",background="#dde",foreground="#009",anchor=W).place(x=10,y=160,width=100,height=20)
vobs=Text(janela)  #TEXT é um componente de multiplas linhas 
vobs.place(x=10,y=180,width=300,height=80)

janela.mainloop()