inputname = input("Please enter your name .. ")
vowelscount= 0
for i in inputname:
    if i in "AEIOUaeiou":
        vowelscount +=1
        
    
print(f"Number of vowels = {vowelscount}")    
