import tkinter as tk
from PIL import Image, ImageTk
import subprocess

def code_generator():
    # Python code to generate Verilog testbench with values read from files

    a_val = entry1.get()
    b_val = entry2.get()

    # Generate Verilog testbench code with the read values
    verilog_code = f"""
    module four_bit_operations(
        input [3:0] A,        // 4-bit input A
        input [3:0] B,        // 4-bit input B
        output [7:0] Sum,     // 4-bit output Sum for addition
        output [7:0] Diff,    // 4-bit output Diff for subtraction
        output [7:0] Product, // 4-bit output Product for multiplication
        output [7:0] Quotient,// 4-bit output Quotient for division
        output [3:0] And,     // 4-bit output And for logical AND
        output [3:0] Or,      // 4-bit output Or for logical OR
        output [3:0] Xor,      // 4-bit output Xor for logical XOR
        output [3:0] not_a,      // 4-bit output Not for A
        output [3:0] not_b      // 4-bit output Not for B
    );

    // Dataflow modeling for addition
    assign Sum = A + B;

    // Dataflow modeling for subtraction
    assign Diff = A - B;

    // Dataflow modeling for multiplication
    assign Product = A * B;

    // Dataflow modeling for division
    assign Quotient = A / B;

    // Dataflow modeling for logical AND
    assign And = A & B;

    // Dataflow modeling for logical OR
    assign Or = A | B;

    // Dataflow modeling for logical XOR
    assign Xor = A ^ B;

    // Dataflow modeling for logical NOT
    assign not_a = ~A;
    assign not_b = ~B;

    endmodule


    module testbench;

    // Define signals
    reg [3:0] A, B;          // 4-bit input signals
    wire [7:0] Sum, Diff, Product, Quotient; // 8-bit output signals
    wire [3:0] And, Or, Xor, not_a, not_b; // 4-bit output signals

    // Instantiate the module under test
    four_bit_operations UUT(
        .A(A),
        .B(B),
        .Sum(Sum),
        .Diff(Diff),
        .Product(Product),
        .Quotient(Quotient),
        .And(And),
        .Or(Or),
        .Xor(Xor),
        .not_a(not_a),
        .not_b(not_b)
    );

    // Stimulus generation
    initial begin
    $display("");
        // Assign values to signals
        A = 4'b{a_val};
        B = 4'b{b_val};

        // Wait for some time for simulation to run
        #10;

        // Display output
        
        $display("Value of A = %b", A);
        $display("Value of B = %b", B);
        $display("");
        
        $display("Sum = %b", Sum);
        $display("");

        $display("Difference = %b", Diff);
        $display("");
        
        $display("Product = %b", Product);
        $display("");
        
        $display("Quotient = %b", Quotient);
        $display("");
        
        $display("AND = %b", And);
        $display("");
        
        $display("OR = %b", Or);
        $display("");

        $display("NOT of A = %b", not_a);
        $display("NOT of B = %b", not_b);
        $display("");
        
        $display("XOR = %b", Xor);
        $display("");
        
        // End simulation
        $finish;
    end

    endmodule
    """

    # Write the generated Verilog code to a file
    with open("verilog.v", "w") as file:
        file.write(verilog_code)


def write_to_file():
    input1 = entry1.get()
    input2 = entry2.get()

    if not is_valid_binary(input1) or not is_valid_binary(input2):
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Invalid input. Please enter 4-bit binary numbers only.\n")
        return

    code_generator()

    result = subprocess.run("iverilog verilog.v && vvp a.out", 
                            shell=True, capture_output=True, text=True)

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, result.stdout)

    subprocess.Popen(["gtkwave", "verilog.vcd"])

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

# Waveform display section
waveform_label = tk.Label(root, text="Waveform View", font=("Helvetica", 12, "bold"))
waveform_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

waveform_canvas = tk.Canvas(root, width=400, height=200, bg="lightgray")
waveform_canvas.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Function to display a placeholder message on the waveform canvas
def display_waveform_message(message):
  waveform_canvas.delete("all")
  waveform_text = waveform_canvas.create_text(waveform_canvas.winfo_width() / 2, 
                                               waveform_canvas.winfo_height() / 2, 
                                               text=message, font=("Helvetica", 12))
  waveform_canvas.bind("<Button-1>", lambda event: launch_gtkwave())  # Bind click event

# Initial message on waveform canvas
display_waveform_message("Click here to launch GTKWave")

def launch_gtkwave():
  # Clear any previous message
  waveform_canvas.delete("all")
  # Launch GTKWave process
  subprocess.Popen(["gtkwave", "verilog.vcd"])

root.mainloop()