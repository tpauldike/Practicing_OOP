#!/usr/bin/env python3
import cmd, sys

class myShell(cmd.Cmd):
    '''
    A console created just to practice
    '''
    intro = "Welcome to my first console\nEnter 'help' to see available commands"
    prompt = '--> '

    def do_EOF(self, line):
        return True

    def do_greet(self, name='Topman'):
        self.name = name
        print(f'Good day {self.name}!')


if __name__ == '__main__':
    myShell().cmdloop()
