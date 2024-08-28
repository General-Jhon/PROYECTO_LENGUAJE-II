from tkinter import *
from tkinter import messagebox
import ast
import os

class SignUp:
    def __init__(self,window):
        self.window= window
        self.window.title("SingUP")
        self.window.geometry("925x500+300+200")
        self.window.configure(bg="#fff")
        self.window.resizable(False,False)

        #Imagen en Ventana
        self.img =PhotoImage(file='login.png')
        self.img_label=Label(self.window,image=self.img,border=0,bg='white')
        self.img_label.place(x=50,y=50)
        
        #Marco en Ventana
        self.frame=Frame(self.window,width=350,height=390,bg="white")
        self.frame.place(x=480,y=70)
        
        
        #Widgets
        self.heading=Label(self.frame,text='Crear Cuenta',fg='#ff0000',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
        self.heading.place(x=30,y=5)
        
        
#Entry User
        self.user = Entry(self.frame,width=25,fg='black',bg='white',font=('Microsoft YaHei UI Light',11),borderwidth=0, highlightthickness=0)
        self.user.place(x=30,y=80)
        self.user.insert(0,'Usuario')
        self.user.bind("<FocusIn>",self.on_enter_user)
        self.user.bind("<FocusOut>",self.on_leave_user)
        
        
        self.frame1=Frame(self.frame,width=295,height=2,bg='black')
        self.frame1.place(x=25,y=107)
        
        
#Entry Password
        self.code = Entry(self.frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11),borderwidth=0, highlightthickness=0)
        self.code.place(x=30,y=150)
        self.code.insert(0,'Contraseña')
        self.code.bind("<FocusIn>",self.on_enter_pass)
        self.code.bind("<FocusOut>",self.on_leave_pass)
        
        
        self.frame2=Frame(self.frame,width=295,height=2,bg='black')
        self.frame2.place(x=25,y=177)
        
#Entry Conform

        self.conform_code = Entry(self.frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11),borderwidth=0, highlightthickness=0)
        self.conform_code.place(x=30,y=220)
        self.conform_code.insert(0,'Confirmar Contraseña')
        self.conform_code.bind("<FocusIn>",self.on_enter_pass_conform)
        self.conform_code.bind("<FocusOut>",self.on_leave_pass_conform)
        
        
        self.frame3=Frame(self.frame,width=295,height=2,bg='black')
        self.frame3.place(x=25,y=247)
        
        # Entry Serial Number
        self.serial_code = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11), borderwidth=0, highlightthickness=0)
        self.serial_code.place(x=30, y=275)
        self.serial_code.insert(0, 'Serial de Activación')
        self.serial_code.bind("<FocusIn>", self.on_enter_serial)
        self.serial_code.bind("<FocusOut>", self.on_leave_serial)
        self.frame4 = Frame(self.frame, width=295, height=2, bg='black')
        self.frame4.place(x=25, y=300)
        
#Boton Confirmacion
        self.conform=Button(self.frame,width=30,pady=7,text='Registrarse',bg='#ff0000',fg='white',border=0,command=self.signup)
        self.conform.place(x=35,y=320)
        self.conform.config(anchor='center')
        self.label=Label(self.frame,text='¿Ya Tienes Cuenta?',fg='black',bg='white',font=('Microsoft YaHei UI Light',9),borderwidth=0, highlightthickness=0)
        self.label.place(x=30,y=369)
        
        self.signin=Button(self.frame,width=9,text='Iniciar Session',bg='white',cursor='hand2',fg='#ff0000',borderwidth=0, highlightthickness=0,command=self.sign)
        self.signin.place(x=200,y=365)
        
        # Leer los seriales archivo txt
        self.valid_serials = self.load_valid_serials()

    def load_valid_serials(self):
        file_path = 'serials.txt'
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return [line.strip() for line in file.readlines()]
        return []
     
    def signup(self):
        username = self.user.get()
        password = self.code.get()
        confirm_password = self.conform_code.get()
        serial = self.serial_code.get()
        
        if password == confirm_password:
            if serial in self.valid_serials:
                file_path = 'datasheet.txt'

                # Verificar si el archivo existe
                if os.path.exists(file_path):
                    with open(file_path, 'r') as file:
                        data = file.read()
                        if data:
                            user_data = ast.literal_eval(data)
                        else:
                            user_data = {}
                else:
                    user_data = {}

                # Agregar/actualizar los datos del usuario
                user_data[username] = password

                # Escribir los datos actualizados en el archivo
                with open(file_path, 'w') as file:
                    file.write(str(user_data))

                messagebox.showinfo('Registro Exitoso', 'Cuenta creada con éxito')

            else:
                messagebox.showerror('Serial Inválido', 'El Serial de Activación es incorrecto')
        else:
            messagebox.showerror('Contraseña Incorrecta', 'Las Contraseñas Deben Ser Iguales')

    def on_enter_user(self, event):
        if self.user.get() == 'Usuario':
            self.user.delete(0, 'end')


    
        
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
            
    def on_enter_pass_conform(self, event):
        if self.conform_code.get() == 'Confirmar Contraseña':
            self.conform_code.delete(0, 'end')
    
    def on_leave_pass_conform(self, event):
        if self.conform_code.get() == '':
            self.conform_code.insert(0, 'Confirmar Contraseña')
            
    def on_enter_serial(self, event):
        if self.serial_code.get() == 'Serial de Activación':
            self.serial_code.delete(0, 'end')
    
    def on_leave_serial(self, event):
        if self.serial_code.get() == '':
            self.serial_code.insert(0, 'Serial de Activación')
    #-----
    def sign(self):
        self.window.destroy()
            
            

    

if __name__ == "__main__":
    root = Tk()
    login_app = SignUp(root)
    root.mainloop()



    