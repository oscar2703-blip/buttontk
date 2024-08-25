from tkinter import*
root=Tk()
root.geometry("100x100")

btn=Button(root,text="Click Me!!",bd="5",background="cyan",command=root.destroy)
btn.pack(side="top")

root.mainloop()