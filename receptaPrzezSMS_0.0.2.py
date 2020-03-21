# credits:
# https://codinginfinite.com/sending-sms-using-python-and-twilio-api/
# https://exceptionshub.com/how-to-center-a-window-on-the-screen-in-tkinter.html


import tkinter
import tkinter.messagebox
from twilio.rest import Client
class SMSGUI:
    def __init__(self):
        #Create root window
        self.root = tkinter.Tk()

        #Set title of root window
        self.root.title("Recepta przez SMS")

        #Create top frame
        self.top_frame = tkinter.Frame(self.root)
        #Create frame one
        self.frame_one = tkinter.Frame(self.root)
        #Create frame two
        self.frame_two = tkinter.Frame(self.root)
        #Create frame three
        self.frame_three = tkinter.Frame(self.root)
        #Create frame four
        self.frame_four = tkinter.Frame(self.root)
        #Create bottom frame
        self.bottom_frame = tkinter.Frame(self.root)

        #Create a label
        self.header = tkinter.Label(self.top_frame, text = "Wpisz dane pacjenta(-tki) i wyślij kod e-recepty przez SMS")
        self.subheader = tkinter.Label(self.top_frame, text = "Dane Pacjenta")
        #Pack the label
        self.header.pack(side = 'top')

        #Label for Patient Name
        self.patientName = tkinter.Label(self.frame_one, text = "Imię:                       ")
        self.patientName.pack(side = 'left')
        #Create an entry widget for Patient Name
        self.patientName = tkinter.Entry(self.frame_one, width = 40)
        self.patientName.pack(side = 'left')

        #Label for Patient Surname
        self.patientSurname = tkinter.Label(self.frame_two, text = "Nazwisko:              ")
        self.patientSurname.pack(side = 'left')
        #Create an entry widget for Patient Surname
        self.patientSurname = tkinter.Entry(self.frame_two, width = 40)
        self.patientSurname.pack(side = 'left')

        #Label for Telephone number
        self.toNumber = tkinter.Label(self.frame_three, text = "Numer telefonu:    ")
        self.toNumber.pack(side = 'left')
        #Create an entry widget for TO: number
        self.toNumber = tkinter.Entry(self.frame_three, width = 9)
        self.toNumber.pack(side = 'left')

        #Label for Prescription code
        self.prescriptionCode = tkinter.Label(self.frame_four, text = "Kod e-recepty (4 cyfry):   ")
        self.prescriptionCode.pack(side = 'left')
        #Create an entry widget for Prescription code
        self.prescriptionCode = tkinter.Entry(self.frame_four, width = 4)
        self.prescriptionCode.pack(side = 'left')

        #Create button
        self.send = tkinter.Button(self.bottom_frame, text = "Wyślij SMS", command = self.sendSms)
        self.send.pack(side = 'left')
        
        # Pack frames
        self.top_frame.pack()
        self.frame_one.pack(anchor="w")
        self.frame_two.pack(anchor="w")
        self.frame_three.pack(anchor="w")
        self.frame_four.pack(anchor="w")
        self.bottom_frame.pack()

        # Center frame on screen
        self.root.withdraw()
        self.root.update_idletasks()  # Update "requested size" from geometry manager
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry("+%d+%d" % (x, y))
        self.root.deiconify()

        tkinter.mainloop()

    def sendSms(self):
        account_sid = 'your-sid'
        auth_token = 'your-auth-token'
        client = Client(account_sid, auth_token)
        name = str(self.patientName.get())
        surname = str(self.patientSurname.get())
        prescription = str(self.prescriptionCode.get())
        # rec = str(self.toNumber.get())
        rec = '+48' + str(self.toNumber.get())
        msg = "Pan(i):  " + name + " " + surname + "." + "\n" + "Nr telefonu:  " + rec + "." + "\n" + "Kod e-recepty:  " + prescription + "." + "\n" + "Kod okazać z dokumentem tożsamości / nr PESEL w aptece."
        message = client.messages.create(body=msg,from_='your-trial-number',to= rec
        )
        # print(message.sid)
        tkinter.messagebox.showinfo('Wysłano następującą wiadomość:', msg)

gui = SMSGUI()