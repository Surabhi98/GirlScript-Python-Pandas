#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Simple TicTacToe game in Python - EAO
#In this game, you will be required to fill in the missing bits and commit you code weekly
# Please fill in the missing prompts every week as directed

#WEEK 1
import random
import sys

board=[i for i in range(0,9)]
player, computer = '',''

# Corners, Center and Others, respectively
moves=((1,7,3,9),(5,),(2,4,6,8))
# Winner combinations - think about what combinations will make you WIN the game!!
winners=((1,5,9),(1,2,3),(1,4,7), (2,5,8), (3,6,9), (4,5,6), (7,8,9), (7,5,3)) 
# Table
tab=range(1,10)


# In[3]:


#WEEK 1
#snippet to print the board
def print_board():
    x=1  #think about what value can variable x have, Hint: Integer
    for i in board:
        end = ' | '
        if x%3 == 0:
            end = ' \n'
            if i != 1: end+='---------\n';
        char=' '
        if i in ('x','o'): char=i;  #Think about what values do we will the grid with
        x+=1                         #what value will x increment each time
        print(char,end=end)
print_board()


# In[ ]:




