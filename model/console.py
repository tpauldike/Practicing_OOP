#!/usr/bin/env python3
import cmd, sys

class Pld(cmd.Cmd):
    '''
    A class for Pld
    '''
    intro = 'Welcome to PLD concole\nType "help" for more information'
    prompt = '==> '

    def do_EOF(self, line):
        '''End of File method'''
        return True

    def do_greet(self, name):
        '''
        greets the string passed as the argument
        '''
        print('hello {}'.format(name))

    def do_exit(self, line):
        '''exit method'''
        return True

if __name__ == '__main__':
    Pld().cmdloop()
