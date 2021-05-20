# --- Mulitple Forms ---
#
# A project to demonstrate how to create a program with multiple forms.
#
# --- Kyle Wilkinson ---
# --- 30/03/2021 ---

# import libraries
from tkinter import *
import random

# --- Define Functions ---
def DrivingLicense():
    #Define Functions
    def DLicenseCheck():
        DLname = inpName.get()
        Age = inpAge.get()

        if DLname != "" or Age != "":
            if int(Age) > 16:
                lblElegible.config(text=DLname + " you are elegible for a license.")
            else:
                lblElegible.config(text=DLname + " you are too young to drive.")
        else:
            lblElegible.config(text=DLname + "please enter your details.")
    
    #Design the form
    DLForm = Tk() # This creates a GUI and assigns it a name
    DLForm.title("Driving License - Kyle Wilkinson")
    DLForm.configure(bg = "dimgrey")
    DLForm.geometry("300x300+300+0") # sets the dimension Form. Width, Height, x position, Y position

    inpName = Entry(DLForm, font=("default", 14))
    inpAge = Entry(DLForm, font=("default", 14))

    inpName.place(x=125, y=100, width=150, height=30)
    inpAge.place(x=125, y=200, width=150, height=30)


    btnCheck = Button(DLForm, text="Check", fg="black", bg="darkgrey", command=DLicenseCheck)

    btnCheck.place(x=25, y=75, width=50, height= 50)


    lblName = Label(DLForm, text="Enter Your Name Bellow", fg="Black", bg="dimgrey")
    lblAge = Label(DLForm, text="Enter Your Age", fg="Black", bg="dimgrey")
    lblElegible = Label(DLForm, text="", fg="black", bg="white")
    
    lblName.place(x=100, y=50, width=200, height=30)
    lblAge.place(x=100, y=150, width=200, height=30)
    lblElegible.place(x=50, y=250, width=200, height=30)

   
    


def ATO():
    def calculate():
        if inpKM.get().isdigit():
            KM = float(inpKM.get())
            if inpCC.get().isdigit():
                CC = inpCC.get()
                if int(CC) > 1500:
                    underprice = KM * 0.45
                    lblOutput.config(text="$%.2f"%underprice)
                else:
                    overprice = KM * 0.65
                    lblOutput.config(text="$%.2f"%overprice)
            else:
                lblOutput.config(text="Please enter all information")
        else:
            lblOutput.config(text="Please enter all information")

    ATOForm = Tk() # This creates a GUI and assigns it a name
    ATOForm.title("ATO Vehicle Rebate - Kyle Wilkinson")
    ATOForm.configure(bg = "lightgreen")
    ATOForm.geometry("300x300+300+0") # sets the dimension Form. Width, Height, x position, Y position

    inpKM = Entry(ATOForm, font=("default", 14))
    inpCC = Entry(ATOForm, font=("default", 14))

    inpKM.place(x=75, y=75, width=175, height=30)
    inpCC.place(x=75, y=180, width=175, height=30)

    btnSubmit = Button(ATOForm, font=("default", 20), text="S\nu\nb\nm\ni\nt", fg="black", bg="green", command= calculate)

    btnSubmit.place(x=20, y= 50, width=30, height=200)

    lblKM = Label(ATOForm, font=("default", 8), text="Please enter how Many\nKillometres you have travelled", fg="black", bg="lightgreen")
    lblCC = Label(ATOForm, font=("default", 8), text="Please enter how much\nCC your rental car has", fg="black", bg="lightgreen")
    lblOutputEx = Label(ATOForm, text="Please check how much you get back bellow", fg="Black", bg="lightgreen")
    lblOutput = Label(ATOForm, text="", fg="Black", bg="white")

    lblKM.place(x=75, y=45, width=175, height=30)
    lblCC.place(x=75, y=150, width=175, height=30)
    lblOutputEx.place(x=55, y=225, width=240, height=30)
    lblOutput.place(x=20, y=260, width=240, height=30)

