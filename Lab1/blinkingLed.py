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
    var.Age = ''
    var.School = ''


def peripheral_loop():
    pass

# main function


def main():
    peripheral_setup()
    pio.terminal.print('What is your name?')
    var.Name = pio.terminal.input(True)
    pio.terminal.print('How old are you?')
    var.Age = pio.terminal.input(True)
    pio.terminal.print('Where do you study?')
    var.School = pio.terminal.input(True)
    pio.terminal.print('Hello ' + var.Name +
                       ', you are ' + var.Age + ' years old and study at ' + var.School)
    while True:
        peripheral_loop()
        time.sleep(0.1)
        pass


if __name__ == '__main__':
    main()
