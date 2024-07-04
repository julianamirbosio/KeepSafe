import customtkinter as ctk


# Configurações do uso da biblioteca ctk
ks_fonte = "Noto Sans Hebrew"
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

print("Importação e configuração inicial realizadas")

# Inicia uma classe mãe janela, do tipo ctk.Ctk, onde estão definidas as especificações
# de todas as janelas como: tamanho, tema, cor

class Janela(ctk.CTk):
    def __init__(self):
        super().__init__()
        print("Janela iniciada")
        self.configure(fg_color="#1E1E1E")
        self.title("KeepSafe")
        self.geometry("1540x800")

        # Cabeçalho

        self.fundo = ctk.CTkFrame(self, width=1540, height=800,
                                  bg_color="#1E1E1E", fg_color="#1E1E1E", corner_radius=0)
        self.fundo.place(x=0, y=0)

        self.menu = ctk.CTkFrame(self.fundo, width=1394, height=108,
                                 bg_color="#1E1E1E", fg_color="#1E1E1E",
                                 border_color="#717070", border_width=2, corner_radius=20)
        self.menu.place(x=73, y=51)

        self.aba_roxa = ctk.CTkFrame(self.fundo, width=1394, height=76,
                                     bg_color="#9219F4", fg_color="#9219F4", corner_radius=0)
        self.aba_roxa.place(x=73, y=0)

        self.KeepSafe = ctk.CTkLabel(self.fundo, text="KeepSafe", text_color="#9219F4",
                                     bg_color="#1E1E1E", font=(ks_fonte + " Black", 48))
        self.KeepSafe.place(x=136, y=81)

        self.texto = ctk.CTkLabel(self.fundo, text="Proteja e organize suas senhas com segurança máxima. "
                                                   "Simples, seguro e confiável.",
                                  text_color="#FFFFFF",
                                  bg_color="#9219F4", font=(ks_fonte + " Bold", 20))
        self.texto.place(x=340, y=29)
