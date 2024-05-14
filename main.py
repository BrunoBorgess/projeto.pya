from typing import Tuple
import customtkinter as ctk
from PIL import Image
import customtkinter as ctk
import tkinter as ttk
from tkinter import *
from CTkTable import *
from PIL import Image
import sqlite3
from tkinter import messagebox


class BackEnd():
    def conecta_db(self):
        self.con = sqlite3.connect('Sistema_cadastro')
        self.cursor = self.con.cursor()
        print('Banco de dados criado com sucesso!')
    def desconecta_db(self):
        self.con.close()
        print('Banco de dados desconectado com sucesso!')
    def criar_tabela(self):
        self.conecta_db()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuario(
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT NOT NULL,
                Email TEXT NOT NULL,
                Telefone TEXT NOT NULL
            );
        """)
        self.con.commit()
        print('Tabela criada com sucesso!!')
        self.desconecta_db()

    def cadastrar_usuario(self):
        self.entry_nome_c = self.entry_nome.get()
        self.entry_email_c= self.entry_email.get()
        self.entry_telefone_c = self.entry_telefone.get()

        self.conecta_db() # Conectando no banco de dados

        self.cursor.execute("""
            INSERT INTO Usuario (Username, Email, Telefone)
            VALUES (?, ?, ?)""", (self.entry_nome_c, self.entry_email_c, self.entry_telefone_c))
        try:
            if (self.entry_nome_c == "" or self.entry_email_c == "" or self.entry_telefone_c):
                messagebox.showerror(title='Erro', message='ERRO!! \n Preencha todos os campos!')
            elif (len(self.entry_nome_c) < 4):
                messagebox.showwarning(title='Atenção', message='O nome de usuário deve contar mais de 4 caracteres!')
            elif (len(self.entry_email_c) < 10):
                messagebox.showwarning(title='Atenção', message='O email deve contar mais de 10 caracteres!')
            elif (len(self.entry_telefone_c) == float < 10):
                messagebox.showwarning(title='ERRO', message='O telefene deve contar apenas numeros!')
            else:
                self.conecta_db.commit()
                messagebox.showinfo(title='Sistema', message='Parabéns!!\nSuas informações foram salvas com sucesso!!')
        except:
            messagebox.showerror(title='ERRO', message='Erro no processamento das informações\nPor favor, tente novamente!')







class janelas():
    def janela_gineco(self):
        self.janela_gi = ctk.CTkToplevel()
        self.janela_gi.geometry('400x200')
        self.janela_gi.title('Seus Cuidados')
        self.img_ginecolo = ctk.CTkImage(light_image=Image.open('gine.png'), size=(390, 190))
        self.lb_gineco_img = ctk.CTkLabel(self.janela_gi, text='', image=self.img_ginecolo)
        self.lb_gineco_img.place(x=5, y=5)


    def janela_papanicolau(self):
        self.janela_papa = ctk.CTkToplevel()
        self.janela_papa.geometry('400x200')
        self.janela_papa.title('Seus Cuidados')
        self.img_papanicolau = ctk.CTkImage(light_image=Image.open('papanicolau.png'), size=(390, 190))
        self.lb_papanicolau_img = ctk.CTkLabel(self.janela_papa, text='', image=self.img_papanicolau)
        self.lb_papanicolau_img.place(x=5, y=5)        

    def janela_ecografia(self):
        self.janela_eco = ctk.CTkToplevel()
        self.janela_eco.geometry('400x200')
        self.janela_eco.title('Seus Cuidados')
        self.img_pelvica = ctk.CTkImage(light_image=Image.open('pelvica.png'), size=(390, 190))
        self.lb_pelvica_img = ctk.CTkLabel(self.janela_eco, text='', image=self.img_pelvica)
        self.lb_pelvica_img.place(x=5, y=5) 

    def janela_mamografia(self):
        self.janela_mamo = ctk.CTkToplevel()
        self.janela_mamo.geometry('400x200')
        self.janela_mamo.title('Seus Cuidados')
        self.img_mamografia = ctk.CTkImage(light_image=Image.open('mamografia.png'), size=(390, 190))
        self.lb_mamografia_img = ctk.CTkLabel(self.janela_mamo, text='', image=self.img_mamografia)
        self.lb_mamografia_img.place(x=5, y=5) 


    def janela_hemografia(self):
        self.janela_hemo = ctk.CTkToplevel()
        self.janela_hemo.geometry('400x200')
        self.janela_hemo.title('Seus Cuidados')
        self.img_hemograma = ctk.CTkImage(light_image=Image.open('hemograma.png'), size=(390, 190))
        self.lb_hemograma_img = ctk.CTkLabel(self.janela_hemo, text='', image=self.img_hemograma)
        self.lb_hemograma_img.place(x=5, y=5) 


class App(ctk.CTk, janelas, BackEnd):
    def __init__(self):
        super().__init__()
        self.configura_janela_inicio()
        self.frame_opcoes()
        self.frame_botoes()
        self.frame_cadastro()

        
    def configura_janela_inicio(self):
        self.geometry('600x450')
        self.title('Saude e cuidados')
        self.resizable(False, False)

    def frame_opcoes(self):
        self.frame_saude = ctk.CTkFrame(self, width=590, height=440, fg_color='turquoise')
        self.frame_saude.place(x=5, y=5)
        self.img_saude = ctk.CTkImage(light_image=Image.open('saude.png'), size=(150, 150))
        self.lab_img = ctk.CTkLabel(self.frame_saude, image=self.img_saude, text='')
        self.lab_img.place(x=5, y=10)
        self.label_orientacao = ctk.CTkLabel(self.frame_saude, text_color='white',text='Cuidar da saúde faz com que o indivíduo\ntenha uma vida maisz feliz e duradoura.\nAlém disso, com simples cuidados, é possível evitar\n a necessidade de desembolsar grandes valores\ncom medicamentos, ter alta produtividade e viver por mais tempo.')
        self.label_orientacao.place(x=200, y=50)


    def frame_botoes(self):
        self.frame_bot = ctk.CTkFrame(self.frame_saude, width=570, height=200, fg_color='palegreen')
        self.frame_bot.place(x=9, y=200)

        # botao exame ginecologico
        self.bt_gineco = ctk.CTkButton(self.frame_bot, text='Exame Ginecologico', width=10,height=20, fg_color='orange', command=self.janela_gineco)
        self.bt_gineco.place(x=2, y=15)

        self.bt_papanicolau = ctk.CTkButton(self.frame_bot, text='Exame Papanicolau', width=40,height=20, fg_color='orange', command=self.janela_papanicolau)
        self.bt_papanicolau.place(x=2, y=50)

        self.bt_ecografia = ctk.CTkButton(self.frame_bot, text='Ecografia Pélvica', width=40,height=20, fg_color='orange', command=self.janela_ecografia)
        self.bt_ecografia.place(x=2, y=85)

        self.bt_hemografia = ctk.CTkButton(self.frame_bot, text='Mamografia de mamas', width=40,height=20, fg_color='orange', command=self.janela_mamografia)
        self.bt_hemografia.place(x=2, y=120)

        self.bt_hemograma = ctk.CTkButton(self.frame_bot, text='Hemograma', width=40,height=20, fg_color='orange', command=self.janela_hemografia)
        self.bt_hemograma.place(x=2, y=155)
    
    def frame_cadastro(self):
        self.frame_cadas = ctk.CTkFrame(self.frame_bot, width=300, height=190)
        self.frame_cadas.place(x=265, y=5)
        self.lb_cadastro = ctk.CTkLabel(self.frame_cadas, text='Deseja receber informações grátis\nsobre sáude da mulher?')
        self.lb_cadastro.place(x=50, y=10)
        self.lb_cadastrese = ctk.CTkLabel(self.frame_cadas, text='Informe seus dados!!', font=ctk.CTkFont(weight='bold'))
        self.lb_cadastrese.place(x=20, y=45)

        # entry cadastro
        self.entry_nome = ctk.CTkEntry(self.frame_cadas, width=180, height=20, placeholder_text='Nome completo', border_width=1)
        self.entry_nome.place(x=20, y=70)
        self.entry_email = ctk.CTkEntry(self.frame_cadas, width=180, height=20, placeholder_text='Email', border_width=1)
        self.entry_email.place(x=20, y=100)
        self.entry_telefone = ctk.CTkEntry(self.frame_cadas, width=180, height=20, placeholder_text='Celular DDD', border_width=1)
        self.entry_telefone.place(x=20, y=130)

        # botões
        self.bt_salvar = ctk.CTkButton(self.frame_cadas, width=60, height=20, text='Confirmar', command=self.cadastrar_usuario)
        self.bt_salvar.place(x=20, y=160)
        self.bt_limapar = ctk.CTkButton(self.frame_cadas, width=60, height=20, text='Limpar', fg_color='teal', command=self.limpar_entry)
        self.bt_limapar.place(x=140, y=160)

    def limpar_entry(self):
        self.entry_nome.delete(0, END)
        self.entry_email.delete(0, END)
        self.entry_telefone.delete(0, END)





if __name__ == "__main__":
    App = App()
    App.mainloop()
