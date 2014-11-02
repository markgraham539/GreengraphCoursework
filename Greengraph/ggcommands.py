from argparse import ArgumentParser
from greengraph import greengraphMain

def process():
   parser = ArgumentParser(description = "Plots a png of green-ness on straight line from locations start to end")

   parser.add_argument('--start', '-s')
   parser.add_argument('--end', '-e')

   arguments= parser.parse_args()

   greengraphMain(arguments.start, arguments.end)

if __name__ == "__main__":
    process()