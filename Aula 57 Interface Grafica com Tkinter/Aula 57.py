from tkinter import *

janela=Tk()  #Criando uma Janela 
janela.title("CFB Cursos")
janela.geometry("500x300") #Indicado o Tamanho 
janela.configure(background="#007")

txt1=Label(janela,text="Curso de Python",background="#FF0",foreground="#000")
txt1.place(x=10, y=10, width=150, height=30) #Indicar Cordenadas manualmente 


vtxt="Módulo TKinter"
vback="#FF0"
vfg="#000"
txt2=Label(janela, text=vtxt, bg=vback, fg=vfg)
txt2.pack(ipadx=20, ipady=20, padx=5, pady=5, side="top", fill=X, expand= True)

#Ipadx:Largura
#Ipady:Altura
#padx: quase um margin no css
#pady
#fill: preenchimento podendo ser no sentido horizontal X ou Vertical Y
#expand: Responsivel  


janela.mainloop()  #Metodo para Rodar a Janela 