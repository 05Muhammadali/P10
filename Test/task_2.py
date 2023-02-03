from tkinter import *

from googletrans import Translator


def func():
    text = text_1.get('1.0', END)
    a = translator.translate(text, dest='uz')
    text_2.delete('1.0', END)
    text_2.insert('1.0', a.text)


root = Tk()
root.geometry("600x600")
root.title('Translator')
root['bg'] = 'black'

translator = Translator()

label = Label(root, fg='white', bg="black", text='Enter your word')
label.place(relx=0.5, y=30, anchor=CENTER)

text_1 = Text(root, width=35, height=5)
text_1.place(relx=0.5, y=100, anchor=CENTER)

btn = Button(root, width=45, text='Translate', command=func)
btn.place(relx=0.5, y=180, anchor=CENTER)

text_2 = Text(root, width=35, height=5)
text_2.place(relx=0.5, y=260, anchor=CENTER)

root.mainloop()
