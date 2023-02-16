from tkinter import *
from PIL import Image, ImageTk

FILENAME = "images.jpg" # файл с графическим изображением

root = Tk()
# # создаем рабочую область 1
frame1 = Frame(root, width=400, height=500, bg="red")
frame1.grid(row=0, column=1)
# # создаем рабочую область 2
frame2 = Frame(root, width=400, height=500, bg="green")
frame2.grid(row=0, column=2)

but = Button(frame1, text="Кнопка").place(x=10, y=10)

c = Canvas(frame2, width=128, height=128)

src_img = Image.open(FILENAME)

img1 = PhotoImage(src_img)
img2 = img1.subsample(2, 2)

c.create_image(0, 0, image=img2, anchor="center")

c.place(x=10, y=10)

Label(frame2, text=FILENAME).place(x=10, y=10)

root.mainloop()