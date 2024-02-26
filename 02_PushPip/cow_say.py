import argparse

from cowsay import cowsay

parser = argparse.ArgumentParser(prog="cow_say", 
                                description="This alternative to default cowsay")

parser.add_argument("text", type=str, help="The message.")

args = parser.parse_args()

print(cowsay(message=args.text))