# Mastermind 07JUN20
# Cracking a Length 4 code with 6 [1-6] Options with Duplicates allowed (1296 options)
# This routine starts with choice [1,1,2,2] and removes all solutions from s that do not have the same number of black and white.
# It will randomly pick a remaining option from s and repeat till only one option, the solution, remains.
# Utilizing the Knuth routine it will always solve the code in 5 attempts or less

from random import choice
import time
import numpy as np

# Fill array s with all possible solution at the start of the game
# Returns an array with all possible solutions s
def solutions():

    s = []
    for i in range (1,7):
        for j in range (1,7):
            for k in range(1,7):
                for l in range (1,7):
                    s.append([i,j,k,l])
    return (s)

# Checking the guess against the secret
# Returns the amount of Black's and White's
def check(guess, secret):
    black=0
    white=0
    secret_count= [0,0,0,0,0,0]
    guess_count = [0,0,0,0,0,0]

# count the number frequency
    for i in range(4):
        secret_count [secret[i]-1]+=1
        guess_count  [guess [i]-1]+=1

# count the black's and remove them so they don't count as white's 
    for i in range (4):
        if  secret[i] == guess[i]:
            black +=1
            secret_count [secret[i]-1]-=1
            guess_count  [guess [i]-1]-=1  

# count the whites    
    for i in range (6):
            white += min (guess_count[i], secret_count[i])
    return (black, white)

# Removes all impossible solutions not providing the same result in Black's and White's
# Returns an array with the remaining possible solutions
def eliminate (guess, s, black, white):
    opts=[]
    for i in range (len(s)):
        b,w = check (guess, s[i])
        if (b==black and w==white):
            opts.append(s[i])
    return (opts)

# This routine optimizes the next guess to assure a win in 5 guesses or less.
# The routine may even choose a guess guaranteed not to win, but necessary to finish in 5 guesses
def minmax (s_w_g,s):
    t=np.zeros(len(s_w_g))
    for i in range (len(s_w_g)):
        t[i]= 0       
        for black in range(4):
            for white in range(5-black):
                temp = len(eliminate(s_w_g[i],s,black,white))    
                if (temp > t[i]): t[i] = temp
    new_guess=s_w_g[np.argmin(t)]
    return (new_guess)
    
# Start

# Create all possible options
s = solutions()
s_w_g=s.copy()

# Pick a random secret
secret = choice (s)

print ("Code:  ",secret)

# Define a first guess
guess   = [1,1,2,2]
guesses = 0

while len(s)>1:
    guesses+=1
    b=0
    w=0
    s_w_g.remove(guess)
    black, white = check (guess, secret)
    s = eliminate (guess, s, black, white)
    print ("Guess",guesses, guess, "Black:", black, "White:", white, "Secret codes remaining:",len(s))
    guess = minmax (s_w_g, s)

print ("Secret:", guess,"found in",guesses+1,"guesses")
