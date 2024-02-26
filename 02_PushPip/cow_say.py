import argparse

from cowsay import cowsay, list_cows

parser = argparse.ArgumentParser(prog="cow_say", 
                                description="This alternative to default cowsay")

parser.add_argument("text", 
                    type=str, 
                    help="The message.",
                    nargs="?")

parser.add_argument("-f", 
                    help="Option specifies a particular cow picture file (''cowfile'') to use.", 
                    default="default")

parser.add_argument("-e", 
                    help="The cow's eyes.", 
                    default="oo")

parser.add_argument("-T", 
                    help="Tongue configuration string.", 
                    default="  ")

parser.add_argument("-n", 
                    help="Wrap text configuration.", 
                    action="store_false")

parser.add_argument("-W", 
                    help="The width of the text bubble.", 
                    type=int, 
                    default=40)

parser.add_argument("-l", help="Show available cow characters.", action="store_true")

args = parser.parse_args()

if args.l :
    print(list_cows())
else:
    print(cowsay(message=args.text,
                cow=args.f,
                eyes=args.e,
                tongue=args.T,
                wrap_text=args.n,
                width=args.W))