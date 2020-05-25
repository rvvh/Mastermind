# Mastermind 25MAY20
# 6 options in a 4 size code and allowing for duplicates (1296 options)
# This routine starts with choice [1,1,2,2] and removes all solutions from s that do not have the same number of black and white
# It will randomly pick a remaining option from s and repeat till only one option, the solution, remains.

from random import choice
import time

# Fill array s with all possible solution at the start of the game
# Returns an array with all possible solutions s
def solutions():
    s=[]
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
    secret_count=[0,0,0,0,0,0]
    guess_count =[0,0,0,0,0,0]
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

# Removes all impossible solutions from solutions that do not provide the same result in Black's and White's
# Returns an array with the remaining possible solutions
def eliminate (guess, s, black, white):
    opts=[]
    for i in range (len(s)):
        b,w=check (guess, s[i])
        if (b==black and w==white):
            opts.append(s[i])
    return (opts)

# Start

# Create all possible options
s = solutions()
s_without_guesses=s.copy()

# Pick a random secret from the possible solutions
secret = choice (s)

print ("Code:  ",secret)

# Define a first guess
guess   = [1,1,2,2]
guesses = 0

while len(s)>1:
    guesses+=1
    b=0
    w=0
    black, white = check (guess, secret)
    print ("Guess",guesses, guess, "Black:", black, "White:", white, "Secret codes remaining:",len(s))

    s_without_guesses.remove(guess)
        
    s = eliminate (guess, s, black, white)
    
    guess = choice (s)
print ("Secret:", guess,"found in",guesses+1,"guesses")

# apply minimax routine to choose the next best option. 
# This might even pick a guess from the full set of options, knowing it does not belong to the possible solutions, to assure a better result overall.
# but this doesnt work yet, getting close though

'''
    t=[]
    for i in range (len(s)):
        for j in range (len(s_without_guesses)):
            black, white = check (s[i],s_without_guesses[j])
            o=[]
            c=0
            #check all possible b and w results
            for k in range (5):
                for m in range (b,5):
                    b,w = eliminate (s[i],s_without_guesses[j], k, m)
                    if (b==black and w==white):
                        c+=1
            t[i]+=c
'''