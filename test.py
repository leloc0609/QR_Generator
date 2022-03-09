import tkinter as tk
import qrcode  as qr

def getURL():
    tmp = userEntry.get()
    img = qr.make(tmp)
    tmp2  = userEntry2.get()
    type(img)  # qrcode.image.pil.PilImage
    img.save(tmp2+".png")

window = tk.Tk()

frame= tk.Frame(window,height=1000, width=1000)
frame.pack()
frame.columnconfigure([0],weight=1, minsize=100)
frame.rowconfigure([0, 1, 2,3,4], minsize=100)

inputFrame = tk.Label(master = frame, text ="Enter link to be convert:")
userEntry = tk.Entry(master = frame, width=100 )
inputFrame2 = tk.Label(master = frame, text ="Enter name to save:")
userEntry2 = tk.Entry(master = frame, width=100 )
setButton =  tk.Button(master = frame, text ="Press to convert", command=getURL, activebackground="red")
inputFrame.grid(column=0, row=0,sticky="ew", padx=10,pady=10)
userEntry.grid(column=0, row=1,sticky="ew",padx=10,pady=10)
inputFrame2.grid(column=0, row=2,sticky="ew", padx=10,pady=10)
userEntry2.grid(column=0, row=3,sticky="ew",padx=10,pady=10)
setButton.grid(column=0, row=4,sticky="ew",padx=10,pady=10)


window.mainloop()
