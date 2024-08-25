from tkinter import *
from tkinter import messagebox
import ast
from Vista.signUp import SignUp
from Vista.gui import MiVentanaPrincipal

class Login:
    def __init__(self,root):
        self.root= root
        self.root.title("Login")
        self.root.geometry("925x500+300+200")
        self.root.configure(bg="#fff")
        self.root.resizable(False,False)

        #Imagen en Ventana
        self.img =PhotoImage(file='login1.png')
        self.img_label=Label(self.root,image=self.img,border=0,bg='white')
        self.img_label.place(x=50,y=50)
        
        #Marco en Ventana
        self.frame=Frame(self.root,width=350,height=350,bg="white")
        self.frame.place(x=480,y=70)
        
        
        #Widgets
        self.heading=Label(self.frame,text='iniciar Sesion',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'),borderwidth=0, highlightthickness=0)
        self.heading.place(x=30,y=5)
        
        #User Entry
        self.user = Entry (self.frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11),borderwidth=0, highlightthickness=0)
        self.user.place(x=30,y=80)
        self.user.insert(0,'Usuario')
        self.user.bind('<FocusIn>', self.on_enter_user)
        self.user.bind('<FocusOut>', self.on_leave_user)
        
        
                
        self.frame1=Frame(self.frame,width=295,height=2,bg='black')
        self.frame1.place(x=25,y=107)
        
        #Password Entry
        self.code = Entry (self.frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11),borderwidth=0, highlightthickness=0)
        self.code.place(x=30,y=150)
        self.code.insert(0,'Contraseña')
        self.code.bind('<FocusIn>', self.on_enter_pass)
        self.code.bind('<FocusOut>', self.on_leave_pass)
        
        self.frame2=Frame(self.frame,width=295,height=2,bg='black')
        self.frame2.place(x=25,y=177)
        
        #-----
        self.button=Button(self.frame,width=27,pady=7,text='Registrarse',bg='#57a1f8',fg='white',border=0,command=self.signin)
        self.button.place(x=35,y=204)
        self.label=Label(self.frame,text='¿Aun no Tienes Cuenta?',fg='black',bg='white',font=("Arial",9))
        self.label.place(x=40,y=270)
        
        self.sign_up=Button(self.frame,width=10,text="Registrarse",bg='white',cursor='hand2',fg='#57a1f8',font=('Arial',9),borderwidth=0, highlightthickness=0,command=self.singup_command)
        self.sign_up.place(x=230,y=265)
        
        
        
    def on_enter_user(self, event):
        if self.user.get() == 'Usuario':
            self.user.delete(0, 'end')
    
    def on_leave_user(self, event):
        if self.user.get() == '':
            self.user.insert(0, 'Usuario')
            
    def on_enter_pass(self, event):
        if self.code.get() == 'Contraseña':
            self.code.delete(0, 'end')
    
    def on_leave_pass(self, event):
        if self.code.get() == '':
            self.code.insert(0, 'Contraseña')
            
    def signin(self):
        username=self.user.get()
        password=self.code.get()
        
        self.file=open('datasheet.txt','r')
        self.d=self.file.read()
        self.r=ast.literal_eval(self.d)
        self.file.close()
        
        
        #print(self.r.keys())
        #print(self.r.values())
        
        if username in self.r.keys() and password==self.r[username]:
            self.open_main_window()
        else:
            messagebox.showerror("Incorrecto","Usuario o Contraseña Erroneos")

    def open_main_window(self):
        # Abre la ventana principal de la aplicación
        print("Abriendo la ventana Principal")
        self.screen = Toplevel(self.root)
        self.screen.title("App")
        #self.screen.geometry("800x600")  # Ajusta el tamaño según sea necesario
        MiVentanaPrincipal(self.screen)
        self.screen.grab_set()
        
    def singup_command(self):
        self.window = Toplevel(self.root)
        self.window.title("Registrarse")
        SignUp(self.window)
        self.window.grab_set()
    
        
        

        
""" 
if __name__ == "__main__":
    root = Tk()
    login_app = Login(root)
    root.mainloop()
"""