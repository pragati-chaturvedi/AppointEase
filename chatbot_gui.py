import customtkinter as ctk
import tkinter as tk
from chatbot import chatbot

def send_message():
    user_input = user_entry.get()
    if user_input.strip() != "":
        chat_history.configure(state='normal')  # Enable editing
        chat_history.insert(tk.END, f"You: {user_input}\n")
        user_entry.delete(0, tk.END)
        #Get chatbot response
        response = chatbot(user_input)
        chat_history.insert(tk.END, f"ChatBot: {response}\n")
        #Chat divider
        chat_history.insert(tk.END, "-"*40 + "\n", "divider")
        chat_history.configure(state='disabled')  #Disable editing

# Create main window
root = ctk.CTk()
root.title("Pragati's Appointment Booking System")
root.geometry("400x600")

# Create chat history box
chat_history = ctk.CTkTextbox(master=root, wrap = 'word', width=400, height=500)
chat_history.pack(pady=10)
chat_history.configure(state='disabled')  # Start as read-only


#insert initial greeting message
chat_history.configure(state='normal')  # Enable editing
chat_history.insert(tk.END, "ChatBot: Welcome to Pragati's Appointment System,how can I help you today?\n", "bot")
chat_history.insert(tk.END, "-"*40 + "\n", "divider")
chat_history.configure(state='disabled')  # Disable editing

# Create user input entry box
user_entry = ctk.CTkEntry(master=root, width=350, height=30)
user_entry.pack(side=tk.LEFT, padx=(10, 0))

# Create send button
send_button = ctk.CTkButton(master=root, text="⤴", width=50, height=30, command=send_message)
send_button.pack(side=tk.LEFT, padx=(5, 10))

# Run the main loop
root.mainloop()
