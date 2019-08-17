import tkinter

window=tkinter.Tk()
window.title("GUI")
label=tkinter.Label(window,text="sk shahriar ahmed raka" ,font=("Arial Bold",50))
window.geometry("1080x720")
label.grid(column=0,row=0)
bt=tkinter.Button(window,text="what?",bg="blue",fg="red")
bt.grid(column=1,row=0)
window.mainloop()