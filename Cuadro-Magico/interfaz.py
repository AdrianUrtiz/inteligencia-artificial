import tkinter as tk

from Nodo import Nodo, Tablero

moves = [
    [[1, 3]],
    [[0, 2, 4]],
    [[1, 5]],
    [[0, 4, 6], [1, 3, 5, 7], [2, 4, 8]],
    [[3, 7], [4, 6, 8], [5, 7]],
]


class App(tk.Tk):
    def __init__(self, *args, **kargs):
        tk.Tk.__init__(self, *args, **kargs)
        self.title("Cuadro Mágico")
        self.geometry("650x800")
        self.container = tk.Frame(self, bg="red")
        self.container.place(relx=0, rely=0, relwidth=1, relheight=1)
        fTab = Frame_Tablero(self.container, self)
        fTab.tkraise()


class Ficha:
    contador = 0

    def __init__(self, r, c, n, frame):
        self.frame = frame
        self.r = r
        self.c = c
        self.n = n
        self.contador = Ficha.contador
        Ficha.contador += 1
        if n != 0:
            self.button = tk.Button(
                self.frame,
                text=str(n),
                font=("Impact", 100),
                command=lambda: frame.move(self.contador, self.r, self.c),
            )
        else:
            self.button = tk.Button(
                self.frame,
                text="",
                font=("Impact", 100),
                command=lambda: frame.move(self.contador, self.r, self.c),
            )
        self.button.place(
            relx=1 / 26 + c * (4 / 13),
            rely=0.05 + self.r * (1 / 4),
            relwidth=4 / 13,
            relheight=1 / 4,
        )


class Frame_Tablero(tk.Frame):
    def __init__(self, parent, root):
        self.root = root
        tk.Frame.__init__(self, parent, bg="black")
        self.place(relx=0, rely=0, relwidth=1, relheight=1)
        b_solve = tk.Button(
            self,
            text="Resolver",
            command=lambda: self.solve(),
            background="black",
            fg="white",
            padx=10,
            pady=5,
        )
        b_solve.place(relx=0.3, rely=0.85, relwidth=0.4, relheight=0.1)
        self.nums = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.aux_tablero = Tablero(self.nums)

        self.fichas = []
        for ir, r in enumerate(self.nums):
            for ic, c in enumerate(r):
                aux = Ficha(ir, ic, c, self)
                self.fichas.append(aux)

    def move(self, icontador, fr, fc):
        er, ec = self.aux_tablero.empty()
        if icontador in moves[er][ec]:
            if er == fr:
                if fc < ec:
                    auxm = "l"
                else:
                    auxm = "r"
            else:
                if fr < er:
                    auxm = "u"
                else:
                    auxm = "d"

            self.aux_tablero.makeMove(auxm)
            self.actualizar(self.aux_tablero.nums)

    def actualizar(self, nums):
        aux = 0
        for ir, r in enumerate(nums):
            for ic, c in enumerate(r):
                if c != 0:
                    self.fichas[aux].button.config(
                        text=str(c),
                        background="black",
                        fg="white",
                        border=10,
                        relief="raised",
                    )
                else:
                    self.fichas[aux].button.config(
                        text="",
                        background="white",
                        bd=5,
                        highlightcolor="white",
                        borderwidth=5,
                    )
                aux += 1


if __name__ == "__main__":
    app = App()
    app.mainloop()
