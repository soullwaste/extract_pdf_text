import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# logo
#this is opening and setting the logo to the variable logo
logo = Image.open('./img/logo.png')
logo = ImageTk.PhotoImage(logo)
#this is actually putting it in the app in a specific grid
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instruction
instructions = tk.Label(root, text="Select a pdf file on your computer to extract all of its text")
instructions.grid(columnspan=3, column=0, row=1)

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, 
                       textvariable=browse_text, 
                       bg="#20bebe", 
                       fg='white',
                       height=2, width=15)
browse_text.set('Browse')
browse_btn.grid(column=1, row=2)





root.mainloop()