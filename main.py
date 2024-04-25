import tkinter as tk
from PIL import Image, ImageTk
import subprocess

def write_to_file():
    input1 = entry1.get()
    input2 = entry2.get()

    if not is_valid_binary(input1) or not is_valid_binary(input2):
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Invalid input. Please enter 4-bit binary numbers only.\n")
        return

    with open("a.txt", "w") as file:
        file.write(input1)
    with open("b.txt", "w") as file:
        file.write(input2)

    result = subprocess.run("python code_generator.py && iverilog verilog.v && vvp a.out", 
                            shell=True, capture_output=True, text=True)

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, result.stdout)

def is_valid_binary(input_str):
    return len(input_str) == 4 and all(char in "01" for char in input_str)

root = tk.Tk()
root.title("4 Bit ALU")
root.geometry("625x625")

# Lock the window size
root.resizable(False, False)

# Load background image
background_image = Image.open("background.png")
background_image = background_image.resize((620, 620), Image.BILINEAR)
background_photo = ImageTk.PhotoImage(background_image)

# Create a label for the background image
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Labels and entry fields for input strings
label1 = tk.Label(root, text="Input Value A", font=("Helvetica", 12))
label1.grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root, font=("Helvetica", 12))
entry1.grid(row=0, column=1, padx=10, pady=5)

label2 = tk.Label(root, text="Input Value B", font=("Helvetica", 12))
label2.grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root, font=("Helvetica", 12))
entry2.grid(row=1, column=1, padx=10, pady=5)

# Submit button
write_button = tk.Button(root, text="Submit", command=write_to_file, font=("Helvetica", 12), bg="#4CAF50", fg="white")
write_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Separator
separator = tk.Frame(height=2, bd=1, relief="sunken")
separator.grid(row=3, column=0, columnspan=2, sticky="we", padx=10, pady=5)

# Output section label
output_label = tk.Label(root, text="Simulation Output", font=("Helvetica", 14, "bold"))
output_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Text widget for simulation output
output_text = tk.Text(root, width=60, height=15, font=("Courier", 12))
output_text.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
