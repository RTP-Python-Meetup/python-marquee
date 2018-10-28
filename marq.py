import os
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
            line.strip() for line in text.split('\n'))
        self.width = max(tuple(len(line) for line in self.lines))
        term_size = os.popen('stty size', 'r').read().split()
        self.term_size = (int(term_size[0]), int(term_size[1]))

    def run(self):
        offset = 0
        print()
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
        

marq = Marquee(marq_text)

marq.run()
