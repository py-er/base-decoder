## A tool to easily base decode/encode text

BaseMultiCoder is a tool used to repeatedly base encode or base decode text. This can be useful if a text has been continuously encoded multiple times with the same or different encoding formats. Additionally, this tool can be used to create an encoded text by repeatedly encoding the original text. You can choose to encode the text randomly using base16, base32, or base64 for each iteration, or use the same encoding format for every iteration.

### Features

-   Decode base64
-   Decode base32
-   Decode base16
-   Decode a mix of the above
-   Decode a string multiple timies in a row
-   Encode base16
-   Encode base32
-   Encode base64
-   Randomly encode with all of the above
-   Encode a string multiple timies in a row

### Usage
-   Decoder
```
python basemulticoder.py -fi/-si <input path>/<string do decode> -o <output path> -m decode
```
-   Encoder
```
python basemulticoder.py -fi/-si <input path>/<string do decode> -o <output path> -m encode16/encode32/encode64/encoderand -t <turns to encode strings>
```

### Examples
-   Decode a string
```
python basemulticoder.py -si dGVzdA== -o decoded.txt -m decode
```
This will decode this base64 string and return the decoded string test in the output file decoded.txt

-   Randomly encoding a file
```
python basemulticoder.py -fi input.txt -o output.txt -m encoderand -t 10
```
This will encode the string in the file input.txt, encode it 10 times randomly between base16, base32, base64 then write the final result to output.txt.