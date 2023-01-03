import customtkinter
from tkinter import *


app = customtkinter.CTk()
app.title("Another Calculator")
app.geometry("500x600")

customtkinter.set_appearance_mode("dark ")
customtkinter.set_default_color_theme("dark-blue") 


expression = ""

font1 = ("Arial", 20, "bold")

# Function to update expression
# in the text entry box
def show(num):
	# point out the global expression variable
	global expression

	# concatenation of string
	expression = expression + str(num)

	# update the expression by using set method
	equation.set(expression)

def clear ():





result_entry = customtkinter.CTkEntry(master = app, placeholder_text  = "", width = 250, fg_color="white", text_color='black')
result_entry.place(x = 0, y = 10)

Button1 = customtkinter.CTkButton(master = app, command=lambda: show("1"), text = "1", width = 50, height = 2, font = font1, fg_color="#b5520b", hover_color= "#b5520b", text_color='white')
Button1.place(x = 10, y =60)

Button2 = customtkinter.CTkButton(master = app,command=lambda: show("2"), text = "2", width = 50, height = 2, font = font1, fg_color="#b5520b", hover_color= "#b5520b", text_color='white')
Button2.place(x = 70, y =60)

Button3 = customtkinter.CTkButton(master = app,command=lambda: show("3"), text = "3", width = 50, height = 2, font = font1, fg_color="#b5520b", hover_color= "#b5520b", text_color='white')
Button3.place(x = 130, y =60)

Button4 = customtkinter.CTkButton(master = app, command=lambda: show("4"),text = "4", width = 50, height = 2, font = font1, fg_color="#b5520b", hover_color= "#b5520b", text_color='white')
Button4.place(x = 10, y =120)

Button5 = customtkinter.CTkButton(master = app,command=lambda: show("5"),text = "5", width = 50, height = 2, font = font1, fg_color="#b5520b", hover_color= "#b5520b", text_color='white')
Button5.place(x = 70, y =120)

Button6 = customtkinter.CTkButton(master = app, command=lambda: show("6"),text = "6", width = 50, height = 2, font = font1, fg_color="#b5520b", hover_color= "#b5520b", text_color='white')
Button6.place(x = 130, y =120)

Button7 = customtkinter.CTkButton(master = app,command=lambda: show("7"),text = "7", width = 50, height = 2, font = font1, fg_color="#b5520b", hover_color= "#b5520b", text_color='white')
Button7.place(x = 10, y =180)

Button8 = customtkinter.CTkButton(master = app, command=lambda: show("8"),text = "8", width = 50, height = 2, font = font1, fg_color="#b5520b", hover_color= "#b5520b", text_color='white')
Button8.place(x = 70, y =180)

Button9 = customtkinter.CTkButton(master = app, command=lambda: show("9"),text = "9", width = 50, height = 2, font = font1, fg_color="#b5520b", hover_color= "#b5520b", text_color='white')
Button9.place(x = 130, y =180)

Button0 = customtkinter.CTkButton(master = app, command=lambda: show("0"),text = "0", width = 50, height = 2, font = font1, fg_color="#b5520b", hover_color= "#b5520b", text_color='white')
Button0.place(x = 70, y =240)

ButtonPlus = customtkinter.CTkButton(master = app,command=lambda: show("+"),text = "+", width = 50, height = 2, font = font1, fg_color="#b5520b", hover_color= "#b5520b", text_color='white')
ButtonPlus.place(x = 190, y =60)

ButtonMinus = customtkinter.CTkButton(master = app,command=lambda: show("-"),text = "-", width = 50, height = 2, font = font1, fg_color="#b5520b", hover_color= "#b5520b", text_color='white')
ButtonMinus.place(x = 190, y =120)

ButtonMultiply = customtkinter.CTkButton(master = app,command=lambda: show("*"),text = "*", width = 50, height = 2, font = font1, fg_color="#b5520b", hover_color= "#b5520b", text_color='white')
ButtonMultiply.place(x = 190, y =180)

ButtonDivide = customtkinter.CTkButton(master = app,command=lambda: show("/"),text = "/", width = 50, height = 2, font = font1, fg_color="#b5520b", hover_color= "#b5520b", text_color='white')
ButtonDivide.place(x = 190, y =240)

ButtonEqual = customtkinter.CTkButton(master = app, command=lambda: show("="),text = "=", width = 50, height = 2, font = font1, fg_color="#b5520b", hover_color= "#b5520b", text_color='white')
ButtonEqual.place(x = 130, y =240)

ButtonClear = customtkinter.CTkButton(master = app,command=lambda: clear ,text = "C", width = 50, height = 2, font = font1, fg_color="#b5520b", hover_color= "#b5520b", text_color='white')
ButtonClear.place(x = 10, y =240)





app.mainloop()
