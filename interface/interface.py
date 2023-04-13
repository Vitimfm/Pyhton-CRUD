from tkinter import Label, Entry, messagebox, Tk, Button, Canvas
from PIL import ImageTk, Image
import defs2

root = Tk()
root.title("Koala Store")
root.resizable(0,0)

bg_frame = Image.open('interface\\imgs\\background.png')
photo = ImageTk.PhotoImage(bg_frame)
bg_panel = Label(root, image = photo)
bg_panel.image = photo
bg_panel.pack(fill= 'both', expand= 'yes')

# ==================== Sign In ===========================

sign_line1 = Canvas(root, width=255, height=2.0, bg="#bdb9b1", highlightthickness=0)
sign_line1.place(x=715, y=235)

koala_icon = Image.open('interface\\imgs\\koala_icon.png')
photo3= ImageTk.PhotoImage(koala_icon)
sign = Label(root, image = photo3, bg= '#23272c')
sign.place(x = 785, y = 255)

singin = Label(root, text ="SIGN IN", 
               font = ('Verdana', 13), 
               bg = '#23272c', 
               fg = 'white')
singin.place(x= 800, y = 365)

user_entry = Entry(root)
user_entry.place(x = 780, y = 405)
pass_entry= Entry(root)
pass_entry.place(x = 780, y = 445)

username_icon = Image.open('interface\\imgs\\username_icon.png')
photo1 = ImageTk.PhotoImage(username_icon)
user = Label(root, image= photo1, bg = '#23272c')
user.place(x = 740, y = 400)

password_icon = Image.open('interface\\imgs\\password_icon.png')
photo2 = ImageTk.PhotoImage(password_icon)
word = Label(root, image= photo2, bg= '#23272c')
word.place(x = 740, y = 440)


Login_button = Button(root, text= 'LOGIN', bg = '#24242c', width=10, 
                      height= 1, 
                      fg = 'white',
                      border = 3,
                      command = lambda: defs2.login(user_entry, pass_entry) 
                      ).place(x=800, y = 480)

forgot = Button(root, text = 'Forgot your password?', 
                fg = 'white',
                bg = '#24242c',
                border= 0,
                ).place(x = 780, y= 515)

accont = Label(root, text = 'Not accont yet?', 
               fg = 'white', 
               bg = '#24242c'
               ).place(x = 760, y = 545)

register_button = Button(root,
                         text = 'SIGN UP NOW',
                         bg = '#24242c',
                         fg = 'white',
                         border= 0,
                         command = defs2.register
                         ).place(x=850, y = 545)

sign_line2 = Canvas(root, width=255, 
                   height=2.0, 
                   bg="#bdb9b1", 
                   highlightthickness=0)
sign_line2.place(x=715, y=580)

# =================== Commands ============================

store = Label(root, 
              text= 'STORE DATA', 
              bg = '#24242c', 
              fg = 'white',
              font= ('Verdana', 13)
              ).place(x = 785, y = 20)

clients_button = Button(root, 
                        text= 'CLIENTS', 
                        bg = '#24242c', 
                        width=25, height= 2, 
                        fg = 'white',
                        border = 3,
                        ).place(x=750, y = 60)

show_button = Button(root, 
       text= 'SHOW INFO', 
       bg = '#24242c', 
       width=25, height= 2, 
       fg = 'white',
       border = 3,
       ).place(x=750, y = 115)

file_button = Button(root, 
       text= 'FILE', 
       bg = '#24242c', 
       width=25, height= 2, 
       fg = 'white',
       border = 3,
       command= defs2.generate_file
       ).place(x=750, y = 170)


root.update()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width - root.winfo_width()) / 2)
y = int((screen_height - root.winfo_height()) / 2)

root.geometry("{}x{}+{}+{}".format(root.winfo_width(),root.winfo_height(), x, y))

root.mainloop()
