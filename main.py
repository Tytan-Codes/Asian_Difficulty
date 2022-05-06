import sys
import os


def main():
    print('(1) Easy mode')
    print('(2) Medium mode')
    print('(3) Hard mode ') 
    print('(4) Asian mode')
    
    main = (int(input('What mode do you want to play: ')))
    
    #WTF IS HAPPENING
    
    if main == 1:
        easy()
        
    if main == 2:
        medium()
    
    if main == 3:
        hard()
    
    if main == 4:
        ASIAN()
     #WTF IS HAPPENING END
    

       
# MODES eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee


def easy():
    print('What a disaster')
    
    
def medium():
    print('STUPID')
    

def hard():
    print('What a disappointment')
    
def ASIAN():
    asian = str(input('A leaf is falling from the tree. What do you do? '))
    print('(1) Run')
    print('(2) Hide')
    print('(3) Stay where you are')
    print('(4) Call 911')
    
    if asian == '1':
        print('You tripped on a branch and you DIED ')
    
    if asian == '2':
        print('You died from low blood in your brain ')
    
    if asian == '3':
        print('The leaf hit you, but you did not know that there was poison on the leaf. The poison killed you')
    
    if asian == '4':
        print('The police sentenced you to death from prank calling')
# MODES ENDS eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee


main()
    
