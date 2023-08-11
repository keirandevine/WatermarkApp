import tkinter
from tkinter import filedialog
from PIL import Image, ImageTk
from water_marker import WaterMarker
from flask import send_file



#___________________________________________Tkinter Window Set Up____________________________________________#
window = tkinter.Tk()
window.title('Watermark App')
window.minsize(width=350, height=500)

window.grid_columnconfigure(0, weight=3)
window.grid_columnconfigure(1, weight=3)
window.grid_columnconfigure(2, weight=3)
window.grid_columnconfigure(3, weight=3)
window.grid_columnconfigure(4, weight=3)


#______________________________________Constants

#______________________________________Definition of Functions________________________________________________#

marker = WaterMarker()
var = tkinter.IntVar()



def upload_img():
    global original_img
    uploaded_file = filedialog.askopenfilename()
    pil_img = Image.open(uploaded_file)
    pil_img.save("base_img.png", "PNG")
    img_resized = pil_img.resize((150, 150))
    original_img = ImageTk.PhotoImage(img_resized)
    canvas.create_image(5, 80, image=original_img, anchor='w')


def choose_wtr_mark():
    global watermarked_img_display
    radio_value = var.get()
    marker.mark_img(radio_value=radio_value, base_img="base_img.png")
    wtrmarked_img = Image.open("watermarked_img.png")
    img_resized = wtrmarked_img.resize((150, 150))
    watermarked_img_display = ImageTk.PhotoImage(img_resized)
    canvas.create_image(315, 80, image=watermarked_img_display, anchor='e')


def download_img():
    watermarked_img = Image.open("watermarked_img.png")
    output_path = r"C:\Users\profe\Desktop\watermarked_img.png"
    watermarked_img.save(output_path)
    msg = tkinter.Message(window, text="The watermarked image has been saved to your desktop")
    msg.grid(row=11, column=1)












#_______________________________________Window Heading / Initial Prompt________________________________________#
heading_label = tkinter.Label(text="WaterMark Whiz")
heading_label.config(font=('Arial', 30, 'bold'))
heading_label.grid(row=0, column=1)

prompt = tkinter.Label(text="Upload your chosen image to get started")
prompt.config(font=('Georgia', 16, 'normal'), pady=10)
prompt.grid(row=1, column=1)

button = tkinter.Button(text="Upload", command=upload_img)
button.grid(row=2, column=1, sticky='n', pady=10)


#_________________________________WaterMark Choice Radiobutton / Main Prompt__________________________________#

choice_label = tkinter.Label(text="Choose your watermark")
choice_label.config(font=('Georgia', 10, 'bold'))
choice_label.grid(row=3, column=1, pady=5)


R1 = tkinter.Radiobutton(window, text="Option 1", variable=var, value=1, command=choose_wtr_mark)
R2 = tkinter.Radiobutton(window, text="Option 2", variable=var, value=2, command=choose_wtr_mark)
R3 = tkinter.Radiobutton(window, text="Option 3", variable=var, value=3, command=choose_wtr_mark)

R1.grid(row=4, column=1)
R2.grid(row=5, column=1)
R3.grid(row=6, column=1)


# go_button = tkinter.Button(text="Go!")
# go_button.grid(row=7, column=1)


#__________________________________Display Images / Image Download Button_______________________________________#

image_labels = tkinter.Label(text="            Original Image                 Watermarked Image     ")
image_labels.config(padx=50, pady=5, font=('Georgia', 10, 'underline'))
image_labels.grid(row=8, column=1)

original_img = tkinter.PhotoImage(file="placeholder.png")
watermarked_img_display = tkinter.PhotoImage(file="placeholder.png")
canvas = tkinter.Canvas(width=320, height=160, bg='beige', highlightthickness=0)
canvas.create_image(5, 80, image=original_img, anchor='w')
canvas.create_image(315, 80, image=watermarked_img_display, anchor='e')
canvas.grid(row=9, column=1)

download_btn = tkinter.Button(text="Download", command=download_img)
download_btn.grid(row=10, column=1)




window.mainloop()