import customtkinter as ctk
from janela import ks_fonte


class KeepSafeSobre:
    def __init__(self, fundo):
        self.fundo = fundo

        # FrameTop
        self.frametop = ctk.CTkFrame(self.fundo, width=1540, height=623,
                                    bg_color="#1E1E1E", fg_color="#1E1E1E",
                                    border_color="#1E1E1E", border_width=0, corner_radius=20)
        self.frametop.place(x=0, y=177)
        # Titulo

        self.titulo = ctk.CTkLabel(self.fundo, text="Nossos Idealizadores:",
                                  text_color="#FFFFFF",
                                  bg_color="#1E1E1E", font=(ks_fonte, 24))
        self.titulo.place(x=645, y=177)

        # FrameJu

        self.frameju = ctk.CTkFrame(self.fundo, width=539, height=432,
                                          bg_color="#1E1E1E", fg_color="#1E1E1E",
                                          border_color="#717070", border_width=3, corner_radius=20)
        self.frameju.place(x=226, y=231)

        self.retangulo_roxo1 = ctk.CTkFrame(self.fundo, width=538, height=91,
                                     bg_color="#9219F4", fg_color="#9219F4", corner_radius=0)
        self.retangulo_roxo1.place(x=226, y=231)

        self.nomeju = ctk.CTkLabel(self.fundo, text="Juliana M. Bosio",
                                   text_color="#FFFFFF", bg_color="#9219F4",
                                   font=(ks_fonte + " Bold", 32))
        self.nomeju.place(x=268, y=259)

        self.infoju = ctk.CTkLabel(self.fundo, text="Graduanda em Ciência da Computação pela "
                                                    "Universidade Federal de Santa Catarina. "
                                                    "Atualmente é diretora de marketing na"
                                                    " empresa Júnior Pixel.",
                                   text_color="#FFFFFF", width=445, height=110,
                                   wraplength=440, anchor="w",
                                   bg_color="#1E1E1E", font=(ks_fonte, 20))
        self.infoju.place(x=265, y=362)

        self.github01 = ctk.CTkLabel(self.fundo, text="Github:",
                                   text_color="#FFFFFF", bg_color="#1E1E1E",
                                   font=(ks_fonte + " Bold", 20))
        self.github01.place(x=265, y=487)
        self.github02 = ctk.CTkLabel(self.fundo, text="https://github.com/julianamirbosio",
                                     text_color="#9219F4", bg_color="#1E1E1E",
                                     font=(ks_fonte + " Bold", 20))
        self.github02.place(x=265, y=513)

        # FrameVini

        self.framevini = ctk.CTkFrame(self.fundo, width=539, height=432,
                                    bg_color="#1E1E1E", fg_color="#1E1E1E",
                                    border_color="#717070", border_width=3, corner_radius=20)
        self.framevini.place(x=780, y=231)

        self.retangulo_roxo2 = ctk.CTkFrame(self.fundo, width=538, height=91,
                                            bg_color="#9219F4", fg_color="#9219F4", corner_radius=0)
        self.retangulo_roxo2.place(x=780, y=231)

        self.nomevini = ctk.CTkLabel(self.fundo, text="Vinícios R. Buzzi",
                                   text_color="#FFFFFF", bg_color="#9219F4",
                                   font=(ks_fonte + " Bold", 32))
        self.nomevini.place(x=822, y=259)

        self.infovini = ctk.CTkLabel(self.fundo, text="Graduando em Ciência da Computação pela "
                                                      "Universidade Federal de Santa Catarina. "
                                                      "Atualmente é integrante do PETComputação "
                                                      "e bolsista PIBIC.",
                                   text_color="#FFFFFF", width=445, height=110,
                                   wraplength=440, anchor="w",
                                   bg_color="#1E1E1E", font=(ks_fonte, 20))
        self.infovini.place(x=820, y=362)

        self.github11 = ctk.CTkLabel(self.fundo, text="Github:",
                                     text_color="#FFFFFF", bg_color="#1E1E1E",
                                     font=(ks_fonte + " Bold", 20))
        self.github11.place(x=820, y=487)
        self.github12 = ctk.CTkLabel(self.fundo, text="https://github.com/buzziologia",
                                     text_color="#9219F4", bg_color="#1E1E1E",
                                     font=(ks_fonte + " Bold", 20))
        self.github12.place(x=820, y=513)

        # Data

        self.data = ctk.CTkFrame(self.fundo, width=612, height=42,
                                      bg_color="#1E1E1E", fg_color="#1E1E1E",
                                      border_color="#717070", border_width=3, corner_radius=20)
        self.data.place(x=464, y=693)
        self.dadostexto = ctk.CTkLabel(self.fundo, text="Dados referentes a junho de 2024.",
                                   text_color="#FFFFFF",
                                   bg_color="#1E1E1E", font=(ks_fonte, 24))
        self.dadostexto.place(x=601, y=703)

        # Buttons

        self.voltar = ctk.CTkButton(self.fundo, text="Volte ao menu principal 🡳", text_color="#FFFFFF",
                                   font=(ks_fonte + " Light", 20),
                                   width=296, height=41,
                                   bg_color="#1E1E1E", fg_color="#6413F4", corner_radius=10,
                                   command=self.voltar)
        self.voltar.place(x=1044, y=99)

    # PROBLEMA DE LOOPING :')
    def voltar(self):
        self.frametop.destroy()  # Destroi a janela sobre
        self.frameju.destroy()
        self.titulo.destroy()
        self.retangulo_roxo1.destroy()
        self.retangulo_roxo2.destroy()
        self.nomeju.destroy()
        self.nomevini.destroy()
        self.infoju.destroy()
        self.infovini.destroy()
        self.github01.destroy()
        self.github02.destroy()
        self.github11.destroy()
        self.github12.destroy()
        self.framevini.destroy()
        self.data.destroy()
        self.dadostexto.destroy()
        self.voltar.destroy()