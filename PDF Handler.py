import tkinter as tk
import os
import re
from tkinter import filedialog
from tkinter.ttk import *
from tkinter import *
from tkinter.filedialog import askopenfile, askopenfilename, askopenfilenames
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from fpdf import FPDF
from PIL import ImageTk, Image

file1 = 'Not selected'
file2 = 'Not selected'
file3 = 'Not selected'



class MyWindow:
    def __init__(self, win):
        menubar = Menu()
        window.config(menu=menubar)
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='New Job', command=lambda: clear_globals())
        file_menu.add_command(label='Open Files', command=lambda: open_files())
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=window.destroy)

        edit = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Edit', menu=edit)
        edit.add_command(label='Append pages', command=lambda: Edit.open_win_E1())
        edit.add_command(label='Edit images', command=None)
        edit.add_command(label='Edit text', command=None)

        help_ = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Help', menu=help_)
        help_.add_command(label='Simple PDF Handler Help', command=lambda: open_win_H1())
        help_.add_separator()
        help_.add_command(label='About', command=lambda: open_win_H2())

        self.lbl1 = Label(win, text="Quick tasks", font=('Helvetica 14 bold'))
        self.lbl1.place(x=10, y=10)
        self.btn2 = Button(win, text='Convert images to PDF')
        self.btn3 = Button(win, text='Browse File Directory')
        self.btn4 = Button(win, text='Reduce file size')
        self.btn6 = Button(win, text='Merge Selected PDFs')

        self.b2 = Button(win, width=20, text='Convert images to PDF', command=lambda: convert_img_to_pdf())
        # self.b2.bind('<Button-1>', self.sub)
        self.b3 = Button(win, text='Select Output Folder', command=lambda: working_folder())
        self.b4 = Button(win, width=20, text='Reduce file size', command=lambda: reduce_pdf_size())
        self.b6 = Button(win, width=20, text='Merge Selected PDFs', command=lambda: merge_pdfs())

        self.b2.place(x=10, y=150)
        self.b3.place(x=450, y=350)
        self.b4.place(x=10, y=100)
        self.b6.place(x=10, y=50)
        frame = Frame(win, width=60, height=40)
        frame.pack()
        frame.place(x=200, y=100)

        # Create an object of tkinter ImageTk
        #img = ImageTk.PhotoImage(Image.open(r'C:\Users\msste\OneDrive\Coding\DA\1.jpg'))
        # Create a Label Widget to display the text or Image
        #label = Label(frame, image=img)
        #label.pack()


def clear_globals():
    global file1
    global file2
    global file3
    global filenames
    file1 = [], file2 = [], file3 = [], filenames = []

