import argparse

from cowsay import cowsay

parser = argparse.ArgumentParser(prog="cow_say", 
                                description="This alternative to default cowsay")

parser.add_argument("text", 
                    type=str, 
                    help="The message.")

parser.add_argument("-f", 
                    help="Option specifies a particular cow picture file (''cowfile'') to use", 
                    default="default")

parser.add_argument("-e", 
                    help="The cow's eyes.", 
                    default="oo")

args = parser.parse_args()

print(cowsay(message=args.text,
             cow=args.f,
             eyes=args.e))