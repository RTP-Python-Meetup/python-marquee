#!/usr/bin/python3

import os
import sys
from time import sleep

marq_text = """██████╗ ████████╗██████╗     ██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗    ███╗   ███╗███████╗███████╗████████╗██╗   ██╗██████╗
██╔══██╗╚══██╔══╝██╔══██╗    ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║    ████╗ ████║██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗
██████╔╝   ██║   ██████╔╝    ██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║    ██╔████╔██║█████╗  █████╗     ██║   ██║   ██║██████╔╝
██╔══██╗   ██║   ██╔═══╝     ██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║    ██║╚██╔╝██║██╔══╝  ██╔══╝     ██║   ██║   ██║██╔═══╝
██║  ██║   ██║   ██║         ██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║    ██║ ╚═╝ ██║███████╗███████╗   ██║   ╚██████╔╝██║
╚═╝  ╚═╝   ╚═╝   ╚═╝         ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝     ╚═╝╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝"""

class Marquee(object):

    def __init__(self, text):
        self.lines = tuple(
            line for line in text.split('\n'))
        self.width = max(tuple(len(line) for line in self.lines))
        term_size = os.popen('stty size', 'r').read().split()
        self.term_size = (int(term_size[0]), int(term_size[1]))

    def run(self):
        offset = 0
        print('\n' * (self.term_size[0] - 1) +
                '\033[{}A'.format((self.term_size[0] + len(self.lines)) // 2))
        while True:
            for line in self.lines:
                if offset < 0:
                    print(" " * (-1 * offset) + line[:offset + self.term_size[1]])
                else:
                    print(line[offset:offset + self.term_size[1]])
            sleep(1/10)
            if offset < self.width:
                offset = offset + 1
            else:
                offset = 0 - self.term_size[1]
            print("\033[1A\033[K" * (len(self.lines) + 1))
        
def main():
    if len(sys.argv) > 1:
        marq_filename = sys.argv[1]
        with open(marq_filename, 'r') as marq_file:
            marq_text = marq_file.read()
    marq = Marquee(marq_text)
    marq.run()

if __name__ == '__main__':
    try:
        exit(main())
    except KeyboardInterrupt:
        print()
        exit()
