import customtkinter as ctk
from tkinter import messagebox
import os
import re
import random
import string
from janela import Janela, ks_fonte


class KeepSafePerfil(Janela):
    def __init__(self, email_usuario):
        self.email_usuario = email_usuario
        super().__init__()
        print("JanelaLogin iniciada")

        self.frame = ctk.CTkFrame(self, width=1036, height=513,
                                  bg_color="#1E1E1E", fg_color="#1E1E1E",
                                  border_color="#717070", border_width=2, corner_radius=20)
        self.frame.place(x=73, y=247)

        self.rolavel = ctk.CTkScrollableFrame(self, width=940, height=300,
                                              bg_color="#1E1E1E", fg_color="#1E1E1E",
                                              border_color="#1E1E1E", border_width=2, corner_radius=20)
        self.rolavel.place(x=106, y=403)

        self.aba_usuario = ctk.CTkFrame(self, width=1036, height=79,
                                        bg_color="#9219F4", fg_color="#9219F4", corner_radius=0)
        self.aba_usuario.place(x=73, y=227)

        self.usuario_name = ctk.CTkLabel(self.aba_usuario, text=f"{self.email_usuario}", text_color="#FFFFFF",
                                         font=(ks_fonte+" Bold", 20),
                                         bg_color="#9219F4")
        self.usuario_name.place(x=56, y=26)

        # Buttons
        self.deslogar = ctk.CTkButton(self, text=" Sempre deslogue da sua conta 🡳", text_color="#FFFFFF",
                                      font=(ks_fonte+" Light", 20),
                                      width=296, height=41,
                                      bg_color="#1E1E1E", fg_color="#1E1E1E", corner_radius=10,
                                      command=self.deslogar)
        self.deslogar.place(x=1044, y=99)

        self.cadastrar = ctk.CTkButton(self, text="🡳", text_color="#FFFFFF",
                                       font=(ks_fonte+" Bold", 16),
                                       width=41, height=41,
                                       bg_color="#1E1E1E", fg_color="#6413F4", corner_radius=41,
                                       command=self.novo_cadastro)
        self.cadastrar.place(x=1015, y=340)

        self.verificar = ctk.CTkButton(self, text="verificar 🡳", text_color="#FFFFFF",
                                       font=(ks_fonte+" Black", 20),
                                       width=334, height=41,
                                       bg_color="#1E1E1E", fg_color="#6413F4", corner_radius=20,
                                       command=self.verificar)
        self.verificar.place(x=1132, y=588)

        # Labels

        self.texto = ctk.CTkLabel(self, text="Verifique a segurança das suas senhas",
                                  text_color="#FFFFFF",
                                  width=322, height=169,
                                  bg_color="#1E1E1E", font=(ks_fonte+" Medium", 36),
                                  wraplength=322)
        self.texto.place(x=1135, y=329)

        self.texto = ctk.CTkLabel(self, text="Dica da Keep Safe: Utilizar senhas "
                                             "distintas fortalece sua segurança",
                                  text_color="#FFFFFF",
                                  width=338, height=67,
                                  bg_color="#1E1E1E", font=(ks_fonte+" Light", 20),
                                  wraplength=338)
        self.texto.place(x=1129, y=498)

        # Entrys

        self.login = ctk.CTkEntry(self, placeholder_text="Login:",
                                  font=(ks_fonte+" SemiBold", 16),
                                  text_color="#FFFFFF", placeholder_text_color="#FFFFFF",
                                  width=234, height=42,
                                  bg_color="#1E1E1E", fg_color="#1E1E1E",
                                  border_color="#FFFFFF", border_width=1, corner_radius=10)
        self.login.place(x=106, y=340)

        self.url = ctk.CTkEntry(self, placeholder_text="Url:",
                                font=(ks_fonte+" SemiBold", 16),
                                text_color="#FFFFFF", placeholder_text_color="#FFFFFF",
                                width=365, height=42,
                                bg_color="#1E1E1E", fg_color="#1E1E1E",
                                border_color="#FFFFFF", border_width=1, corner_radius=10)
        self.url.place(x=367, y=340)

        self.senha = ctk.CTkEntry(self, placeholder_text="Senha:",
                                  font=(ks_fonte+" SemiBold", 16),
                                  text_color="#FFFFFF", placeholder_text_color="#FFFFFF",
                                  width=239, height=42,
                                  bg_color="#1E1E1E", fg_color="#1E1E1E",
                                  border_color="#FFFFFF", border_width=1, corner_radius=10)
        self.senha.place(x=750, y=340)

        self.carregar_cadastros()  # Carregar cadastros ao iniciar a janela de perfil
        self.carregar_info_frames()  # Carregar os frames com as informações dos cadastros salvos

    def novo_cadastro(self):
        login = self.login.get()
        url = self.url.get()
        senha = self.senha.get()

        if login and url and senha:
            self.adicionar_info_frame(login, senha, url)
            self.salvar_cadastro(login, senha, url)

            # Limpar os campos após adicionar o cadastro
            self.login.delete(0, 'end')
            self.url.delete(0, 'end')
            self.senha.delete(0, 'end')

        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

    def adicionar_info_frame(self, login, senha, url):
        info_frame = ctk.CTkFrame(self.rolavel, width=883, height=130,
                                  bg_color="#1E1E1E", fg_color="#161616",
                                  border_color="#FFFFFF", border_width=2, corner_radius=20)
        info_frame.pack(pady=5, padx=(20, 40), fill="x")

        frame_login = ctk.CTkFrame(info_frame, width=355, height=42,
                                   bg_color="#161616", fg_color="#1E1E1E",
                                   border_color="#717070", border_width=2, corner_radius=20)
        frame_login.place(x=16, y=16)

        frame_senha = ctk.CTkFrame(info_frame, width=355, height=42,
                                   bg_color="#161616", fg_color="#1E1E1E",
                                   border_color="#717070", border_width=2, corner_radius=20)
        frame_senha.place(x=397, y=16)

        frame_url = ctk.CTkFrame(info_frame, width=737, height=42,
                                 bg_color="#161616", fg_color="#1E1E1E",
                                 border_color="#717070", border_width=2, corner_radius=20)
        frame_url.place(x=16, y=70)

        label_login = ctk.CTkLabel(info_frame, text=f"{login}",
                                   text_color="#FFFFFF",
                                   bg_color="#1E1E1E", font=("Noto Sans Hebrew SemiBold", 20))
        label_login.place(x=30, y=22)

        senha_oculta = "*" * len(senha)
        label_senha = ctk.CTkLabel(info_frame, text=senha_oculta,
                                   text_color="#FFFFFF",
                                   bg_color="#1E1E1E", font=("Noto Sans Hebrew SemiBold", 20))
        label_senha.place(x=412, y=22)

        label_url = ctk.CTkLabel(info_frame, text=f"{url}",
                                 text_color="#FFFFFF",
                                 bg_color="#1E1E1E", font=("Noto Sans Hebrew SemiBold", 20))
        label_url.place(x=30, y=75)

        def toggle_senha():
            if label_senha.cget("text") == senha_oculta:
                label_senha.configure(text=senha)
            else:
                label_senha.configure(text=senha_oculta)

        def remover_info_frame():
            info_frame.destroy()
            self.remover_cadastro(login, senha, url)

        botao_mostrar_senha = ctk.CTkButton(info_frame, text="Mostrar",
                                            text_color="#FFFFFF",
                                            font=("Noto Sans Hebrew Bold", 12),
                                            width=70, height=32,
                                            bg_color="#1E1E1E", fg_color="#6413F4",
                                            corner_radius=10, command=toggle_senha)
        botao_mostrar_senha.place(x=760, y=16)

        botao_remover = ctk.CTkButton(info_frame, text="Excluir",
                                      text_color="#FFFFFF",
                                      font=("Noto Sans Hebrew Bold", 12),
                                      width=70, height=32,
                                      bg_color="#1E1E1E", fg_color="#6413F4",
                                      corner_radius=10, command=remover_info_frame)
        botao_remover.place(x=760, y=70)

    def salvar_cadastro(self, login, senha, url):
        arquivo_usuario = f"{self.email_usuario}_cadastros.txt"

        with open(arquivo_usuario, "a") as arquivo:
            arquivo.write(f"{login},{senha},{url}\n")

    def carregar_cadastros(self):
        arquivo_usuario = f"{self.email_usuario}_cadastros.txt"

        if not os.path.exists(arquivo_usuario):
            return []

        cadastros = []
        with open(arquivo_usuario, "r") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            login, senha, url = linha.strip().split(',')
            cadastros.append({"login": login, "senha": senha, "url": url})

        return cadastros

    def carregar_info_frames(self):
        cadastros = self.carregar_cadastros()

        for cadastro in cadastros:
            self.adicionar_info_frame(cadastro["login"], cadastro["senha"], cadastro["url"])

    def remover_cadastro(self, login, senha, url):
        arquivo_usuario = f"{self.email_usuario}_cadastros.txt"

        if not os.path.exists(arquivo_usuario):
            return

        with open(arquivo_usuario, "r") as arquivo:
            linhas = arquivo.readlines()

        with open(arquivo_usuario, "w") as arquivo:
            for linha in linhas:
                if linha.strip() != f"{login},{senha},{url}":
                    arquivo.write(linha)

    def verificar(self):
        cadastros = self.carregar_cadastros()

        senhas_repetidas = self.encontrar_senhas_repetidas(cadastros)
        senhas_fraca, senhas_media, senhas_forte = self.avaliar_forca_senhas(cadastros)

        mensagem = ""

        if senhas_repetidas:
            mensagem += f"Senhas repetidas encontradas:\n"
            for senha in senhas_repetidas:
                mensagem += f"URL: {senha['url']} - Senha: {senha['senha']}\n"
            mensagem += "\n"
        print()
        if senhas_fraca:
            mensagem += f"Senhas fracas encontradas:\n"
            for senha in senhas_fraca:
                mensagem += f"URL: {senha['url']} - Senha: {senha['senha']}\n"
                sugestao = self.gerar_senha_forte()
                mensagem += f"Sugestão de senha forte: {sugestao}\n"
                print()
            print()
            mensagem += "\n"

        if senhas_media:
            mensagem += f"Senhas de força média encontradas:\n"
            for senha in senhas_media:
                mensagem += f"URL: {senha['url']} - Senha: {senha['senha']}\n"
                print()
            mensagem += "\n"

        if senhas_forte:
            mensagem += f"Senhas fortes encontradas:\n"
            for senha in senhas_forte:
                mensagem += f"URL: {senha['url']} - Senha: {senha['senha']}\n"
                print()
            mensagem += "\n"

        if not mensagem:
            mensagem = "Nenhuma senha repetida encontrada. Todas as senhas estão seguras."

        messagebox.showinfo("Verificação de Senhas", mensagem)

    def gerar_senha_forte(self):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(16))  # Gerando senha de 16 caracteres
        return senha

    def encontrar_senhas_repetidas(self, cadastros):
        senhas_repetidas = []
        senhas_verificadas = []

        for cadastro in cadastros:
            senha = cadastro["senha"]
            if senha not in senhas_verificadas and cadastros.count(cadastro) > 1:
                senhas_repetidas.append(cadastro)
                senhas_verificadas.append(senha)

        return senhas_repetidas

    def avaliar_forca_senhas(self, cadastros):
        senhas_fraca = []
        senhas_media = []
        senhas_forte = []

        for cadastro in cadastros:
            senha = cadastro["senha"]

            if len(senha) < 8 or re.search(r'[a-z]', senha) is None or re.search(r'[A-Z]', senha) is None or re.search(
                    r'\d', senha) is None:
                senhas_fraca.append(cadastro)
            elif len(senha) >= 8 and re.search(r'[a-z]', senha) and re.search(r'[A-Z]', senha) and re.search(r'\d',
                                                                                                             senha):
                senhas_media.append(cadastro)
            elif len(senha) >= 12 and re.search(r'[a-z]', senha) and re.search(r'[A-Z]', senha) and re.search(r'\d',
                                                                                                              senha) and re.search(
                    r'[^a-zA-Z\d\s]', senha):
                senhas_forte.append(cadastro)

        return senhas_fraca, senhas_media, senhas_forte

    def deslogar(self):
        if messagebox.askyesno("Sair", "Deseja realmente sair?"):
            self.destroy()

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    # Exemplo de uso para abrir a janela de perfil diretamente
    app = KeepSafePerfil("usuario_exemplo@gmail.com")
    app.run()