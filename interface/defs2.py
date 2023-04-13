from tkinter import messagebox, Label, Entry, Tk, Frame, W, Button
import datetime

date = datetime.datetime.now()    # Atualização data diária para def relatorio()

def generate_file():
       
       countClient = 0    # variavel para contar o numero de clientes
       nomess = []        # lista para armazenar nomes dos clientes
    
       logins = open('logins.txt', 'r')
       for linhas in logins.readlines():
              l = linhas.split('-')              
              nomess.append(l[0])      # Adiciona o primeiro valor (no caso 'Nome: nome') na lista          
              countClient += 1         # conta um cliente
                     
       arquivo = open("dados.txt", "w+")             # "w+" para criar o relatorio 
       arquivo.write('Relatorio de Clientes \n')
       arquivo.write('\n')
       arquivo.write(f'A loja Sk8-Life possui {countClient} cliente(s) \n')
       
       for i in range(len(nomess)):                
       #for range para percorrer os idices da lista nomess
              arquivo.write(str(f'{i + 1}.{nomess[i].split(":")[1]} \n'))    
              #printa cada indice da lista 
       arquivo.write(f'City, {date.day}/{date.month}/{date.year}.')  
       #data atualizada para o relatorio gerado
       arquivo.close()
       
       return messagebox.showinfo('', 'File generated in dados.py')
       
       

def login(user_entry, pass_entry):
    username = user_entry.get()
    password = pass_entry.get()
    
    readlog = open('logins.txt', 'r')
    
    for line in readlog.readlines():
           value = line.split('-')
           if username == value[1].split(':')[1].strip() and password == value[2].split(':')[1].strip():
                  
                  return messagebox.showinfo("Login sucessfull", "")
           
           elif username == '' or password == '':
                  return messagebox.showinfo("", "Blank not allowed")
           else:
                  return messagebox.showinfo("", "Wrong Username or Password")             
    readlog.close()


def set_register(root, entry_name, entry_login, entry_password, entry_email, entry_birth, entry_phone, entry_street):                  
       name = entry_name.get()
       login = entry_login.get()
       password = entry_password.get()
       email = entry_email.get()
       birth = entry_birth.get()
       phone = entry_phone.get()
       street = entry_street.get()
       
       lista = [name, login, password, email, birth, phone, street]
       for i in lista:
              if i == '':
                     return messagebox.showinfo("", "Blank is not allowed")
                     
                     
       logins = open("logins.txt", 'a')
       logins.write(f'Nome: {name} -Login: {login} -Senha: {password} -Email: {email} -Data de Nascimento: {birth} -Numero de celular: {phone} -Endereco:{street} \n')
       logins.close()
       
       messagebox.showinfo("", "Register Complete!")
       
       return root.destroy()

          
          
def register():

      root = Tk()
      root.title("Registration")
      root.geometry("500x500")
      root.config(bg='#23272c')
      
      # Title
      Label(root, text="Create Your Account", font=("Helvetica", 20), fg="white", bg="#23272c").pack(pady=20)

      # Registration Form
      frame_reg = Frame(root, bg="#23272c")
      frame_reg.pack()

      # Name
      Label(frame_reg, text="Name", font=("Helvetica", 14), fg="white", bg="#23272c").grid(row=0, column=0, padx=10, pady=10, sticky=W)
      entry_name = Entry(frame_reg, font=("Helvetica", 14), width=20)
      entry_name.grid(row=0, column=1, padx=10, pady=10)

      # Login
      Label(frame_reg, text="Login", font=("Helvetica", 14), fg="white", bg="#23272c").grid(row=1, column=0, padx=10, pady=10, sticky=W)
      entry_login = Entry(frame_reg, font=("Helvetica", 14), width=20)
      entry_login.grid(row=1, column=1, padx=10, pady=10)

      # Password
      Label(frame_reg, text="Password", font=("Helvetica", 14), fg="white", bg="#23272c").grid(row=2, column=0, padx=10, pady=10, sticky=W)
      entry_password = Entry(frame_reg, font=("Helvetica", 14), width=20, show="*")
      entry_password.grid(row=2, column=1, padx=10, pady=10)

      # Email
      Label(frame_reg, text="Email", font=("Helvetica", 14), fg="white", bg="#23272c").grid(row=3, column=0, padx=10, pady=10, sticky=W)
      entry_email = Entry(frame_reg, font=("Helvetica", 14), width=20)
      entry_email.grid(row=3, column=1, padx=10, pady=10)

      # Birth Date
      Label(frame_reg, text="Birth Date", font=("Helvetica", 14), fg="white", bg="#23272c").grid(row=4, column=0, padx=10, pady=10, sticky=W)
      entry_birthdate = Entry(frame_reg, font=("Helvetica", 14), width=20)
      entry_birthdate.grid(row=4, column=1, padx=10, pady=10)

      # Phone Number
      Label(frame_reg, text="Phone", font=("Helvetica", 14), fg="white", bg="#23272c").grid(row=5, column=0, padx=10, pady=10, sticky=W)
      entry_phone = Entry(frame_reg, font=("Helvetica", 14), width=20)
      entry_phone.grid(row=5, column=1, padx=10, pady=10)

      # Address
      Label(frame_reg, text="Address", font=("Helvetica", 14), fg="white", bg="#23272c").grid(row=6, column=0, padx=10, pady=10, sticky=W)
      entry_street = Entry(frame_reg, font=("Helvetica", 14), width=20)
      entry_street.grid(row=6, column=1, padx=10, pady=5)
      
      singup = Button(root, text = 'SIGN UP', bd = 3, font=("Helvetica", 14), 
                      fg="white", 
                      bg="#23272c",
                      command= lambda: set_register(root, entry_name, entry_login, entry_password, entry_email, entry_birthdate, entry_phone, entry_street)
                      ).place(x = 205, y = 430)
      
      root.update()
      screen_width = root.winfo_screenwidth()
      screen_height = root.winfo_screenheight()

      x = int((screen_width - root.winfo_width()) / 2)
      y = int((screen_height - root.winfo_height()) / 2)

      root.geometry("{}x{}+{}+{}".format(root.winfo_width(),root.winfo_height(), x, y))
      
      root.mainloop()