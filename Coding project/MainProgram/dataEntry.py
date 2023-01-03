import math 
import customtkinter

customtkinter.set_appearance_mode("dark ")

customtkinter.set_default_color_theme("dark-blue") 

#radio_var = tkinter.IntVar(0)
root = customtkinter.CTk()
root.geometry("500x500")

root2 = customtkinter.CTk()
root2.geometry("500x500")

combobox_var = customtkinter.StringVar(value="option 2")  # set initial value

def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)





def login():
    print("login")

def stuff():
    if checkbox.get() == 1:
        print("hell yes")

frame = customtkinter.CTkFrame(master = root, width = 300, height = 300)
frame.pack(pady = 20, padx = 60, fill = "both", expand = True)

label = customtkinter.CTkLabel(master = frame, text = "Login System", font = ("Roboto", 24))
label.pack(pady = 20,padx = 20)

entry1 = customtkinter.CTkEntry(master = frame, placeholder_text="Username")
entry1.pack(pady = 20,padx = 20)

entry2 = customtkinter.CTkEntry(master = frame, placeholder_text="Password", show = "*")
entry2.pack(pady = 20,padx = 20)

button = customtkinter.CTkButton(master = frame, text = "Login", command = login) 
button.pack(pady = 20,padx = 20)

checkbox = customtkinter.CTkCheckBox(master = frame, text = "Remember me", command = stuff)
checkbox.pack(pady = 20,padx = 20)


combobox = customtkinter.CTkComboBox(master=frame,
                                     values=["option 1", "option 2"],
                                     command=combobox_callback,
                                     variable=combobox_var)
combobox.pack(padx=20, pady=10)


root.mainloop()
