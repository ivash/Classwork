module lshift210 (DI, SO); 
input  [31:0] DI; 

output [9:0] SO; 
reg    [9:0] SO; 


  always @(DI) 
  begin 
	SO <= DI << 2;
  end 
endmodule