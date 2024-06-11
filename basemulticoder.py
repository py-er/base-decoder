import base64
import argparse
import random

## Decode base16
def decode16(message):
    try:
        decoded_message = base64.b16decode(message)
        return decoded_message
    except:
        return False

## Decode base32
def decode32(message):
    try:
        decoded_message = base64.b32decode(message)
        return decoded_message
    except:
        return False

## Decode base64
def decode64(message):
    try:
        decoded_message = base64.b64decode(message)
        return decoded_message
    except:
        return False
    
## Encode base16
def encode16(message):
    encoded_message = base64.b16encode(message)
    return encoded_message

## Encode base32
def encode32(message):
    encoded_message = base64.b32encode(message)
    return encoded_message

## Encode base64
def encode64(message):
    encoded_message = base64.b64encode(message)
    return encoded_message

## Encode random
def random_encoding(message):
    choises_list = ["encode16", "encode32", "encode64"]
    choises_dict = {"encode16": encode16(message), "encode32": encode32(message), "encode64": encode64(message)}
    return choises_dict[random.choice(choises_list)]

## Try decoding with all
def decode(message):
    decoded_message = message
    while True:
        last = decoded_message
        decoded_message = decode16(last)

        if decoded_message:
            continue
        else:
            decoded_message = decode32(last)

        if decoded_message:
            continue
        else:
            decoded_message = decode64(last)
        
        if decoded_message:
            try:
                decoded_message.decode("utf-8")
                continue
            except:
                decoded_message = last
                break
        else:
            decoded_message = last
            break
        
    return decoded_message

def encode(message, base, turns):

    if base == "16":
        for x in range(turns):
            message = encode16(message)

    elif base == "32":
        for x in range(turns):
            message = encode32(message)

    elif base == "64":
        for x in range(turns):
            message = encode64(message)

    elif base == "rand":
        for x in range(turns):
            message = random_encoding(message)

    return(message.decode("utf-8"))

def main(args):
    ## Input
    if args.input or args.text:
        if args.input:
            with open(args.input) as input_file:
                input = input_file.read()
        else:
            input = args.text
    else:
        print("Error: Need an input, use -fi or -ti. Use -h for more help.")
        return(None)

    ## Mode
    ## Decode
    if args.mode.lower() == "decode":
        output = decode(input)
        try:
            print(output.decode("utf-8"))
        except AttributeError:
            print("Input could not be decoded! Try changing mode!")
            return(None)
    ## Encode
    elif args.mode and args.turns:
        if args.mode.lower() == "encode16":
            output = encode(input.encode(), "16", args.turns)
        elif args.mode.lower() == "encode32":
            output = encode(input.encode(), "32", args.turns)
        elif args.mode.lower() == "encode64":
            output = encode(input.encode(), "64", args.turns)
        elif args.mode.lower() == "encoderand":
            output = encode(input.encode(), "rand", args.turns)
        else:
            print("Error: Need an mode (-m Decode/Encode) and turns (-et) for encodes. Use -h for more help.")
            return(None)    
        if not args.output:
            print(output)
    else:
        print("Error: Need an mode (-m Decode/Encode) and turns (-et) for encodes. Use -h for more help.")
        return(None)


    ## Output
    if args.output:
        with open(args.output, "w") as output_file:
            output_file.write(output)
        print ("Output has been saved!")
        return(None)


if __name__ == "__main__":
    ## Arguments setup
    parser = argparse.ArgumentParser()
    parser.add_argument("-fi", "--file", dest = "input", help="Input File")
    parser.add_argument("-ti", "--text", dest = "text", help="Input Text")
    parser.add_argument("-fo", "--output", dest = "output", help="Output File")
    parser.add_argument("-m", "--mode",dest = "mode", help="Mode (Decode/Encode16/Encode32/Encode64/EncodeRAND)")
    parser.add_argument("-et", "--turns", dest = "turns", help="Encoding Turns", type=int)
    args = parser.parse_args()

    ## Run main function
    main(args)