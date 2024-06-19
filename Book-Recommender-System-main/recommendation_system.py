# -*- coding: utf-8 -*-
'''
Program: recommendation_system.py. 

Programmer: Omar Shatrat

Date: 11/28/2022

Description: Program recommends books to users based on their similarty score of other users

'''

import sys

def construct_ratings():
    # Generates a list of all unique book names in the file. Returns list of books and dictionary of records
    try:
        ratings = open('ratings.txt').readlines()
    except FileNotFoundError:
        print('File not found. Program aborted.')
        sys.exit()
    books = set()
    indiv = set()
    for i in range(0, len(ratings), 3):
        rating = ratings[i + 1].strip()
        books.add(rating)
    books = list(books)
    
    for i in range(0, len(ratings), 3):
        name = ratings[i].strip()
        indiv.add(name)
    indiv = list(indiv)

    
    # Creates a dictionary of user -> list ratings
    #6. Create a dictionary of user -> list ratings
    records = {}
        
    #7. Loop through lines again to get user names and ratings on every third line
    for i in range(0, len(ratings), 3):
    # 8. If the user is not in the dictionary, add them and initialize their ratings to 0 for each book
        name = ratings[i].strip()
        book = ratings[i+1].strip()
        rate = ratings[i+2].strip()
        if name not in records:
            records[name] = [0] * len(books)
        #9. Set the user's rating for the book
            for w in range(len(books)):
                if books[w] == book:
                    records[name][w] = rate   
        else:
            for w in range(len(books)):
                if books[w] == book:
                    records[name][w] = rate
    
    #10. Return the list of books and the dictionary of ratings
    return books, records

def Sort_Tuple(tup):
        # Getting length of list of tuples. Returns sorted tuple
        lst = len(tup)
        for i in range(0, lst): 
            for j in range(0, lst-i-1):
                if (tup[j][1] > tup[j + 1][1]):
                    temp = tup[j]
                    tup[j]= tup[j + 1]
                    tup[j + 1]= temp
        return tup
    
def averages(books, ratings):
    # Creates list with average ratings for each book. Returns sorted list
    avgs = []
    # Initialize list of lists (lol) where non-zero ratings for each book is stored in its own list
    lol = [[] for i in range(54)]
    
    # Iterate over dictionary to find qth value for each key and append it
    for q in range(len(books)):
        for i in ratings.keys():
            if ratings[i][q] != 0:
                lol[q].append(int(ratings[i][q]))
    
    # Takes averages of the lists within lol and appends them to avgs
    for i in lol:
        avgs.append( round(sum(i) / len(i), 2) )
    
    # Final list of tuples
    final = []
    for i in range(len(avgs)):
        final.append( (books[i], avgs[i]) )
    
    sorted = Sort_Tuple(final)
    sorted.reverse()
    return sorted

def dot(K, L):
    # Finds dot product of two lists, return it
        if len(K) != len(L):
            return 0
        return sum(i[0] * i[1] for i in zip(K, L))
   
def intify(lst):
    # Makes every element in a list into an integer, if applicable. Returns new list
    list1 = []
    for i in lst:
        i = int(i)
        list1.append(i)
    return list1

def similarities(user, ratings):
   # Calculates similarity scores within records dictionary. Returns list of similarity scores
    person = intify(ratings[user]) 
    
    sims = []
    
    # For loop excludes the user from the final list
    for i in ratings.keys():
        if i != user:
            sims.append( (i, dot(person, intify(ratings[i]))) )
    
    sims = Sort_Tuple(sims)
    sims.reverse()
    return sims
        
def recommended(sims, books, ratings):
    # Using the top 3 similar users, the function calculates their average book scores. Returns list
    top3 = sims[0:3]
    # List to be populated with average scores later
    lst = [ (i-i) for i in range(len(books))]
    
    for i in range(len(lst)):
        one = ratings[top3[0][0]][i]
        two = ratings[top3[1][0]][i]
        three = ratings[top3[2][0]][i]
        
        # Deals with issue of ratings of 0
        zerocnt = 0
        sums = 0
        if one == 0:
            zerocnt += 1
        else:
            sums += int(one)
        
        if two == 0:
            zerocnt += 1
        else:
            sums += int(two)
            
        if three == 0:
            zerocnt += 1
        else:
            sums += int(three)
        
        if zerocnt != 3:
            avg = sums / (3 - zerocnt)
            lst[i] = round(avg, 2)
    
    final = []
    
    for i in range(len(lst)):
        final.append( (books[i], lst[i]) )
    
    final = Sort_Tuple(final)
    final.reverse()
    return final
            
def print_pretty(lis):
    # Prints elements in an appealing manner, with a space in between
    for i in range(len(lis)):
        print(lis[i][0], '', lis[i][1])
            

def main():
    # Executes all previous functions with a menu UI
    books, ratings = construct_ratings()
    avgs = averages(books, ratings)
    
    print("Welcome to the CS131B Book Recommender. Type the word in the")
    print("left column to do the action on the right.")
    print("recommend : recommend books for a particular user")
    print("averages  : output the average ratings of all books in the system")
    print("quit      : exit the program")

    flag = ""
    while flag != "quit":
        flag = input("next task? ")
        if flag == "recommend":
            user = input("user? ")
            if user in ratings:
                sims = similarities(user, ratings)
                recs = recommended(sims, books, ratings)
                print_pretty(recs)
            else:
                print_pretty(avgs)
        elif flag == "averages":
            print_pretty(avgs)
        print()
    
main()   

