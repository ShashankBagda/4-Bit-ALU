import tkinter as tk
from PIL import Image, ImageTk
import subprocess


def write_to_file():
    # Get the input strings from the entry fields
    input1 = entry1.get()
    input2 = entry2.get()

    # Validate input strings
    if not is_valid_binary(input1) or not is_valid_binary(input2):
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Invalid input. Please enter 4-bit binary numbers only.\n")
        return

    # Write the input strings to a file
    with open("a.txt", "w") as file:
        file.write(input1)
    with open("b.txt", "w") as file:
        file.write(input2)

    # Run the Verilog simulation and capture output
    result = subprocess.run("python code_generator.py && iverilog verilog.v && vvp a.out", 
                            shell=True, capture_output=True, text=True)

    # Display the output in the text widget
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, result.stdout)


def is_valid_binary(input_str):
    # Check if input string is a valid 4-bit binary number
    return len(input_str) == 4 and all(char in "01" for char in input_str)


# Create the main application window
root = tk.Tk()
root.title("4 Bit ALU")
root.geometry("615x460")

# Load background image
background_image = Image.open("background.jpg")
# Resize the image to fit the window size
background_image = background_image.resize((615, 460), Image.BILINEAR)
background_photo = ImageTk.PhotoImage(background_image)

# Create a label for the background image
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create labels and entry fields for input strings
label1 = tk.Label(root, text="   Input Value A   ", font=("Helvetica", 12))
label1.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry1 = tk.Entry(root, font=("Helvetica", 12))
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = tk.Label(root, text="   Input Value B   ", font=("Helvetica", 12))
label2.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry2 = tk.Entry(root, font=("Helvetica", 12))
entry2.grid(row=1, column=1, padx=5, pady=5)

# Create a button to trigger writing to file
write_button = tk.Button(root, text="Submit", command=write_to_file, font=("Helvetica", 12))
write_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

# Add a separator
separator = tk.Frame(height=2, bd=1, relief="sunken")
separator.grid(row=3, column=0, columnspan=2, sticky="we", padx=5, pady=5)

# Add a label for the output section
output_label = tk.Label(root, text="Simulation Output:", font=("Helvetica", 14, "bold"))
output_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Add a text widget to display simulation output
output_text = tk.Text(root, width=60, height=15, font=("Courier", 12))
output_text.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()
