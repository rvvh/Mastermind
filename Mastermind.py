# Mastermind
# 6 options in a 4 size code allowing for duplicates

from random import choice

#Fill array with all possible solution at the start of a game
#Returns an array with all possible solution 
def all_options():
    for i in range (1,7):
        for j in range (1,7):
            for k in range(1,7):
                for l in range (1,7):
                    options.append([i,j,k,l])
    return (options)

# Checking the attempt against the code
# Returns the amount of Black's and White's
def check(attempt,code):
    black=0
    white=0
    attempt_count=[0,0,0,0,0,0]
    code_count   =[0,0,0,0,0,0]
# count the number frequency
    attempt = list(map(int, attempt))
    code    = list(map(int, code))
    
    for i in range(4):
        code_count   [code[i]-1]+=1
        attempt_count[attempt[i]-1]+=1

# count the black's and white's
    for i in range (4):
        if code[i]==attempt[i]:
            black +=1
            code_count[attempt[i]-1]-=1
    for i in range (6):
            white += min (attempt_count[i-1], code_count[i-1])
    return (black, white)

# Removes all impossible solutions from solutions that do not provide the same result in Black's and White's
# Returns an array with the remaining possible solutions
def eliminate (attempt, options, black, white):
    opts=[]
    count =[]
    for i in range (len(options)):
        bl,wh=check (attempt, options[i])
        if (bl==black and wh==white):
            opts.append(options[i])
    return (opts)

# Start

# Create all possible options
options = []
options=all_options()

# Pick a random code from the possible options
code = choice (options)

print ("Code:",code)

# Define a first attempt
attempt = [1,1,2,2]

n=0
while len(options)>1:
    n+=1
    
    black, white= check (attempt, code)
    print ("Attempt",n, attempt, "Black:", black, "White:", white)
    
    options = eliminate (attempt, options, black, white)
    print ("Remaining options:",len(options))

    attempt = choice (options)
    
print ("Attempt",n+1, attempt, "Black: 4", "White: 0")