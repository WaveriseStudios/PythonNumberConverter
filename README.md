# PythonNumberConverter
A simple python script, made for testing purposes, to convert any number in DEC, BIN or HEX into any of DEC, BIN or HEX based on an enum.
Supported conversion types :
- DEC_TO_BIN
- DEC_TO_HEX
- BIN_TO_DEC
- BIN_TO_HEX
- HEX_TO_DEC
- HEX_TO_BIN
#
How to use it ?

print(convert_number("42", ConversionType.DEC_TO_BIN))   = "101010" <br />
<br />
print(convert_number("42", ConversionType.DEC_TO_HEX))   = "2A"<br />
<br />
print(convert_number("101010", ConversionType.BIN_TO_DEC))  = "42"<br />
<br />
print(convert_number("101010", ConversionType.BIN_TO_HEX))  = "2A"<br />
<br />
print(convert_number("2A", ConversionType.HEX_TO_DEC))   = "42"<br />
<br />
print(convert_number("2A", ConversionType.HEX_TO_BIN))   = "101010"

