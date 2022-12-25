from tkinter import *

class Menu0:

    def __init__(self):

        self.window = Tk()
        self.window.geometry("1304x926")
        self.window.configure(bg = "#ffffff")
        self.canvas = Canvas(
            self.window,
            bg = "#ffffff",
            height = 926,
            width = 1304,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"backgroundMenu0.png")
        self.background = self.canvas.create_image(
            661.0, 582.0,
            image=self.background_img)

        self.img0 = PhotoImage(file = f"img0Menu0.png")
        self.b0 = Button(
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btn_clicked,
            relief = "flat")

        self.b0.place(
            x = 447, y = 207,
            width = 422,
            height = 150)

        self.window.resizable(False, False)
        self.window.mainloop()

    def btn_clicked(self):
        print("Button Clicked")

eso = Menu0()