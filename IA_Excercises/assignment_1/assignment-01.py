# ==========================================================
# Artificial Intelligence.  ETSII (University of Seville).
# Course 2017-18
# Deliverable 01 
# ===========================================================


# Define, using Python, the functions asked in each exercise, using the blank
# space below the statement.

# IMPORTANT: DO NOT CHANGE THE NAMES EITHER TO THIS FILE OR TO THE FUNCTIONS
# ASKED IN EACH EXERCISE (in that case, the exercise will not be evaluated) 


# THIS ASSIGNMENT WORTHS 5% OF THE TOTAL GRADE


# *****************************************************************************
# ACADEMIC INTEGRITY AND CHEATING: the assignments are individual, and thus
# they have to be carried out independently by each student. SHARING CODE IS
# STRICTLY FORBIDDEN. It as also forbidden to use any third-party code,
# available on web or on any source, without the approval of the teacher.  

# Any plagiarism detected will result in a FINAL GRADE OF ZERO IN THE COURSE,
# for ALL the students involved, and it may lead to other disciplinary
# measures. Furthermore, the grades obtained until that moment will not be
# kept for future calls.  
# *****************************************************************************




# -----------------------------------------------------------------------------
# EXERCISE 1)

# Suppose we have a text file containing an ASCII representation of different
# digits written by hand. The digits.txt file provided is an example of this
# type of file, with 300 digit images written by hand.  We'll assume that each
# digit is represented by a 28x28 pixel image, where each pixel is represented
# by a character ("#" for a black pixel where the stroke has passed, " " for
# blank pixels)

# Define a function:

#(the only changes with respect the 1st call
#is that these 2 excersise are commented and the code of the 2nd improved a little)


def print_least_used_pixels(file,n):
    #inicialize a matrix to store the counter of each pixel
    counter = init_matrix(28,28)
    lineCounter=0
    charaCounter=0
    x = open(file) #open file to read it
    for line in x.readlines():
        for chara in line: #for each line, for each pixels it is checked if
            #there is a '#' or not 
            if chara=='#':#if there is a '#' then it is added 1 to the counter
                #in that pixel position (in the matrix that represents it)
                counter[lineCounter%28][charaCounter]+=1
            charaCounter+=1
        charaCounter=0 #reset after iteration
        lineCounter+=1
        
    buff='' #buffer for final print
    
    #lastly the matrix is prepared checking if the number in each pixel is
    #greater o lower than n (the input number). If it is higher then stores a 
    #blank ' ' else stores a '*'
    for x in range(28):
        for y in range(28):
            if counter[x][y]<n:
                buff+='*'
            else:
                buff+=' '
        buff+='\n' #new line
    print(buff) #print final result

#inicialize matrix (all 0)                
def init_matrix(w,h):
    return [[0 for x in range(w)] for y in range(h)]

# to print on screen a 28x28 image, in which the pixels where the stroke has
# passed less than n times (taking into account all the images of the file)
# are marked with a "*". That is to say, in the image that has to be printed, 
# we will write a "*" only on those pixel positions for which there are 
# fewer than n images in the file, whose stroke passes through that pixel.


# For example:

# >>> print_least_used_pixels("digits.txt",5)
# ****************************
# ****************************
# **********    **************
# *********            *******
# *******               ******
# ******                   ***
# ****                     ***
# ****                     ***
# ****                     ***
# ****                     ***
# ****                     ***
# ****                     ***
# ****                     ***
# ****                     ***
# ****                     ***
# *****                    ***
# ****                     ***
# *****                    ***
# *****                    ***
# *****                    ***
# *****                    ***
# *****                   ****
# *****                  *****
# ******                ******
# *******               ******
# ********            ********
# ************      **********
# ****************************

# >>> print_least_used_pixels("digits.txt",150)
# ****************************
# ****************************
# ****************************
# ****************************
# ****************************
# ****************************
# ************      **********
# ***********        *********
# **********         *********
# **********   **    *********
# ********** *****   *********
# ****************  **********
# ***************   **********
# *************     **********
# ***********       **********
# ************      **********
# ************       *********
# *************     **********
# **************    **********
# **************    **********
# *************     **********
# ************      **********
# ************     ***********
# *************   ************
# ****************************
# ****************************
# ****************************
# ****************************











# -----------------------------------------------------------------------------
# EJERCICIO 2)

# Suppose our department has bought a new computer that we're going to use as
# a server for practices. For that reason, we need to register the students as
# users of that server. To this end, we have to automatically generate a
# username for each student, based on his/her name and surnames (they are
# spanish students, so they have two surnames). 


# Define a function auto_usernames(file) such that receiving as input the name
# of a file containing the data of each user, it prints out a listing of them in
# alphabetical order of surnames, along with the automatically generated
# username.

#code improved
def auto_username(file):
    
    shortName,longName = process(file) #get the list of names from file 
    
    mapp = {}
    
    for name in shortName+longName: #both list are iterated
        if name[2] == 'NONE':
            #if there is 'NONE' in this position (not compound name)...
            adder(mapp,name[0],name[1],name[3],name[4]) #list of one-name people are added and has a username generated
        else:
            adder(mapp,name[0],name[1],name[3],name[4],name[2]) #list of one-name people are added and has a username generated
    
    toString(mapp)
    