'''Sample run

Welcome to the CS131B Book Recommender. Type the word in the
left column to do the action on the right.
recommend : recommend books for a particular user
averages  : output the average ratings of all books in the system
quit      : exit the program

next task? recommend

user? Ben
The Bourne Series  5.0
The Lord of the Rings  5.0
Holes  5.0
The Lion the Witch and the Wardrobe  5.0
Ender's Game  5.0
The Hobbit  5.0
My Sister's Keeper  5.0
Sabriel  5.0
Harry Potter Series  5.0
The Hitchhiker's Guide To The Galaxy  4.33
To Kill a Mockingbird  4.33
The Princess Bride  4.0
Watership Down  4.0
The Golden Compass  3.67
The Da Vinci Code  3.67
The War Of The Worlds  3.67
Hatchet  3.0
Shattered  3.0
Flowers For Algernon  3.0
Inkheart  3.0
Eragon  2.33
The Chrysalids  2.0
The Great Gatsby  1.67
Lord of the Flies  1.67
Bleach (graphic novel)  1.0
Speak  1.0
Life of Pi  1.0
The Sisterhood of the Travelling Pants  1.0
Dinotopia: A Land Apart from Time  0
I Know Why the Caged Bird Sings  0
Neuromancer  0
Practical Magic  0
Owl in Love  0
The Shadow Club  0
Thirteen Reasons Why  0
The Hunt for Red October  0
Shonen Jump Series  0
The Hunger Games  0
Ranger's Apprentice Series  0
Nineteen Eighty-Four (1984)  0
The Summer Tree  0
The Joy Luck Club  0
Maus: A Survivor's Tale  0
Kiss the Dust  0
Far North  0
Dealing with Dragons  0
A Great and Terrible Beauty  0
Naruto  0.0
The Five People You Meet in Heaven  0
Foundation Series  0
The Princess Diaries  -1.0
Twilight Series  -1.67
Bone Series  -3.0
Brave New World  -3.0


next task? recommend

user? aalison
Sabriel  4.0
The Bourne Series  3.86
The Hitchhiker's Guide To The Galaxy  3.83
Ender's Game  3.81
My Sister's Keeper  3.8
Harry Potter Series  3.61
Hatchet  3.58
Holes  3.57
The Princess Bride  3.5
The Lion the Witch and the Wardrobe  3.24
The Lord of the Rings  3.04
The Hunt for Red October  3.0
Shonen Jump Series  3.0
The Summer Tree  3.0
Maus: A Survivor's Tale  3.0
The Hobbit  2.85
The War Of The Worlds  2.83
Nineteen Eighty-Four (1984)  2.83
Inkheart  2.77
The Golden Compass  2.76
Eragon  2.72
Flowers For Algernon  2.62
Dealing with Dragons  2.6
Foundation Series  2.57
The Joy Luck Club  2.56
The Hunger Games  2.5
A Great and Terrible Beauty  2.5
Neuromancer  2.38
Bleach (graphic novel)  2.33
Shattered  2.33
The Da Vinci Code  2.25
Bone Series  2.06
Brave New World  1.88
The Five People You Meet in Heaven  1.83
To Kill a Mockingbird  1.77
Watership Down  1.7
The Great Gatsby  1.58
The Chrysalids  1.56
Naruto  1.52
Ranger's Apprentice Series  1.4
Lord of the Flies  1.36
Owl in Love  1.0
Speak  1.0
Kiss the Dust  1.0
Far North  1.0
The Princess Diaries  0.9
Dinotopia: A Land Apart from Time  0.5
Twilight Series  0.47
The Sisterhood of the Travelling Pants  0.43
Practical Magic  0.33
Life of Pi  0.22
The Shadow Club  0.0
I Know Why the Caged Bird Sings  -0.33
Thirteen Reasons Why  -0.33


next task? averages
Sabriel  4.0
The Bourne Series  3.86
The Hitchhiker's Guide To The Galaxy  3.83
Ender's Game  3.81
My Sister's Keeper  3.8
Harry Potter Series  3.61
Hatchet  3.58
Holes  3.57
The Princess Bride  3.5
The Lion the Witch and the Wardrobe  3.24
The Lord of the Rings  3.04
The Hunt for Red October  3.0
Shonen Jump Series  3.0
The Summer Tree  3.0
Maus: A Survivor's Tale  3.0
The Hobbit  2.85
The War Of The Worlds  2.83
Nineteen Eighty-Four (1984)  2.83
Inkheart  2.77
The Golden Compass  2.76
Eragon  2.72
Flowers For Algernon  2.62
Dealing with Dragons  2.6
Foundation Series  2.57
The Joy Luck Club  2.56
The Hunger Games  2.5
A Great and Terrible Beauty  2.5
Neuromancer  2.38
Bleach (graphic novel)  2.33
Shattered  2.33
The Da Vinci Code  2.25
Bone Series  2.06
Brave New World  1.88
The Five People You Meet in Heaven  1.83
To Kill a Mockingbird  1.77
Watership Down  1.7
The Great Gatsby  1.58
The Chrysalids  1.56
Naruto  1.52
Ranger's Apprentice Series  1.4
Lord of the Flies  1.36
Owl in Love  1.0
Speak  1.0
Kiss the Dust  1.0
Far North  1.0
The Princess Diaries  0.9
Dinotopia: A Land Apart from Time  0.5
Twilight Series  0.47
The Sisterhood of the Travelling Pants  0.43
Practical Magic  0.33
Life of Pi  0.22
The Shadow Club  0.0
I Know Why the Caged Bird Sings  -0.33
Thirteen Reasons Why  -0.33


next task? quit

'''
