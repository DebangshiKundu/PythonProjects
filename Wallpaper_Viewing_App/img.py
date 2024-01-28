import tkinter as tk
from PIL import ImageTk, Image

def show(index):
    img = img_list[index]
    canvas.itemconfig(img_item, image=img)
    window.geometry(f"{img.width()}x{img.height()}") 

def next():
    global index
    index = (index + 1) % len(img_list)
    show(index)

def prev():
    global index
    index = (index - 1) % len(img_list)
    show(index)

window = tk.Tk()
window.title('Wallpaper Viewing App')
index = 0

img1 = ImageTk.PhotoImage(Image.open('/Users/debangshi/Downloads/jack-anstey-XVoyX7l9ocY.png').resize((1400, 750)))
img2 = ImageTk.PhotoImage(Image.open('/Users/debangshi/Downloads/jmsdono-0ZBRKEG_5no.jpg').resize((1400, 750)))
img3 = ImageTk.PhotoImage(Image.open('/Users/debangshi/Downloads/frank-mckenna-OD9EOzfSOh0.jpg').resize((1400, 750)))
img4 = ImageTk.PhotoImage(Image.open('/Users/debangshi/Downloads/zhao-chen-B1KzVJ8aNkw.jpg').resize((1400, 750)))
img5 = ImageTk.PhotoImage(Image.open('/Users/debangshi/Downloads/cristina-gottardi--YzMZYqwoH4.jpg').resize((1400, 750)))

img_list = [img1, img2, img3, img4, img5]

canvas = tk.Canvas(window)
canvas.pack(expand=True, fill='both')

img_item = canvas.create_image(0, 0, anchor='nw', image=img1)

button_frame = tk.Frame(window)
button_frame.pack()

button_prev = tk.Button(button_frame, text='<<', command=prev)
button_exit = tk.Button(button_frame, text='Exit', command=window.quit)
button_next = tk.Button(button_frame, text='>>', command=next)

button_prev.grid(row=0, column=0, sticky='nsew')
button_exit.grid(row=0, column=1, sticky='nsew')
button_next.grid(row=0, column=2, sticky='nsew')

window.geometry(f"{img1.width()}x{img1.height()}")

window.mainloop()
