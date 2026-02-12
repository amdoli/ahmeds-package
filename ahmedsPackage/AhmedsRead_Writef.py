import os 
import time

# to chose a file
def choosing_a_file():
    print(os.listdir())
    print("which file do you want me to read:\n")
    while True:
        file=input("")
        if file in os.listdir():
            break
        else:
            print("there is no file with that name!")
            time.sleep(0.5)
            print("please try again:")
    return file
    
# I did this one at the biggening just to test the read not to write but I don't want to change it
# instead I will write another func for the challenge and will let this one just for reading only without writing!
def AhmedsRead_Write():
    time.sleep(0.5)
    totalWord=0
    totalChar=0
    lines=0
    alllines=""
    reverse_line=""
    while True:
        File=choosing_a_file()
        # here the program read a file 
        try:
            with open(File, "r") as file:
                for line in file:
                    alllines+=line
                    totalWord+=(len(line.split()))
                    totalChar+=(len(line))
                    lines+=1
                    reverse_line+=line.rstrip("\n")[::-1]+"\n"
                break
        except IsADirectoryError:
            time.sleep(0.5)
            print("that's a directory not a file!")
            time.sleep(1)
    freq=counting_words(alllines)
    largest=largest_word(alllines)
    average=avg(totalChar,totalWord)
    while True:
        time.sleep(0.5)
        print("do you want the output to be in seperate file (Output.txt)? [yes,no]\n")
        answer=input("")
        time.sleep(0.5)
        # write in a output.txt file
        if answer.lower() in ["y","yes","yup"]:
            write(totalChar,totalWord,lines,freq,largest,average,reverse_line)
            break
        # read only
        if answer.lower() in ["n","no",]:
            print(f"\ntotal characters: {totalChar}")
            print(f"total words: {totalWord}")
            print(f"total lines: {lines}")
            print(f"Most common words: {freq} times")
            print(f"Longest word: {largest}")
            print(f"Average word length: {average}")
            print(f"\nReversed content (line by line):\n{reverse_line}")
            break
    
# to count the frequncy
def counting_words(paragraph):
    freq={}
    for word in paragraph.split():
        if word not in freq.keys():
            freq[word]=0
        freq[word]+=1
    most_freq=0
    for words in freq:
        if most_freq < freq.get(words):
            most_freq = freq.get(words)
    return most_freq

# to get the largest word
def largest_word(words):
    words=words.split()
    longest=0
    longest_word=''
    for word in words:
        if longest < len(word):
            longest = len(word)
            longest_word = word
    return longest_word
    #print(f"\n the longest word is {longest_word} which has {longest} char")

# to get the average
def avg(total_char,total_words):
    total_char=int(total_char)
    total_words=int(total_words)
    average= round(total_char/total_words,2)
    return average

# to write in new file which I name it ("Output.txt")
def write(totalChar,totalWord,lines,freq,largest,average,reverse_line):
    with open("Output.txt","w") as file:
        file.write(f"\ntotal characters: {totalChar}\n")
        file.write(f"total words: {totalWord}\n")
        file.write(f"total lines: {lines}\n")
        file.write(f"Most common words: {freq} times\n")
        file.write(f"Longest word: {largest}\n")
        file.write(f"Average word length: {average}\n")
        file.write(f"\nReversed content (line by line):\n{reverse_line}\n")
    print("the file created succesfully!")









