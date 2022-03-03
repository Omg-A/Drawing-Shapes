from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Drawing Lines On A Canvas")
root.geometry("900x600")

#Making Canvas
canvas = Canvas(root, width=890, height=490, bg="white", highlightbackground="lightgray")
canvas.pack()

#Label for dropdown
label_color = Label(root, text="Enter Color")
label_color.place(relx=0.6, rely=0.9, anchor=CENTER)

#Dropdown for color
fill_color = ["black", "red", "blue", "yellow", "green"]
dropdown = ttk.Combobox(root, state="readonly", values=fill_color, width=10)
dropdown.place(relx=0.8, rely=0.9, anchor=CENTER)


#StartX
label_startx = Label(root, text="StartX")
label_startx.place(relx=0.1, rely=0.85, anchor=CENTER)

startx_num = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900]
dropdown_startx = ttk.Combobox(root, state="readonly", values=startx_num, width=10)
dropdown_startx.place(relx=0.2, rely=0.85, anchor=CENTER)

#StartY
label_starty = Label(root, text="StartY")
label_starty.place(relx=0.3, rely=0.85, anchor=CENTER)

starty_num = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900]
dropdown_starty = ttk.Combobox(root, state="readonly", values=starty_num, width=10)
dropdown_starty.place(relx=0.4, rely=0.85, anchor=CENTER)

#EndX
label_endx = Label(root, text="EndX")
label_endx.place(relx=0.5, rely=0.85, anchor=CENTER)

endx_num = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900]
dropdown_endx = ttk.Combobox(root, state="readonly", values=endx_num, width=10)
dropdown_endx.place(relx=0.6, rely=0.85, anchor=CENTER)

#EndY
label_endy = Label(root, text="EndY")
label_endy.place(relx=0.7, rely=0.85, anchor=CENTER)

endy_num = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900]
dropdown_endy = ttk.Combobox(root, state="readonly", values=endy_num, width=10)
dropdown_endy.place(relx=0.8, rely=0.85, anchor=CENTER)

def draw(keypress, oldx, oldy, newx, newy):
    fill_color = dropdown.get()
    
    if(keypress == "c"):
        draw_circle = canvas.create_oval(oldx, oldy, newx, newy, fill=fill_color)
        print(fill_color + " Circle")
    if(keypress == "r"):
        draw_rect = canvas.create_rectangle(oldx, oldy, newx, newy, fill=fill_color)
        print(fill_color + " Rectangle")
    if(keypress == "l"):
        draw_line = canvas.create_line(oldx, oldy, newx, newy, width=3, fill=fill_color)
        print(fill_color + " Line")
        
def circle(event):
    print("circle")
    oldx = dropdown_startx.get()
    oldy = dropdown_starty.get()
    newx = dropdown_endx.get()
    newy = dropdown_endy.get()
    keypress = "c"
    draw(keypress, oldx, oldy, newx, newy)

def rectangle(event):
    print("rectangle")
    oldx = dropdown_startx.get()
    oldy = dropdown_starty.get()
    newx = dropdown_endx.get()
    newy = dropdown_endy.get()
    keypress = "r"
    draw(keypress, oldx, oldy, newx, newy)

def line(event):
    print("line")
    oldx = dropdown_startx.get()
    oldy = dropdown_starty.get()
    newx = dropdown_endx.get()
    newy = dropdown_endy.get()
    keypress = "l"
    draw(keypress, oldx, oldy, newx, newy)
 
root.bind("<c>", circle)
root.bind("<r>", rectangle)
root.bind("<l>", line)

root.mainloop()