import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")



root = customtkinter.CTk()
root.title("PomoTODOro")
root.geometry("500x350")

def add():
    print("Added todo")
    entry1.delete(0, "end")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Add here your todo's")
label.grid(row=0, column=0, sticky="nsew")

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="enter todo...")
entry1.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

button = customtkinter.CTkButton(master=frame, text="ADD", command=add)
button.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Done")
checkbox.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

root.mainloop()
