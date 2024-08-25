from tkinter import Tk
from Vista.signIn import Login

def main():
    root = Tk()
    app = Login(root)
    root.mainloop()

if __name__ == "__main__":
    main()