def Wages():
    def Money():
        if inpHours.get().isdigit():
            Hours = float(inpHours.get())
            if inpAge.get().isdigit():
                Age = float(inpAge.get())
                if inpName.get() != "":
                    name = inpName.get()
                    if float(Age) < 18:
                        YoungTotal = Hours * 5.6
                        lblOutput.config(text="$%.2f"%YoungTotal)
                    else:
                        OldTotal = Hours * 7.8
                        lblOutput.config(text="$%.2f"%OldTotal)
                else:
                        lblOutput.config(text="Please enter all information")
            else:
                    lblOutput.config(text="Please enter all information")
        else:
            lblOutput.config(text="Please enter all information")

    WagesForm = Tk()
    WagesForm.title("Wages - Kyle Wilkinson")
    WagesForm.config(bg = "dimgrey")
    WagesForm.geometry("300x300+300+0")

    inpName = Entry(WagesForm, font=("default", 14))
    inpAge = Entry(WagesForm, font=("default", 14))
    inpHours = Entry(WagesForm, font=("default", 14))
    
    btnSubmit = Button(WagesForm, font=("default", 20), text="Submit", fg="black", bg="darkgrey", command= Money)
    btnSubmit.place(x=25, y=175, width=250, height=30)

    inpName.place(x=10, y=120, width=70, height=30)
    inpAge.place(x=90, y=120, width=70, height=30)
    inpHours.place(x=170, y=120, width=120, height=30)

    lblDetails = Label(WagesForm, font=("default", 8), text="Please enter your details down bellow", fg="black", bg="darkgrey")
    lblName = Label(WagesForm, font=("default", 8), text="Name", fg="black", bg="darkgrey")
    lblAge = Label(WagesForm, font=("default", 8), text="Age", fg="black", bg="darkgrey")
    lblHours = Label(WagesForm, font=("default", 8), text="Hours worked this week", fg="black", bg="darkgrey")
    lblOutputEx = Label(WagesForm, text="Please check how much you get back bellow", fg="Black", bg="darkgrey")
    lblOutput = Label(WagesForm, text="Please enter all information", fg="Black", bg="white")

    lblDetails.place(x=10, y=40, width=280, height=30)
    lblName.place(x=10, y=80, width=70, height=30)
    lblAge.place(x=90, y=80, width=70, height=30)
    lblHours.place(x=170, y=80, width=120, height=30)
    lblOutputEx.place(x=30, y=225, width=240, height=30)
    lblOutput.place(x=30, y=260, width=240, height=30)

def Farenheight():
    def FarScale(scaleNumber):
        Total = (int(scaleNumber) * 9/5) + 32
        lblOutput.config(text=f'{"%.2f"%Total}°F')

    # --- Design the Graphical User Interface GUI ---
    # Build the Form
    Form = Tk()  # this creates a GUI and assign it a name.
    Form.title("Project Name - Kyle Wilkinson")
    Form.configure(bg="dimgrey")
    Form.geometry("350x500+100+100") # sets the dimension of the form Width, Height, position on the screen X & Y coordinates

    # Create the form controls (the objects/widgets on the form, buttons, labels, inputboxes etc)

    scaleNumber = Scale(Form, from_=-100, to=100, label="Celcius", length=325, orient=HORIZONTAL, command=FarScale)
    scaleNumber.set(0)
    scaleNumber.place(x=10, y=100)

    lblOutput = Label(Form, text="0", font=("default", 14), fg="black", bg="White")
    labelOutput = Label(Form, text="Farenheight", font=("default", 14), fg="black", bg="White")

    # --- Set the Location on the form
    lblOutput.place(x=100, y=250, width=200, height=30)
    labelOutput.place(x=100, y=200, width=200, height=30)

def MultiplicationGrid():
    def Middle(self):
        Side = int(scaleSide.get())
        Bottom = int(scaleBottom.get())
        Total = Side * Bottom
        lblMiddle.config(text=Total)

    # --- Design the Graphical User Interface GUI ---
    # Build the Form
    Form = Tk()  # this creates a GUI and assign it a name.
    Form.title("Multiplication Grid - Kyle Wilkinson")
    Form.configure(bg="dimgrey")
    Form.geometry("500x500+200+200") # sets the dimension of the form Width, Height, position on the screen X & Y coordinates

    # Create the form controls (the objects/widgets on the form, buttons, labels, inputboxes etc)

    scaleSide = Scale(Form, from_=1, to=20, length=400, orient=VERTICAL, command=Middle)
    scaleSide.set(0)
    scaleSide.place(x=50, y=20)

    scaleBottom = Scale(Form, from_=1, to=20, length=400, orient=HORIZONTAL, command=Middle)
    scaleBottom.set(0)
    scaleBottom.place(x=70, y=420)

    lblMiddle = Label(Form, text="1", font=("default", 42), fg="black", bg="white")
    lblMiddle.place(x=250, y=250, width=100, height=100)

