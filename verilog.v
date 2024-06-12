
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
        A = 4'b1111;
        B = 4'b1101;

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
    