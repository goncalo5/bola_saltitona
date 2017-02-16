from Tkinter import *
from constantes import *


class Game(object):
    def __init__(self):
        self.i = Tk()
        self.i.title('Bola Saltitona')
        self.i.geometry('%ix%i' % (L_TELA, H_TELA))
        self.i.configure(bg=COR_DO_FUNDO)

        self.canvas = Canvas(self.i, width=L_TELA, height=H_TELA)
        self.canvas.focus_force()
        self.canvas.pack()
        self.canvas.bind('<Key>', self.movimentar)

        self.x = 10
        self.y = H_TELA - CAMPO[0] * TAM_BLOCO - DIAM

        self.criar_campo()
        self.vy = 0
        self.parado = True
        self.criar_bola()
        self.cair()

        self.i.mainloop()

    def movimentar(self, event):
        print event.keysym
        if event.keysym == 'Up' and self.parado:
            self.canvas.move('bola', 0, -SALTO)
            self.y -= SALTO
        if event.keysym == 'Right':
            if CAMPO[(self.x + DIR) / TAM_BLOCO] <= (H_TELA - self.y) / TAM_BLOCO:
                self.x += DIR
                self.canvas.move('bola', DIR, 0)
        if event.keysym == 'Left':
            if CAMPO[(self.x - ESQ) / TAM_BLOCO] <= (H_TELA - self.y) / TAM_BLOCO:
                self.x -= ESQ
                self.canvas.move('bola', -ESQ, 0)


    def cair(self):
        self.canvas.move('bola', 0, self.vy)
        self.y += self.vy
        print 'x', self.x, 'y', self.y, 'vy', self.vy
        if (H_TELA - self.y) > CAMPO[int(self.x / TAM_BLOCO)] * TAM_BLOCO + DIAM:
            self.vy = PESO
            self.parado = False
        else:
            self.vy = 0
            self.parado = True
        if self.y >= H_TELA - DIAM:
            self.i.destroy()
        self.i.after(1000, self.cair)

    def criar_campo(self):
        x0 = 0
        for c in CAMPO:
            y0 = H_TELA - c * TAM_BLOCO
            x = x0 + TAM_BLOCO
            self.canvas.create_rectangle(
                x0, y0, x, H_TELA, fill=COR_CAMPO, outline='')
            x0 = x

    def criar_bola(self):
        self.canvas.create_oval(self.x, self.y, self.x + DIAM, self.y + DIAM,
                                fill=COR_BOLA, tag='bola')


if __name__ == '__main__':
    Game()
