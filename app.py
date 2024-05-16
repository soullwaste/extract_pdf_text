import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# logo
#this is opening and setting the logo to the variable logo
logo = Image.open('./img/logo.png')
# making the image a tkinter image
logo = ImageTk.PhotoImage(logo)
#this is actually putting it in the app in a specific grid
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instruction
instructions = tk.Label(root, text="Select a pdf file to extract all of its text")
instructions.grid(columnspan=3, column=0, row=1)

def openFile():
    browse_text.set("Loading...")
    file = askopenfile(parent=root, 
                       mode='rb', 
                       title='choose a file', 
                       filetypes=[("pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfReader(file)
        page = read_pdf.pages[0]
        page_content = page.extract_text()
        print(page_content)
    #text box
    text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
    text_box.insert(1.0, page_content)
    #centering what shows in the text box
    text_box.tag_configure("center", justify="center")
    text_box.tag_add('center', 1.0, "end")
    text_box.grid(column=1, row=3)

    browse_text.set('browse')

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, 
                       textvariable=browse_text, 
                       bg="#20bebe", 
                       fg='white',
                       height=2, width=15,
                       command=lambda:openFile())
browse_text.set('Browse')
browse_btn.grid(column=1, row=2)





root.mainloop()