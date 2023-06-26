from tkinter import *
from tkinter import ttk
converter = Tk()
converter.geometry("600x400")

converter.title("CURRENCY CONVERTER")

OPTIONS ={
    "Australian Dollar": 54.69,
    "Argentine peso": 0.40,
    "British Pound": 100.70,
    "Brezilean Real": 15.511,
    "Canadian Dollar": 59.59,
    "Chinese yuan": 11.99,
    "Danish krone": 11.88,
    "Euro": 88.53,
    "Hong Kong Dollar": 10.50,
    "Indonatian Rupiah": 0.004,
    "Iranian Rial": 0.0019,
    "Japaneese Yen": 0.63,
    "Kuwaiti Dinar": 17.21,
    "Malasian Riggit": 18.6,
    "Mexican peso": 4.40,
    "Nepalese Rupee": 0.62,
    "New Zeland Dollar": 51.16,
    "Omani Rail": 214.25,
    "pakistani Rupee": 0.291,
    "Soudi Aribian Riyal": 21.99,
    "Singapore Dollar": 61.82,
    "Sri Lankan Rupee": 0.25,
    "Thai Bhat": 2.41,
    "Turkish lira": 4.32,
    "US Dollar": 82.48,
    "Venenzuelan Bolivar":0.000034
    }

def ok():
    price = rupee.get()
    answer = variable.get()
    DICT = OPTIONS.get(answer,None)
    converted = float(DICT)*float(price)
    Result.delete(1.0,END)
    Result.insert(INSERT,"Price in ",INSERT,answer,INSERT," = ", INSERT, converted)


appName = Label(converter,text="Currency",
                font=("arial",25,"bold","underline"),fg="dark red")
appName.grid(row=0,column=0,padx=10)
appName = Label(converter,text="Converter",
                font=("arial",25,"bold","underline"),fg="dark red")
appName.grid(row=0,column=2,padx=10)

Result = Text(converter,height=5,width=50,font=("arial",10,"bold"),bd=5)
Result.grid(row=1,columnspan=10,padx=3)

india = Label(converter,text="INDIAN Rupees: ",font=("arial",10,"bold"), fg="red")
india.grid(row=2,column=0)

rupee = Entry(converter,font=("calibri",20,"bold"))
rupee.grid(row=2,column=1)

choice = Label(converter,text="Choose currency: ",font=("arial",10,"bold"), fg="red")
choice.grid(row=3,column=0)

variable = StringVar(converter)
variable.set(None)
option = OptionMenu(converter,variable,*OPTIONS)
option.grid(row=3,column=1,sticky="ew")
button = Button(converter,text = "Convert", fg = "green", font=("callable",20,), bg="powder blue",command=ok)
button.grid(row=3,column=2)

mainloop()