#receives the name, surnames and the dict(called mapp) and return the auto
#generated username
def user(name,surname1,surname2,mapp):
    
    string = ''
    
    #get the first letter of each name (simple or compound names)
    for nameC in name.split(" "):
        string += nameC[0]
    
    string += surname1[0:3]+surname2[0:3] #get the 3 first letters of each surname
    
    string = string.lower() #they are lowered
    
    #now it is checked that the new autogenerated username is not repeated and
    #if it is repeated this is fixed adding a number behind
    for person in mapp:
        if mapp[person][2][-1].isdigit() and (mapp[person][2]==string or mapp[person][2][:-1]==string[:-1]):
            #if the person has a digit in the last position of its username and
            #is the same (just checking if it has a digit but not which)...
            if int(mapp[person][2][-1]) >= int(string[-1]):
                #if the digit from the dictionary (mapp) is higher or equal then the digit
                #is incremented and substitutes the digit of our autogenerated username
                string = string[:-1] + str(int(mapp[person][2][-1])+1)
                
        elif mapp[person][2] == string:
            #else it is repeated but with no number in the last position...
            string += '1'
            
    return string
    
#receives the txt file and return 2 list: 1 with people with 1 name (::) and 1 
#with compound names 
def process(file):
    f = open(file)
    onlyname=[]
    duoname=[]
    
    for line in f.readlines():
        if len(line.split('::'))==2:
            #if '::' it is a simple name
            if len(line.split(':'))==5:
                #if length is correct ...
                dni,name,none,surname1,surname2= line.split(':')
                onlyname.append([dni,name,'NONE',surname1,surname2])
        else:
            #else it is a compound name
            if len(line.split(':'))==5:
                #if length is correct ...
                dni,name,second,surname1,surname2= line.split(':')
                duoname.append([dni,name,second,surname1,surname2])
    #return 2 list nombreSolo->simple names and nombreCombo->compund names            
    return onlyname,duoname

#receives the main dict (already prepared) and print correctly the information
def toString(mapp):
    aux=''
    #first the header is printed
    print('DNI      Surnames                       Name            User ')
    print('-------- ------------------------------ --------------- --------')
    #then the dict is iterated and check if it has only surnames or 
    #also has a number in this case is not printed (the number)
    for element in sorted(mapp):
        if element[-1].isdigit():
            aux = element[:-1]
        else:
            aux = element
        print("{0:>8} {1:<30} {2:<15} {3}".format(mapp[element][0],aux,mapp[element][1],mapp[element][2]))

#reveives the dict where data will be stored, and some extra datta
def adder(mapp,dni,name,surname1,surname2,name2=""):
    
    surnames = surname1 + " " + surname2[:-1]
    
    for person in mapp:
        #check other people already added to the data structure (key -> surnames of a person)
        if person==surnames:
            #if there is other person with the same surnames...
            if person[-1].isdigit():
                #if the surname has a digit then get the number increment 1 and
                #add it to the new person (this way there is no repetition)
                surnames = str(int(person[-1])+1)
            else:
                surnames += '1' #if there is no name it is the first repeated (so we add number 1)
    
    if name2 == '':
        #if the person has a compound name...
        
        username = user(name,surname1,surname2,mapp)#get autogenerated username
        mapp[surnames]=[dni,name,username] #add info (array) <- value and surnames <- key
    else:
        username = user(name+" "+name2,surname1,surname2,mapp)#get autogenerated username
        mapp[surnames]=[dni,name+" "+name2,username] #add info (array) <- value and surnames <- key
        
# For example, applying the function auto_usernames to the file nombres.txt
# provided, the following lines has to be printed: 

# >>> auto_username("nombres.txt")
#
# DNI      Surnames                       Name            User 
# -------- ------------------------------ --------------- --------
# 67834547 Abad Garcia                    Maria Jose      mjabagar
# 87452221 Fernandez Lopera               Maria           mferlop1
# 76865412 Fernandez Lopez                Mario           mferlop
# 36638712 Gomariz Gonzaga                Amador          agomgon1
# 12987534 Gomez Gonzalez                 Alicia          agomgon
# 21783647 Gonzalez Echevarri             Antonia Maria   amgonech
# 87654321 Luna Espejo                    Emilio          elunesp
# 78988851 Mencheta Ruiz                  Javier Liborio  jlmenrui2
# 88734412 Mencheta Ruiz                  Jose Luis       jlmenrui1
# 22426553 Menendez Ruiz                  Juan            jmenrui
# 23823472 Mensaque Ruibarros             Juan Luis       jlmenrui
# 63555789 Muela Garcia                   Lidia           lmuegar
# 73535787 Navas Suarez                   Rocio           rnavsua
# 73163633 Perez Posada                   Manuel Jose     mjperpos
# 73263638 Poza Ramirez                   Isabel          ipozram
# 73276362 Rodicio Martinez               Antonio Manuel  amrodmar1
# 12326523 Rodriguez Marquez              Antonio Manuel  amrodmar
# 34551211 Sanchez Sanchez                Fermin Jose     fjsansan
# 78363677 Sanchez Santaella              Enrique Manuel  emsansan
# 21334456 Torres Chacon                  Eduardo         etorcha


# The input file has a sequence of lines of the form:
# ID:Name1:Name2:Surname1:Surname2
# or (for students who do not have a compound name):
# ID:Name::Surname1:Surname2

# As shown in the above example, each student's user name is generated by the
# following rule: initial of the first name, initial of the middle name (if
# any), the first three letters of the first surname and the first three
# letters of the second surname, all in lowercase. If under this rule there
# are several students with the same username, they have to be distinguished
# by successive numerical indexes that are added at the end.


# Note that if a line in the file does not have the above format, you should
# ignore it


# HINTS:
# - The methods "split" and "lower" of the string class may be useful.
# - When reading each line of the input file, the last character will be "\n"
#   (newline). If we have a string s, then s[:-1] is the same string but
#   without the last character.   
# - To sort the lines in alphabetical order, it may be useful the "sort"
#   method of the list class, with an appropriate "key=..." parameter.  
# - The lines in the example above has been printed using the following
#   formatting string:  "{0:>8} {1:<30} {2:<15} {3}"


# ----------------------------------------------------------------------------------

