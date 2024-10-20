# Mastermind 07JUN20
# Cracking a Length 4 code with 6 [1-6] Options with Duplicates allowed (s = 1296 options)
# This routine starts with choice [1,1,2,2] and removes all solutions from s that do not have same number of black and white.
# Randomly picking a remaining option from s, repeating till one option, the solution, remains.
# Utilizing Knuth routine it will always solve the code in 5 attempts or less
# Mods 08APR21 Result formatting
# Mods 21SEP24 Added timer

from random import choice
import numpy as np
import time

# Fill array s with all possible solution at the start of game
# Returns an array with all possible solutions s
def solutions():
    s = []
    for i in range (1,7):
        for j in range (1,7):
            for k in range(1,7):
                for l in range (1,7):
                    s.append([i,j,k,l])
    return (s)

# Checking guess against secret
# Returns amount of Black's and White's
def check(guess, secret):
    black=0
    white=0
    secretcount= [0,0,0,0,0,0]
    guesscount = [0,0,0,0,0,0]

# count number frequency
    for i in range(4):
        secretcount [secret[i]-1]+=1
        guesscount  [guess [i]-1]+=1

# count Black's and remove so they don't count as White's 
    for i in range (4):
        if  secret[i] == guess[i]:
            black +=1
            secretcount [secret[i]-1]-=1
            guesscount  [guess [i]-1]-=1  

# count the Whites    
    for i in range (6):
            white += min (guesscount[i], secretcount[i])
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
def minmax (swg,s):
    t=np.zeros(len(swg))
    for i in range (len(swg)):
        t[i]= 0       
        for black in range(4):
            for white in range(5-black):
                temp = len(eliminate(swg[i],s,black,white))    
                if (temp > t[i]): t[i] = temp
    newguess=swg[np.argmin(t)]
    return (newguess)
    
# Start

# Create all possible options
s = solutions()
# Create copy swg of solutions set s
swg=s.copy()

# Pick a random secret code
secret = choice (s)
print ("                     | Black | White | Codes remaining |")

# Start timer
tic = time.perf_counter()

# Define a first guess. This initial guess is from the Knutt routine to assure success within 5 attempts
guess   = [1,1,2,2]
guesses = 1

while len(s)>1:
    b=0
    w=0
# Knutt routine requires a working copy of all remaining non used quesses, removing the guess from the set after each guess.
    swg.remove(guess)
# Return number of Blacks and Whites
    black, white = check (guess, secret)
# Remove all non potential solutions from s    
    s = eliminate (guess, s, black, white)
# Print last guess, number of Blacks and Whites and remaining potential solutions    
    print ("Guess",guesses, guess, "|  ",black,"  |  ", white, "  |",end=" ")
# Print alignment
    if len(s)<100: print (" ",end="")
    if len(s)<10 : print (" ",end="")
    print ("     ",len(s),"      |",)
#Account for first time right solution    
    if guess==s[0]: guesses-=1
# Update number of guesses
    guesses+=1
# Using  Knutt routine to optimize next guess    
    guess = minmax (swg, s)
# Present code and number of total guesses    
    if len(s)==1:
        toc = time.perf_counter()
        print ("Secret:", s[0],"found in",'{:.2f}'.format(toc - tic), "seconds and", guesses, "guess", end="")
# Print alignment for one or multiple guesses
        if guesses>1: print ("es")
