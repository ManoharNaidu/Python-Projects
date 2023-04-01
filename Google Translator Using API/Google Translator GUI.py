from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox

root = tk.Tk()
root.title("Language Translator")
root.geometry("590x370")


def translate():
    Lang1 = Text_Entry1.get("1.0","end-1c")
    CL = Choose_Language.get()

    if Lang1 == '': #checking error, if the checkbox is empty and try to translate
        messagebox.showerror("Google Tranlator","Enter the text to translate!")
    else:
        Text_Entry2.delete(1.0,'end')
        translator = Translator()
        output = translator.translate(Lang1,dest=CL)
        Text_Entry2.insert("end",output.text)

def clear():
    Text_Entry1.delete(1.0,"end")
    Text_Entry2.delete(1.0,"end")

a = tk.StringVar()

Frame1 = Frame(root,width=590,height=370,relief = RIDGE,borderwidth=5,bg="#eab676")
Frame1.place(x=0,y=0)

AutoSelect = ttk.Combobox(Frame1,width=27,textvariable=a,state='randomly',font=('verdana',10,"bold"))
AutoSelect['values'] = ('Auto Select',)

AutoSelect.place(x=15,y=60)
AutoSelect.current(0)

L = tk.StringVar()
Choose_Language = ttk.Combobox(Frame1,width=27,textvariable=L,state='randomly',font=('verdana',10,"bold"))
Choose_Language['values'] = ("Afrikaans",
    "Albanian",
    "Amharic",
    "Arabic",
    "Armenian",
    "Azerbaijani",
    "Basque",
    "Belarusian",
    "Bengali",
    "Bosnian",
    'Bulgarian',
    "Catalan",
    "Cebuano",
    "Chichewa",
    "Chinese (simplified)",
    "Chinese (traditional)",
    "Corsican",
    "Croatian",
    "Czech",
    "Danish",
    "Dutch",
    "English",
    "Esperanto",
    "Estonian",
    "Filipino",
    "Finnish",
    "French",
    "Frisian",
    "Galician",
    "Georgian",
    "German",
    "Greek",
    "Gujarati",
    "Haitian creole",
    "Hausa",
    "Hawaiian",
    "Hebrew",
    "Hebrew",
    "Hindi",
    "Hmong",
    "Hungarian",
    "Icelandic",
    "Igbo",
    "Indonesian",
    "Irish",
    "Italian",
    "Japanese",
    "Javanese",
    "Kannada",
    "Kazakh",
    "Khmer",
    "Korean",
    "Kurdish (kurmanji)",
    "Kyrgyz",
    "Lao",
    "Latin",
    "Latvian",
    "Lithuanian",
    "Luxembourgish",
    "Macedonian",
    "Malagasy",
    "Malay",
    "Malayalam",
    "Maltese",
    "Maori",
    "Marathi",
    "Mongolian",
    "Myanmar (burmese)",
    "Nepali",
    "Norwegian",
    "Odia",
    "Pashto",
    "Persian",
    "Polish",
    "Portuguese",
    "Punjabi",
    "Romanian",
    "Russian",
    "Samoan",
    "Scots gaelic",
    "Serbian",
    "Sesotho",
    "Shona",
    "Sindhi",
    "Sinhala",
    "Slovak",
    "Slovenian",
    "Somali",
    "Spanish",
    "Sundanese",
    "Swahili",
    "Swedish",
    "Tajik",
    "Tamil",
    "Telugu",
    "Thai",
    "Turkish",
    "Ukrainian",
    "Urdu",
    "Uyghur",
    "Uzbek",
    "Vietnamese",
    "Welsh",
    "Xhosa",
    "Yiddish",
    "Yoruba",
    "Zulu"
                             )
Choose_Language.place(x=305,y=60)
Choose_Language.current(0)




Label(root,text="Google Translator",font = ("Helvetica 20 bold"),fg="black",bg="#eab676").pack(pady=10)

Text_Entry1 = Text(Frame1,width=20,height=7,borderwidth=5,relief = RIDGE,font = ('verdana',15) )
Text_Entry1.place(x=10,y=100)

Text_Entry2 = Text(Frame1,width=20,height=7,borderwidth=5,relief = RIDGE,font = ('verdana',15) )
Text_Entry2.place(x=300,y=100)

Btn1 = Button(Frame1,command=translate,text="Translate", relief = RAISED,font =('verdana',10,'bold'),bg="#063970",fg="white",cursor = "hand2")
Btn1.place(x=185,y=300)

Btn2 = Button(Frame1,command=clear,text="Clear", relief = RAISED,font =('verdana',10,'bold'),bg="#063970",fg="white",cursor = "hand2")
Btn2.place(x=300,y=300)


root.mainloop()