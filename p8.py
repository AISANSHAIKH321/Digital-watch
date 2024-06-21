# digital clock

from tkinter import*
from datetime import*

root = Tk()
root.title("Digital Watch by Kamal Sir")
root.geometry("800x400+350+350")
root.configure(bg="honeydew2")
root.resizable(False,False)

f = ("calibri",150,"bold")
lab = Label(root, font=f, bg="honeydew2", fg="black")
lab.pack(pady=20)

def show():
	dt = datetime.now()

	hr = dt.hour
	shr = str(hr)
	if hr < 10 :
		shr ="0" + shr
	
	mi = dt.minute
	smi = str(mi)
	if mi < 10:
		smi = "0" + smi
	
	se = dt.second
	sse = str(se)
	if se < 10:
		sse = "0" + sse

	msg = shr +":" +smi +":" +sse
	lab.configure(text=msg)
	root.after(1,show)
show()

root.mainloop()