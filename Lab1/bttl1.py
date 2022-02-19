from goto import *
import time
import var
import pio
import resource
import Ports


def peripheral_setup():
    pio.terminal = Ports.SerialTerminal(9600)


def variable_setup():
    var.Name = ''


def peripheral_loop():
    pass

# main function


def main():
    peripheral_setup()
    pio.terminal.print('What is your name?\n')
    while True:
        var.Name = pio.terminal.input(True)
        if var.Name == "thay Thao dep giai":
            pio.terminal.print('Hello ' + var.Name)
            break
        pass


if __name__ == '__main__':
    main()
