import customtkinter as ctk
from tkinter import messagebox
import os
from janela import Janela, ks_fonte
from widget_sobre import KeepSafeSobre
from janela_perfil import KeepSafePerfil

#1E1E1E -> cinza escuro
#717070 -> cinza claro
#9219F4 -> roxo

class KeepSafeLogCad(Janela):
    def __init__(self):
        super().__init__()
        print("JanelaLogin iniciada")

        #Frames

        self.framecadastro = ctk.CTkFrame(self.fundo, width=692, height=357,
                                  bg_color="#1E1E1E", fg_color="#1E1E1E",
                                  border_color="#000000", border_width=3, corner_radius=20)
        self.framecadastro.place(x=73, y=397)

        self.framelogin = ctk.CTkFrame(self.fundo, width=692, height=357,
                                  bg_color="#1E1E1E", fg_color="#1E1E1E",
                                  border_color="#000000", border_width=3, corner_radius=20)
        self.framelogin.place(x=781, y=397)

        # Entrys

        self.nome = ctk.CTkEntry(self.fundo, placeholder_text="Nome:",
                                 font=(ks_fonte+" SemiBold", 16),
                                 text_color="#FFFFFF", placeholder_text_color="#FFFFFF",
                                 width=444, height=42,
                                 bg_color="#1E1E1E", fg_color="#1E1E1E",
                                 border_color="#FFFFFF", border_width=1, corner_radius=10)
        self.nome.place(x=196, y=447)

        self.email1 = ctk.CTkEntry(self.fundo, placeholder_text="Email:",
                                   font=(ks_fonte+" SemiBold", 16),
                                   text_color="#FFFFFF", placeholder_text_color="#FFFFFF",
                                   width=444, height=42,
                                   bg_color="#1E1E1E", fg_color="#1E1E1E",
                                   border_color="#FFFFFF", border_width=1, corner_radius=10)
        self.email1.place(x=196, y=506)

        self.senha1 = ctk.CTkEntry(self.fundo, placeholder_text="Senha:", show="*",
                                   font=(ks_fonte+" SemiBold", 16),
                                   text_color="#FFFFFF", placeholder_text_color="#FFFFFF",
                                   width=444, height=42,
                                   bg_color="#1E1E1E", fg_color="#1E1E1E",
                                   border_color="#FFFFFF", border_width=1, corner_radius=10)
        self.senha1.place(x=196, y=566)

        self.senha2 = ctk.CTkEntry(self.fundo, placeholder_text="Confirmar senha:", show="*",
                                   font=(ks_fonte+" SemiBold", 16),
                                   text_color="#FFFFFF", placeholder_text_color="#FFFFFF",
                                   width=444, height=42,
                                   bg_color="#1E1E1E", fg_color="#1E1E1E",
                                   border_color="#FFFFFF", border_width=1, corner_radius=10)
        self.senha2.place(x=196, y=625)

        self.email = ctk.CTkEntry(self.fundo, placeholder_text="Email:",
                                  font=(ks_fonte+" SemiBold", 16),
                                  text_color="#FFFFFF", placeholder_text_color="#FFFFFF",
                                  width=444, height=42,
                                  bg_color="#1E1E1E", fg_color="#1E1E1E",
                                  border_color="#FFFFFF", border_width=1, corner_radius=10)
        self.email.place(x=897, y=447)

        self.senha = ctk.CTkEntry(self.fundo, placeholder_text="Senha:", show="*",
                                  font=(ks_fonte+" SemiBold", 16),
                                  text_color="#FFFFFF", placeholder_text_color="#FFFFFF",
                                  width=444, height=42,
                                  bg_color="#1E1E1E", fg_color="#1E1E1E",
                                  border_color="#FFFFFF", border_width=1, corner_radius=10)
        self.senha.place(x=897, y=506)

        # Buttons

        self.cadastrar = ctk.CTkButton(self.fundo, text="Submeter", text_color="#FFFFFF",
                                       font=(ks_fonte+" Bold", 16),
                                       width=100, height=41,
                                       bg_color="#1E1E1E", fg_color="#6413F4", corner_radius=10,
                                       command=self.cadastrar)
        self.cadastrar.place(x=546, y=693)

        self.logar = ctk.CTkButton(self.fundo, text="Login", text_color="#FFFFFF",
                                   font=(ks_fonte+" Bold", 16),
                                   width=100, height=41,
                                   bg_color="#1E1E1E", fg_color="#6413F4", corner_radius=10,
                                   command=self.logar)
        self.logar.place(x=1249, y=566)

        self.sobre = ctk.CTkButton(self.fundo, text="Sobre os programadores 🡳", text_color="#FFFFFF",
                                   font=(ks_fonte+" Light", 20),
                                   width=296, height=41,
                                   bg_color="#1E1E1E", fg_color="#6413F4", corner_radius=10,
                                   command=self.sobre)
        self.sobre.place(x=1044, y=99)

        # Labels

        self.texto = ctk.CTkLabel(self.fundo, text="Cadastrar:",
                                  text_color="#FFFFFF",
                                  bg_color="#1E1E1E", font=(ks_fonte+" SemiBold", 24))
        self.texto.place(x=84, y=352)

        self.texto = ctk.CTkLabel(self.fundo, text="Logar:",
                                  text_color="#FFFFFF",
                                  bg_color="#1E1E1E", font=(ks_fonte+" SemiBold", 24))
        self.texto.place(x=799, y=352)

        self.texto = ctk.CTkLabel(self.fundo, text="Mantenha suas senhas seguras e organizadas em um só lugar",
                                  text_color="#FFFFFF",
                                  width=679, height=99,
                                  bg_color="#1E1E1E", font=(ks_fonte+" SemiBold", 32),
                                  wraplength=679)
        self.texto.place(x=425, y=190)

        self.texto = ctk.CTkLabel(self.fundo, text="Fácil de usar, seguro e confiável – "
                                                    "o KeepSafe é a solução definitiva para a gestão de suas senhas.",
                                  text_color="#FFFFFF",
                                  width=475, height=53,
                                  bg_color="#1E1E1E", font=(ks_fonte+" Regular", 16),
                                  wraplength=475)
        self.texto.place(x=524, y=288)

    def run(self):
        self.mainloop()


    def abrir_janela_perfil(self):
        print("Abrindo janela principal")
        self.destroy()  # Destroi a janela de login
        janela_perfil = KeepSafePerfil()  # Cria uma instância da classe CeuAzul Previsao
        janela_perfil.mainloop()


    def sobre(self):
        print("abrindo")
        #self.destroy() # Destroi a janela de login

        janela_sobre = KeepSafeSobre(self.fundo)


    def cadastrar(self):
        # Obter o e-mail e as senhas inseridos pelo usuário
        email_cadastro = self.email1.get()
        senha_cadastro = self.senha1.get()
        confirmar_senha = self.senha2.get()

        # Verificar se os campos não estão vazios
        if not email_cadastro or not senha_cadastro or not confirmar_senha:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos!")
            return

        # Verificar se as senhas coincidem
        if senha_cadastro != confirmar_senha:
            messagebox.showerror("Erro", "As senhas não coincidem!")
            return

        # Salvar o cadastro em um arquivo (podemos usar o e-mail como nome do arquivo para cada usuário)
        arquivo_usuario = f"{email_cadastro}.txt"
        if os.path.exists(arquivo_usuario):
            messagebox.showwarning("Aviso", "Usuário já cadastrado!")
            return

        with open(arquivo_usuario, "w") as arquivo:
            arquivo.write(f"{email_cadastro}\n{senha_cadastro}")

        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")

    def logar(self):
        email_login = self.email.get()
        senha_login = self.senha.get()

        # Verificar se os campos não estão vazios
        if not email_login or not senha_login:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos!")
            return

        # Verificar se o arquivo do usuário existe
        arquivo_usuario = f"{email_login}.txt"
        if not os.path.exists(arquivo_usuario):
            messagebox.showerror("Erro", "Usuário não encontrado!")
            return

        # Verificar se a senha está correta
        with open(arquivo_usuario, "r") as arquivo:
            linhas = arquivo.readlines()
            senha_armazenada = linhas[1].strip()

        if senha_login != senha_armazenada:
            messagebox.showerror("Erro", "Senha incorreta!")
            return

        self.destroy()
        KeepSafePerfil(email_login).run()
