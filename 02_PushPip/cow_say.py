import argparse

from cowsay import cowsay

parser = argparse.ArgumentParser(prog="cow_say", 
                                description="This alternative to default cowsay")

parser.add_argument("text", 
                    type=str, 
                    help="The message.")

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

args = parser.parse_args()

print(cowsay(message=args.text,
             cow=args.f,
             eyes=args.e,
             tongue=args.T,
             wrap_text=args.n))