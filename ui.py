from tkinter import Tk, filedialog, Label, Button, Canvas
import pydicom
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

root = Tk()

def open():
    root.filename = filedialog.askopenfilename(initialdir="./", title="Selecte image")
    dataset = pydicom.dcmread(root.filename)
    pat_name = dataset.PatientName
    display_name = pat_name.family_name + ", " + pat_name.given_name
    print(root.filename)
    plt.imshow(dataset.pixel_array, cmap=plt.cm.bone)
    plt.savefig('./tmp/test.png')
    label = Label(root, text="Filename.........: {}".format(root.filename))
    label.grid(column=2,row=0)
    label = Label(root, text="Storage type.....: {}".format(dataset.SOPClassUID))
    label.grid(column=2,row=1)
    label = Label(root, text="Patient's name...: {}".format(display_name)) ## nguoi benh
    label.grid(column=2,row=2)
    label = Label(root, text="Patient id.......: {}".format(dataset.PatientID))
    label.grid(column=2,row=3)
    label = Label(root, text="Modality.........: {}".format(dataset.Modality))
    label.grid(column=2,row=4)
    label = Label(root, text="Study Date.......: {}".format(dataset.StudyDate))
    label.grid(column=2,row=5)
    label = Label(root, text="Image size.......: {} x {}, {} bytes".format(dataset.Rows, dataset.Columns, len(dataset.PixelData)))
    label.grid(column=2,row=6)
    show_image()

def show_image():
    image = Image.open('./tmp/test.png')
    display = ImageTk.PhotoImage(image)
    label = Label(root, image=display)
    label.grid(column=1, row=0, columnspan=1, rowspan=7)
    label.image = display

def save_as_png():
    plt.savefig('./output/test.png')

root.title('DICOM Example')
root.geometry('1400x600')
my_btn = Button(root, text="Open image", command=open)
my_btn.grid(column=0, row=0)
my_btn2 = Button(root, text="Save as png image", command=save_as_png)
my_btn2.grid(column=0, row=1)


root.mainloop()

#
# window = Tk()
#
# window.title("Welcome to LikeGeeks app")
#
# window.geometry('350x200')
#
# lbl = Label(window, text="Hello")
#
# lbl.grid(column=0, row=2)
#
# btn = Button(window, text="Click Me")
#
# btn.grid(column=1,row=1)
#
# window.mainloop()