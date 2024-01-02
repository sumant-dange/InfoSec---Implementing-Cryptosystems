import tkinter as tk
from tkinter import scrolledtext

def start_server():
    """Function to start the server (dummy action)."""
    display_message("Server started.")

def stop_server():
    """Function to stop the server (dummy action)."""
    display_message("Server stopped.")

def display_message(message):
    """Display messages in the text box."""
    text_box.insert(tk.END, message + "\n")

def run_gui():
    # Create the GUI window
    root = tk.Tk()
    root.title("Server Control Panel")

    # Create a text box to display messages
    global text_box
    text_box = scrolledtext.ScrolledText(root, width=50, height=20)
    text_box.pack(padx=10, pady=10)

    # Create "Start Server" button
    start_btn = tk.Button(root, text="Start Server", command=start_server)
    start_btn.pack(pady=10)

    # Create "Stop Server" button
    stop_btn = tk.Button(root, text="Stop Server", command=stop_server)
    stop_btn.pack(pady=10)

    # Run the GUI
    root.mainloop()

if __name__ == "__main__":
    run_gui()
