import math
import tkinter as tk
from datetime import datetime
import time

window = tk.Tk()
window.title('Clock')
window.geometry('800x800')
window.config(bg='black')

# frame=tk.Frame(window, bg='black')
# frame.pack(pady=2)
# frame.pack_propagate(False)
# frame.config(width=800,height=45)

# clock_btn=tk.Button(frame, text='Clock', font=('Times New Roman',30),highlightbackground='black')
# clock_btn.pack(side='left', fill='both', expand=True)

# alarm_btn=tk.Button(frame, text='Alarm', font=('Times New Roman',30),highlightbackground='black')
# alarm_btn.pack(side='left', fill='both', expand=True)

# timer_btn=tk.Button(frame, text='Timer', font=('Times New Roman',30),highlightbackground='black')
# timer_btn.pack(side='left', fill='both', expand=True)

# sw_btn=tk.Button(frame, text='Stopwatch', font=('Times New Roman',30),highlightbackground='black')
# sw_btn.pack(side='left', fill='both', expand=True)


def update_time():
    current_time = datetime.now().strftime("    %H:%M:%S    ")
    label.config(text=current_time,bg='black')
    window.after(1000, update_time)


label = tk.Label(window, font=('Courier New', 100))
label.pack(padx=75, pady=75)

canvas = tk.Canvas(window, width=200, height=400,bg='black')
canvas.pack(expand=True, fill='both')

bg = tk.PhotoImage(file='pythonProject/clock/clockimg.png')

canvas.create_image(390, 250, image=bg)

# clock hands
x_centre=390
y_centre=250
sec_len=150
min_len=130
hr_len=80

#drawing hands
sec_hand=canvas.create_line(390,250,390+sec_len,250+sec_len,width=1,fill='red')
min_hand=canvas.create_line(390,250,390+min_len,250+min_len,width=2,fill='white')
hr_hand=canvas.create_line(390,250,390+hr_len,250+hr_len,width=4,fill='white')

def clock_update():
    hr=int(time.strftime('%I'))
    min=float(time.strftime('%M'))
    sec=float(time.strftime('%S'))

    # for seconds
    seconds_x=sec_len*math.sin(math.radians(sec*6))+x_centre
    seconds_y=-1*sec_len*math.cos(math.radians(sec*6))+y_centre
    canvas.coords(sec_hand,x_centre,y_centre,seconds_x,seconds_y)

    # for minutes
    min_x=min_len*math.sin(math.radians(min*6))+x_centre
    min_y=-1*min_len*math.cos(math.radians(min*6))+y_centre
    canvas.coords(min_hand,x_centre,y_centre,min_x,min_y)

    # for hours
    hr_x=hr_len*math.sin(math.radians(hr*30))+x_centre
    hr_y=-1*hr_len*math.cos(math.radians(hr*30))+y_centre
    canvas.coords(hr_hand,x_centre,y_centre,hr_x,hr_y)

    window.after(1000,clock_update)

clock_update()
update_time()
window.mainloop()
