def ColorMixer():

    def ColorMix(Self):
        RedA = scaleRed.get()
        GreenA = scaleGreen.get()
        BlueA = scaleBlue.get()
        CMix = (RedA,GreenA,BlueA)
        print(CMix)
        HexMix = str('#%02x%02x%02x' % (RedA,GreenA,BlueA))
        print(HexMix)

        MixerForm.config(bg=HexMix)

        lblRGB.config(text=CMix)
        lblHex.config(text=HexMix)

    def Random(*args):
        Red = random.randint(0, 255)
        Green = random.randint(0, 255)
        Blue = random.randint(0, 255)
        scaleRed.set(Red)
        scaleGreen.set(Green)
        scaleBlue.set(Blue)

    MixerForm = Tk()
    MixerForm.title("Color Mixer - Kyle Wilkinson")
    MixerForm.config(bg="Black")
    MixerForm.geometry("300x300+300+300")

    scaleRed = Scale(MixerForm, from_=0, to=255, label="Red", orient=HORIZONTAL, command=ColorMix)
    scaleRed.set(0)
    scaleRed.pack()

    scaleGreen = Scale(MixerForm, from_=0, to=255, label="Green", orient=HORIZONTAL, command=ColorMix)
    scaleGreen.set(0)
    scaleGreen.pack()

    scaleBlue = Scale(MixerForm, from_=0, to=255, label="Blue", orient=HORIZONTAL, command=ColorMix)
    scaleBlue.set(0)
    scaleBlue.pack()

    btnRandom = Button(MixerForm, text="R\na\nn\nd\no\nm", font=("default", 24), fg="black", bg="white", command=Random)
    btnRandom.place(x=10, y=10, width=40, height=250)

    lblRGB = Label(MixerForm, text="0, 0, 0", font=("default", 14), fg="black", bg="White")
    lblHex = Label(MixerForm, text="#000000", font=("default", 14), fg="black", bg="White")

    lblRGB.place(x=100, y=200, width=100, height=30)
    lblHex.place(x=100, y=250, width=100, height=30)

# --- Design the Graphical User Interface (GUI) ---

# Build the Form
Form = Tk() # This creates a GUI and assigns it a name
Form.title("Multiple Forms - Kyle Wilkinson")
Form.configure(bg = "aliceblue")
Form.geometry("350x500+0+0") # sets the dimension Form. Width, Height, x position, Y position

#  Input Boxes
# ---Name and Set the Style
#inpEntry1 = Entry(Form, font=("default", 14))

# --- Set the location on the form
#inpEntry1.place(x=100, y=100, width=150, height=30)

# --- Labels ----
#  Name and Set the Style
lblHeader = Label(Form, text="Multi Form Project", font=("default", 24), fg="black", bg="aliceblue")

# --- Set the Location on the form
lblHeader.place(x=25, y=50, width=300, height=50)

# --- Buttons ---
# set Name and style and  assign a function to the command property
btnDriverLicense = Button(Form, text="Driver's License", fg="Black", bg="White", command = DrivingLicense)
btnATORebate = Button(Form, text="ATO Vehicle Rebate", fg="Black", bg="White", command = ATO)
btnWages = Button(Form, text="Calculate Wages", fg="Black", bg="White", command = Wages)
btnFarenheight = Button(Form, text="Farenheight", fg="Black", bg="White", command = Farenheight)
btnMultiplicationGrid = Button(Form, text="Multiplication Grid", fg="Black", bg="White", command = MultiplicationGrid)
btnColorMixer = Button(Form, text="ColorMixer", fg="Black", bg="White", command = ColorMixer)

# --- Set the Location on the form
btnDriverLicense.place(x=10, y=300, width=100, height=30)
btnATORebate.place(x=115, y=300, width=120, height=30)
btnWages.place(x=240, y=300, width=100, height=30)
btnFarenheight.place(x=10, y=350, width=100, height=30)
btnMultiplicationGrid.place(x=115, y=350, width=120, height=30)
btnColorMixer.place(x=240, y=350, width=100, height=30)

# run the main loop
Form.mainloop()