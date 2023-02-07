from tkinter import *
from tkinter import messagebox
import wikipedia

class SearchApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Search App | Developed by Adarsh Kumar")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#262626")

        title=Label(self.root,text="Search Application",font=("times new roman",40,"bold"),bg="white",fg="#262626").place(x=0,y=0,relwidth=1)
        lbl_word=Label(self.root,text="Enter Word",font=("times new roman",30,"bold"),bg="#262626",fg="white").place(x=10,y=100)
       
        self.var_search=StringVar()
        txt_word=Entry(self.root,textvariable=self.var_search,font=("times new roman",20)).place(x=250,y=110,width=300)
        btn_search=Button(self.root,text="Search",command=self.searchword,font=("times new roman",20,"bold"),bg="lightyellow",fg="#262626").place(x=600,y=108,height=40,width=120)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",20,"bold"),bg="lightyellow",fg="#262626").place(x=790,y=108,height=40,width=120)
        btn_enable=Button(self.root,text="Enable Mode",command=self.enable,font=("times new roman",20,"bold"),bg="lightyellow",fg="#262626").place(x=950,y=108,height=40,width=200)
        btn_disable=Button(self.root,text="Disable",command=self.disable,font=("times new roman",20,"bold"),bg="lightyellow",fg="#262626").place(x=1210,y=108,height=40,width=120)

        self.lbl_mode=Label(self.root,font=("times new roman",15),bg="#262626",fg="yellow")
        self.lbl_mode.place(x=20,y=160)
        frame1=Frame(self.root,bd=2,relief=RIDGE)
        frame1.place(x=15,y=190,width=1320,height=500)

        scrolly=Scrollbar(frame1,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill='y')
        
        self.txt_area=Text(frame1,font=("times new roman",15),yscrollcommand=scrolly.set)
        self.txt_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_area.yview)

    def enable(self):
        self.txt_area.config(state=NORMAL)  
        self.lbl_mode.config(text="MODE: ENABLED")

    def disable(self):
        self.lbl_mode.config(text="MODE: DISABLED")
        self.txt_area.config(state=DISABLED) 

    def clear(self):
        self.var_search.set("")
        self.txt_area.delete('1.0',END)
        self.lbl_mode.config(text="")

    def searchword(self):
        if self.var_search.get()=="":
            messagebox.showerror("Error","Search Area should not be empty")     
        else:
            fetch_data=wikipedia.summary(self.var_search.get())
            self.txt_area.insert('1.0',fetch_data)          
    

root = Tk()
obj = SearchApp(root)
root.mainloop()    