class Edit:
    def open_win_E1(self=None):
        global E1
        E1 = tk.Toplevel(window)
        E1.geometry("750x450")
        E1.title("Merge and append pages from PDF")
        E1.iconbitmap(r"C:\Users\msste\PycharmProjects\pythonProject\Simple PDF Handler.ico")


        head1, tail1 = os.path.split(file1)
        head2, tail2 = os.path.split(file2)
        head3, tail3 = os.path.split(file3)
        data = ("'" + tail1 + "'", "'" + tail2 + "'", "'" + tail3 + "'")

        lb = Listbox(E1, height=3, width=40, selectmode='multiple')
        for num in data:
            lb.insert(END, num)
            lb.place(x=50, y=50)

        op1 = tk.Button(E1, text='Select 1st File', command=lambda: open_file1())
        op1.place(x=150, y=350)
        op2 = tk.Button(E1, text='Select 2nd File', command=lambda: open_file2())
        op2.place(x=350, y=350)
        op3 = tk.Button(E1, text='Select 3rd File', command=lambda: open_file3())
        op3.place(x=550, y=350)
        ap = tk.Button(E1, text='Append all', command=lambda: append_pages_pdf())
        ap.place(x=350, y=50)
        #page_entry(self, E1)


        lbl1 = Label(E1, text='Select pages')
        lbl2 = Label(E1, text='All pages')
        lbl3 = Label(E1, text='Insert after page')
        lbl1.place(x=10, y=250)
        lbl2.place(x=10, y=280)
        lbl3.place(x=10, y=200)
        global v0
        v0 = IntVar(value=2)
        r1 = Radiobutton(E1, variable=v0, value=1, command=lambda: Edit.naccheck())
        r1.place(x=100, y=250)
        r2 = Radiobutton(E1, variable=v0, value=2, command=lambda: Edit.naccheck())
        r2.place(x=100, y=280)
        global t1, t2, t3, t5, t6
        t1 = Entry(E1, bd=3)
        t1.place(x=130, y=250)
        t2 = Entry(E1, bd=3)
        t2.place(x=330, y=250)
        t3 = Entry(E1, bd=3)
        t3.place(x=530, y=250)
        # t4=Entry(new, bd=3)
        # t4.place(x=130, y=200)
        t5 = Entry(E1, bd=3)
        t5.place(x=330, y=200)
        t6 = Entry(E1, bd=3)
        t6.place(x=530, y=200)
        Edit.naccheck()

        t1.bind("<KeyRelease>", Edit.t1_entry)
        t2.bind("<KeyRelease>", Edit.t2_entry)
        t3.bind("<KeyRelease>", Edit.t3_entry)
        t5.bind("<KeyRelease>", Edit.t5_entry)
        t6.bind("<KeyRelease>", Edit.t6_entry)
        #get = tk.Button(E1, text='get', command=None)
        #get.place(x=310, y=80)
        #get.bind("<Button-1>", Edit.key)


    def t1_entry(event):
        global pages_f1
        pages_f1 = int(t1.get())-1
        print(pages_f1)


    def t2_entry(event):
        global pages_f2
        pages_f2 = int(t2.get())-1
        print(pages_f2)

    def t3_entry(event):
        global pages_f3
        pages_f3 = int(t3.get())-1
        print(pages_f3)

    def t5_entry(event):
        global position_f2
        position_f2 = int(t5.get())-1
        print(position_f2)

    def t6_entry(event):
        global position_f3
        position_f3= int(t6.get())-1
        print(position_f3)


    def naccheck(self=None):
        if v0.get() == 2:
           t1.configure(state='disabled')
        else:
           t1.configure(state='normal')


def refresh():
    E1.destroy()
    Edit.open_win_E1()


def open_win_H1():
    H1 = tk.Toplevel(window)
    H1.geometry("570x400")
    H1.title("Simple PDF Handler Help")
    H1.iconbitmap(r"C:\Users\msste\PycharmProjects\pythonProject\Simple PDF Handler.ico")
    help_topics = '''
                  Help Topics:
                  1. Quick tasks on Main Window:
                  1.1 Merge Selected PDFs
                  1.2 Reduce File size
                  1.3 Convert images to pdf
                  All task are self-explanatory. 
                  To run each task, the source files and an output folder should be selected.
                  
                  2. File Menu Tasks:
                  2.1 New job can be called to clear all inputs
                  2.2 Open files menu item is used to browse for files 
                  2.3 Exit command will close the program
                  
                  3. Edit Menu Tasks:
                  3.1 Append Pages feature allows to combine pages from three different PDF files
                  A separate window contains files selection and page entry data fields.
                  Note: pages should be entered in the following format: e.g., [1, 3 ]
                  3.2 Edit Images
                  A separate window for image editing (under development)
                  3.3 Edit Text
                   A separate window for text editing (under development)
                   
                  '''
    help_topics = re.sub("\n\s*", "\n", help_topics)  # remove leading whitespace from each line
    h = CustomText(H1, wrap="word", width=100, height=10, borderwidth=0)
    h.tag_configure("blue", foreground="blue")
    h.pack(sid="top", fill="both", expand=True)
    h.insert("1.0", help_topics)
    h.HighlightPattern("^.*? - ", "blue")
    tk.Button(H1, text='OK', command=H1.destroy).pack()


def open_win_H2():
    H2 = tk.Toplevel(window)
    H2.geometry("250x100")
    H2.title("About Simple PDF Handler")
    H2.iconbitmap(r"C:\Users\msste\PycharmProjects\pythonProject\Simple PDF Handler.ico")
    about = '''
           Simple PDF Handler
           Program version: 1.2.0
           Author: Maksym Stetsenko
           '''
    about = re.sub("\n\s*", "\n", about)  # remove leading whitespace from each line
    t = CustomText(H2, wrap="word", width=100, height=10, borderwidth=0)
    t.tag_configure("blue", foreground="blue")
    t.pack(sid="top", fill="both", expand=True)
    t.insert("1.0", about)
    t.HighlightPattern("^.*? - ", "blue")
    tk.Button(H2, text='OK', command=H2.destroy).pack()


def working_folder():
    global folder_path
    folder_path = filedialog.askdirectory()


def open_file1():
    global file1
    file1 = askopenfilename(filetypes=[('PDF Files', '*.pdf'), ('all files', '*.*')])
    refresh()


def open_file2():
    global file2
    file2 = askopenfilename(filetypes=[('PDF Files', '*.pdf'), ('all files', '*.*')])
    refresh()


def open_file3():
    global file3
    file3 = askopenfilename(filetypes=[('PDF Files', '*.pdf'), ('all files', '*.*')])
    refresh()


def open_files():
    files = askopenfilenames(
        filetypes=[('PDF Files', '*.pdf'), ('Image Files', '*.png'), ('Image Files', '*.jpg'), ('Image Files', '*.bmp'),
                   ('all files', '*.*')])
    global filenames
    filenames = files


def convert_img_to_pdf():
    img_pdf = FPDF()

    for i in filenames:
        img_pdf.add_page()
        img_pdf.image(i)

    img_pdf.output(folder_path + '/converted.pdf', 'F')


def reduce_pdf_size():
    reader = PdfReader(filenames)
    writer = PdfWriter()
    for page in reader.pages:
        page.compress_content_streams()  # This is CPU intensive!
        writer.add_page(page)
    with open(folder_path + "/reduced size.pdf", "wb") as f:
        writer.write(f)


def merge_pdfs():
    merger = PdfMerger()
    for pdf in filenames:
        merger.append(pdf)
    merger.write(folder_path + "/Merged.pdf")
    merger.close()


def append_pages_pdf():
    merger = PdfMerger()
    reader1 = open(file1, "rb")
    reader2 = open(file2, "rb")
    input1 = PdfReader(reader1)
    input2 = PdfReader(reader2)

    if v0.get() == 2:
       merger.append(fileobj=input1, pages = [0, (len(input1.pages)-1), 1])
    else:
        merger.append(fileobj=input1, pages=[pages_f1])
    merger.merge(position=position_f2, fileobj=input2, pages=[pages_f2])
    if file3 == 'Not selected':
       pass
    else:
        input3 = open(file3, "rb")
        merger.merge(position=position_f3, fileobj=input3, pages=[pages_f3])
    output = open(folder_path + "/merged.pdf", "wb") # Write to an output PDF document
    merger.write(output)
    # Close File Descriptors
    merger.close()
    output.close()

class CustomText(tk.Text):
    '''A text widget with a new method, HighlightPattern

    example:

    text = CustomText()
    text.tag_configure("red",foreground="#ff0000")
    text.HighlightPattern("this should be red", "red")

    The HighlightPattern method is a simplified python
    version of the tcl code at http://wiki.tcl.tk/3246
    '''
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

    def HighlightPattern(self, pattern, tag, start="1.0", end="end", regexp=True):
        '''Apply the given tag to all text that matches the given pattern'''

        start = self.index(start)
        end = self.index(end)
        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", end)
        self.mark_set("searchLimit", end)

        count = tk.IntVar()
        while True:
            index = self.search(pattern, "matchEnd", "searchLimit", count=count, regexp=regexp)
            if index == "": break
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.tag_add(tag, "matchStart", "matchEnd")

window = tk.Tk()
mywin = MyWindow(window)
window.title('Simple PDF Handler')
window.geometry("600x400+10+10")
window.iconbitmap(r"C:\Users\msste\PycharmProjects\pythonProject\Simple PDF Handler.ico")

window.mainloop()
