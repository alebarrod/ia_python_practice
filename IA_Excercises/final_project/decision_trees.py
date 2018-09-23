# ==========================================================
# Artificial Intelligence. Third course.
# Grado en Ingeniería Informática 
# 2017-2018
# Universidad de Sevilla
# Final Project
# Professor: José Luis Ruiz Reina
# ===========================================================

# --------------------------------------------------------------------------
# First member of the group (or the only author): 
#
# SURNAMES: Barea Rodríguez
# NAME: Alejandro
# 
# Second member (if it is a group):
#
# SURNAMES:
# NAME:
# ----------------------------------------------------------------------------



# *****************************************************************************
# ACADEMIC INTEGRITY AND CHEATING: this project have to be carried out
# independently by each student or group. SHARING CODE IS STRICTLY
# FORBIDDEN. It as also forbidden to use any third-party code, available on
# web or on any source, without the approval of the teacher.

# Any plagiarism detected will result in a FINAL GRADE OF ZERO IN THE COURSE,
# for ALL the students involved, and it may lead to other disciplinary
# measures. Furthermore, the grades obtained until that moment will not be
# kept for future calls.  
# *****************************************************************************

# IMPORTANT: DO NOT CHANGE THE NAMES EITHER TO THIS FILE OR TO THE FUNCTIONS
# ASKED (in that case, it will not be evaluated) 


# THIS FINAL PROJECT WORTHS 20% OF THE TOTAL GRADE




# ---------------------------------------------------------------------------
# SECTION 0: Data sets
# ---------------------------------------------------------------------------

# In this section, you do not have to do anything, buth it is important to
# read it in order to understand the structure of the data sets provided. 

#
# Files play_tennis.py, contac_lenses.py, votes.py and credit.py (that can be
# downloaded from the web page of this final project) contain the data sets
# we are going to use in this final project, and our implementations will be
# tested on them. 

# Each of these files contain the corresponding definition for the following
# variables: 


# * attributes: is a list of pairs (Attribute,Values) for each attribute (or
#   feature) of the data set. Attribute is the name of the attribute and
#   Values is the list of its possible values. 

# * class_name: name of the classification attribute.

# * classes: possible values (or classes) of the classification attribute. 

# * train: training set, a list of examples. Each example is a list of values,
#   where a value in a given position is the value of the attribute of the
#   same position in the attributes list described above. The value in the
#   last position is the class of the example. 

# In addition, votes.py and credit.py contain the following additional
# variables: 

# * valid: validation set, is a list of examples with the same format than the
#   trainig set. This set of examples will be used to adjust or generalize the
#   model learned in the trainig phase. In our case, it will be used to prune
#   the learned decision tree. 


# * test: test set, a list of examples with the same format than the training
#   set. These examples will be used to evaluate the final accuracy of a
#   learned classifier. 

# Let us import these four files:  

import play_tennis
import contact_lenses
import votes
import credit
import titanic
import random
from math import log
from collections import defaultdict



# ---------------------------------------------------------------------------
# SECTION 1: Learning decision trees
# ---------------------------------------------------------------------------

# Decision tree representation:
# =============================

# NOTE: In the following description we could be using the same term
# "attribute" to refer to two different things: variables attributes of an
# object of a python class, and attributes of data sets. We hope that it will
# be clear from the context to what we are referring in each case, but to
# avoid confussion, we also use the term "field" for variable attributes
# of an python class. 


# We will represent decision trees using the following data structure, in
# a recursive way 
            

class NodeDT(object):
    
    def  __init__(self,attribute=-1,distr=None,branches=None,clas=None):
        self.distr=distr 
        self.attribute=attribute 
        self.branches=branches 
        self.clas=clas

    
    


# An object of this class NodeDT will represent a decision tree node, by means
# of its four fields (distr, atrribute, branches, class), as we describe in
# the following. We will have two types of nodes, both represented by objects
# of the class NodeDT: LEAF nodes, those with a class value, and INNER nodes,
# corresponding to a given attribute and having as many successors subtrees as
# posible values of the attribute. Depending on the type of the node, some of
# the attributes of the object will have None value. That is:
        
a = NodeDT("contact_lenses.py");
# * In a leaf node, the "clas" field contains the classification value
#   returned by the node. The "branches" and "attribute" fields have None
#   value.  

# * In a inner node, the "clas" field is None, the "attribute" field is an
#   index to the corresponding attribute in the list of attributes of the data
#   set, and "branches" is a dictionary representing its successors
#   subtrees. In particular, the keys of that dictionary are the different
#   values of the attribute (the label of the branch) and the value assigned
#   to that key is an object of the class NodeDT recusively representing the
#   subtree corresponding to that value.    


# IMPORTANT NOTE: In the "attribute" field we will not store the name of the
# attribute, but an INDEX to the position of that attribute in list of
# attributes of the data set.


# In both types of nodes, the "distr" field will store the distribution,
# according to the different class values, of the examples in the training set
# corresponding to that node. 


# With an example, it will better understood.  


# EXAMPLE
# -------

# Let us describe how to represent the "Play Tennis" decision tree shown in
# slide 8 of unit 3.  

# Let us assume the variable pt_tree contains such tree (in this case, the
# tree has been built using the learning algorithm asked later). 

# >>> pt_tree=learn_tree(play_tennis.train,play_tennis.attributes)


# That tree is an object of the class NodeDT, or more precisely the root node
# of the tree:  


# >>> pt_tree
# <__main__.NodeDT at 0x7f1b8d74b550>

# It is an inner node (the root in this case), whose attribute is
# "Outlook". In the attributes variable of play_tennis.py, "Outlook" is the
# first attribute, so the corresponding index is 0, and that is what we
# store in the "attribute" field:


# >>> pt_tree.attribute
# 0

# In the "distr" field, we store the class distribution of the examples
# corresponding to that node (in this case all the examples, since its the
# root node):

# >>> pt_tree.distr
# defaultdict(int, {'no': 5, 'yes': 9})

# Note that the distribution is stored using "defaultdict", a datatype similar
# to "dict", but with a default value that it is assumed to correspond to any
# "key" not present in the dictionary. In this particular case, initializing
# with "defaultdict(int)", we obtain a default dictionary in which every key
# not explicitly in it, will have associated default value of 0. For more
# details on default dictionaries, see the python manual reference, module
# "collections". 

# In the "branches" field, we store a dictionary, with a key for every value
# of the "Outlook" attribute. The value associated to each key is itself a
# NodeDT object, recursively representing  the corresponding subtree. 

# >>> pt_tree.branches

# {'Sunny': <__main__.NodeDT object at 0x7fa508e0e198>, 
#  'Overcast': <__main__.NodeDT object at 0x7fa508e0ecf8>, 
#  'Rainy': <__main__.NodeDT object at 0x7fa508e1eac8>}

 

# For example, the subtree of the branch "Outlook=Sunny", starts with an inner
# node corresponding to the index attribute 2 ("Humidity"):

# >>> pt_tree.branches["Sunny"].attribute
# 2

# With "Outlook=Sunny", we have 3 negative and 2 positive examples: 

# >>> pt_tree.branches["Sunny"].distr
# defaultdict(int, {'no': 3, 'yes': 2})

# And the branches are:

# >>> pt_tree.branches["Sunny"].branches
# {'High': <__main__.NodeDT at 0x7f8c84687710>,
#  'Normal': <__main__.NodeDT at 0x7f8c846877f0>}

# The node corresponding to "Outlook=Sunny" and "Humidity=Normal" is a leaf of
# the tree, classifying as "yes": 

# >>> pt_tree.branches["Sunny"].branches["Normal"].clas
# 'yes'

# And with "Outlook=Sunny" and "Humidity=Normal", we have 2 positive and 0
# negative examples: 

# >>> pt_tree.branches["Sunny"].branches["Normal"].distr
# defaultdict(int, {'yes': 2})

# The node corresponding to "Outlook Sunny" and "Humidity=High" is also a leaf
# of the tree, classifying as negative, and whose distribution is 3 negative
# and 0 positive examples:

# >>> pt_tree.branches["Sunny"].branches["High"].clas
# 'no'
# >>> pt_tree.branches["Sunny"].branches["High"].distr
# defaultdict(int, {'no': 3})

# The following are the rest of the nodes: 

# >>> pt_tree.branches["Overcast"].clas
# 'yes'
# >>> pt_tree.branches["Overcast"].distr
# defaultdict(int, {'yes': 4})


# >>> pt_tree.branches["Rainy"].attribute
# 3
# >>> pt_tree.branches["Rainy"].branches
#{'Strong': <__main__.NodeDT at 0x7f8c84687630>,
# 'Weak': <__main__.NodeDT at 0x7f8c84687668>}
# >>> pt_tree.branches["Rainy"].distr
# defaultdict(int, {'no': 2, 'yes': 3})

# >>> pt_tree.branches["Rainy"].branches["Strong"].clas
# 'no'
# >>> pt_tree.branches["Rainy"].branches["Strong"].distr
# defaultdict(int, {'no': 2})

# >>> pt_tree.branches["Rainy"].branches["Weak"].clas
# 'yes'
# >>> pt_tree.branches["Rainy"].branches["Weak"].distr
# defaultdict(int, {'yes': 3})


# FUNCTIONS ASKED
# ===============

# Using the above data structure, implement the following four functions:


# 1. A function "learn_tree(examples,attributes)", such that receiving a set
# of examples and a list of attributes (with names and values, as in in data
# set files) apply the id3 algorithm described in class, to obtain a decision
# tree. 

#measure the impurity, it receives a list and return the impurity number (from 1.0 to 0.0)
def entropy_func(values):
    acum = 0
    res = 0
    excep = 0
    
    for value in values:
        acum = acum + value
        if value != 0:
            excep = excep + 1
    
    if excep <= 1:
        res = 0
    else:
        for value in values:
            if value != 0:
                res = res -value/acum * log(value/acum, 2)
    
    return res

#inicializes the recursive function respecting the requirements
def learn_tree(train, attributes, impurity_func=entropy_func,
               max_freq_split=1.0,
               min_prop_examples=0):
    
    return learn_tree_main(train, attributes, attributes.copy(), impurity_func, max_freq_split, min_prop_examples, len(train))
    

def learn_tree_main(train,attributes,resting_attributes,
                    impurity_func,
                    max_freq_split,
                    min_prop_examples,
                    size):
    clas_dict = {}
    node_clas = None
    branches = None
    attribute = None
    attributes_left = False
    
    #Create a dict with every possible class
    for example in train:
        if example[-1] not in clas_dict:
            clas_dict[example[-1]] = 1;
        else:
            clas_dict[example[-1]] = clas_dict[example[-1]]+1
    
    #Check if there is any attribute left to continue
    for attribu in resting_attributes:
        if attribu[1] != []:
            attributes_left = True
            break
    
    #get the entropy of the train set
    clas_ent = impurity_func(clas_dict.values())
    
    #prepare dist
    distr = defaultdict(int,clas_dict)
    
    #get the proportion of the most abundant
    max_prop = get_prop(distr)
    
    #get the number of examples tested in the actual node (get the proportion)
    min_prop = len(train)/size
    
    if len(clas_dict) == 1:
        #If all examples correctly classified
        for key in clas_dict.keys():
            node_clas = key
            branches = None
            attribute = None
    elif attributes_left == False or min_prop_examples >= min_prop or max_freq_split <= max_prop:
        #If no attributes left 
        
        
        max_clas = None
        max_number = 0
        #Select the most common attribute to add it as a final node
        for clas in clas_dict:
            if clas_dict[clas] > max_number:
                max_clas = clas
                max_number = clas_dict[clas]
        
        node_clas = max_clas
        
    else:
        #Classify examples by attribute and class
        
        #prepare train set to process entropy
        preentropy = train_classifier(train,resting_attributes)
        #get the entropy of each element
        entropy = prepare_entropy(preentropy, impurity_func)
        #get the chosen attribute and its value
        attrib = prepare_gain(entropy, attributes, clas_ent)
        
        
        #prepare list of resting attributes for next iteration
        aux = []
        for tuples in resting_attributes:
            if tuples[0] == attrib:
                aux.append((tuples[0],[]))
            else:
                aux.append((tuples[0],tuples[1]))
        
        attribute = aux.index((attrib,[]))  #attribute position
        
        #divide train list by chosen attribute options
        branch_dict = {}
        for branch in attributes[attribute][1]:
            branch_dict[branch] = []
            for row in train:
                if row[attribute] == branch:
                    branch_dict[branch].append(row)
        
        #finaly change resting the chosen attribute
        for attribut in resting_attributes:
            if attribut[0] == attrib:
                resting_attributes[resting_attributes.index(attribut)] = (attrib,[])
        
        #call recursively this function with each branch sublists (from train list)
        branches = {}    
        for branch in branch_dict:
            if branch_dict[branch] != []:        
                branches[branch] = learn_tree_main(branch_dict[branch], attributes, resting_attributes.copy(), impurity_func, max_freq_split, min_prop_examples, size)
        
        
        
    
    #create and return node
    return NodeDT(attribute,distr,branches,node_clas)


#receive the train list and attribute list and return a train list as a dict -> keys -> attributes, values -> list with a tuple for each possible value of each attribute. This tuple has the name of the value and a dict with key->class and value-> amount of examples classified 
#return value from play_tennis(1st iteration):
#{'Outlook': [('Sunny', {'no': 3, 'yes': 2}), ('Overcast', {'yes': 4}), ('Rainy', {'yes': 3, 'no': 2})],
# 'Temperature': [('High', {'no': 2, 'yes': 2}), ('Low', {'yes': 3, 'no': 1}), ('Mild', {'yes': 4, 'no': 2})],
# 'Humidity': [('High', {'no': 4, 'yes': 3}), ('Normal', {'yes': 6, 'no': 1})],
# 'Wind': [('Weak', {'no': 2, 'yes': 6}), ('Strong', {'no': 3, 'yes': 3})]}
def train_classifier(train,attributes):
    save = {}

    for index in range(0,len(attributes)):
        save[attributes[index][0]] = []
        for attrib in attributes[index][1]:
            aux = {}
            for row in train:
                
                if row[index] == attrib:
                    if row[-1] in aux:
                        aux[row[-1]] = aux[row[-1]]+1
                    else:
                        aux[row[-1]] = 1
                    
            save[attributes[index][0]].append((attrib,aux))
    return save


#receive a classified_dict from train_classifier and the impurity_func and compute the entropy for each value from available attributes returning the same structure but substitutes the dict with key->class and value->quantity by a tuple with the result of the impurity func and the amount of examples afected by this impurity_func result
#return value from play_tennis(1st iteration):
#{'Outlook': {'Sunny': (0.9709505944546686, 5), 'Overcast': (0, 4), 'Rainy': (0.9709505944546686, 5)},
#'Temperature': {'High': (1.0, 4), 'Low': (0.8112781244591328, 4), 'Mild': (0.9182958340544896, 6)},
#'Humidity': {'High': (0.9852281360342516, 7), 'Normal': (0.5916727785823275, 7)},
#'Wind': {'Weak': (0.8112781244591328, 8), 'Strong': (1.0, 6)}}
def prepare_entropy(entropy_set, impurity_func):
    ent_save = {}
    for key in entropy_set.keys():
        ent_aux = []
        for choice in entropy_set[key]:
            aux = {}
            for pos in choice[1]:
                if choice[0] not in aux:
                    aux[choice[0]] = []
                aux[choice[0]].append(choice[1][pos])
            
            ent_aux.append(aux)
        
        aux2 = {}
        for atrib in ent_aux:
            for key2 in atrib:
                aux2[key2] = (impurity_func(atrib[key2]),sum_array(atrib[key2]))
        
        ent_save[key] = aux2
    return ent_save

#simple func -> return the sum of an array acomulated
def sum_array(array):
    acum = 0
    for element in array:
        acum = acum + element
    return acum
    
#receives the result of prepare_entropy, attribute list and the train clas impurity and return the chosen attribute
#return value from play_tennis(1st iteration):
#'Outlook'
def prepare_gain(ent_dict, attributes, clas_ent):
    gain_values = []   
    for row in ent_dict:
        if ent_dict[row] != {}:
            aux = []
            for value in ent_dict[row]:
                aux.append(ent_dict[row][value])
            gain_values.append(gain_func(aux, row, clas_ent))
        
    acum = -1
    attribute = ''
    for value in gain_values:
        if value[0] > acum:
            acum = value[0]
            attribute = value[1]
    return attribute
    
#receive a list with tuples with impurity and the quantity of examples affected by that impurity
#return value from play_tennis(1st iteration):
#0.2467498197744391,'Outlook'
def gain_func(value_combo, attribute, clas_ent):
    total = 0
    
    for tuples in value_combo:
        total = total + tuples[1]
        
    res = clas_ent
    
    for tuples in value_combo:
        res = res - tuples[0] * (tuples[1] / total)

    return res,attribute


#receives the distr from a tree and a function min or max
#returns the proportion of the most abundant (max) or the least abundandt (min)
def get_prop(distr):
    prop = []
    acum = 0
    for clas in distr:
        prop.append(distr[clas])
        acum += distr[clas]
    
    return max(prop)/acum

# This function has additional input parameters, explained below in detail. 

# 2. A function "print_DT(tree,attributes,class_name)" such that receiving a
# decision tree, the list of attributes of the problem (as in the data set
# files) and the name of the class attribute, prints the tree as shown in the
# examples below.   

def print_DT(tree,attributes,class_name):
    
    #first it is prepared the root node print 
    root_str = "Root node ("
    not_first = False
    
    for one in tree.distr:
        if not_first:
            root_str += " "
        else:
            not_first = True
        
        root_str += one + ": "+str(tree.distr[one])
        
    
    root_str +=")"
    print(root_str)
    #the next action is call the main method to print the tree recursively
    sub_print_DT(tree, attributes, class_name, 1)
            

def sub_print_DT(tree, attributes, class_name, tabs):
    #buffer to prepare the string to print
    pre_print = ""
    
    
    #its added a tab for each iteration to easily read the tree printed
    for i in range(0,tabs):
        pre_print += "\t"
    
    #its checked if it is a leaf node and print it depending on that
    if tree.clas != None:
        pre_print += class_name + ": " + tree.clas + "."
        print(pre_print)
        
    elif attributes != None:
        #if there is attributes it is an inner node
        next_attribute = attributes[tree.attribute]
        
        #for each value for the attribute
        for option in next_attribute[1]:
            print_buf = pre_print
            print_buf += next_attribute[0] + " = " + option + ". ("
            
            cont = False #the first blank space is avoid
            
            if option in tree.branches.keys():
                #for each branch of the current node (only if it exists):
                for clas in tree.branches[option].distr:
                    
                    if not cont:
                        cont = True
                        
                    else:
                        print_buf += " "
                    #prepare in the buffer distribution of the node
                    print_buf += clas + ": " + str(tree.branches[option].distr[clas])
                print_buf += ")"
                #print the buffer and call the recursive function to print the tree adding 1 to the tabs
                #and a subtree for each option (for each call to the recursive function)
                print(print_buf)
                sub_print_DT(tree.branches[option], attributes, class_name, tabs+1)
    
# Root node (no: 5  yes: 9)
#  Outlook = Sunny. (no: 3  yes: 2)
#       Humidity = High. (no: 3)
#            Play Tennis: no.
#       Humidity = Normal. (yes: 2)
#            Play Tennis: yes.
#  Outlook = Overcast. (yes: 4)
#       Play Tennis: yes.
#  Outlook = Rainy. (yes: 3  no: 2)
#       Wind = Weak. (yes: 3)
#            Play Tennis: yes.
#       Wind = Strong. (no: 2)
#            Play Tennis: no.

# 3. A function "classify_DT(example,tree)" such that receiving an example
# (without its class) and a decision tree, returns the class that the tree
# assigns to the example.

def classify_DT(example, tree):
    res = None
    if tree.clas == None:
        #If it is not a leaf node
        for branch in tree.branches:
            if branch == example[tree.attribute]:
                #If the attribute  value is the same as the branch one:
                
                #classify the using the subtree recursively (until reaching a leaf node)
                res = classify_DT(example,tree.branches[branch])
    else:
        #Else (it is a leaf node)
        res = tree.clas
    return res

# 4. A function "accuracy_DT(tree,examples)", such that receiving and list of
# examples (with their class) and a decision tree, returns the proportion of
# examples correctly classified by the tree. 

def accuracy_DT(tree,examples):
    general_cont = 0
    correct_cont = 0
    
    #acomulate the number of examples compared (it does not increment the complexity)
    #and comparing the number of correctly classified examples
    for example in examples:
        predict = classify_DT(example, tree)
        general_cont += 1
        if predict == example[-1]:
            #If the classificationion is the same as the real class the cont is incremented
            correct_cont += 1
            
    #get the proportion of correctly classified examples (number between 1.0 and 0.0)
    return correct_cont / general_cont            

# -------------

# Let us explain in more detail a number of additional input parameters of  the 
# function learn_tree. The complete specification of the function is:

# learn_tree(training_set,
#            attributes,
#            impurity_func=entropy,
#            max_freq_split=1.0,
#            min_prop_examples=0)

# where:

# - training_set is a list of examples, as provided in the data files. 

# - attributes is list of the attributes of the data, and its possible values,
#   as provided in the data files.

# - impurity_func: this is a parameter indicating the function that we will
#   use to mesure the "impurity" of a distribution of examples in
#   classes. This generalizes the criteria used in the slides. 
#   The impurity function may be either entropy or gini (the default value is
#   entropy):  

#     * The entropy of a distribution is defined as in the slides of unit 3,
#       but generalized to possibly more than two classes: if we have n 
#       different classes, the entropy of a distribution [x1,...,xn] is
#                     sum_{i=1,n} -(xi/N)log(xi/N), 
#       where N is x1+...+xn and log is base 2 logarithm.
   
#     * Analogously, the gini impurity of a distribution is defined in the
#       following way: 
#                      1- sum_{i=1,n} (xi/N)**2

def gini(array):
    acum = 0
    
    for element in array:
        acum += element
    
    res = 0
    if acum != 0:    
        for element in array:
            res += (element/acum)**2
        
    return abs(1-res)

#   Both entropy and gini measure the lack of homogeneity of a distribution
#   and can be used as a criteria to decide which is the best attribute to
#   split at a given node of a decision tree, in the following way. If we have
#   a set of examples E at a Node, and a candidate attribute A with values
#   v1,...,vm, then we define the Gain of A in E as:

#      Gain(A,E)=impurity(E)-sum_{j=1,m}(N_vj/N)*impurity(E_vj)

#   where E_vj is the subset of examples in E with A=vj, N_vj is the size  
#   of E_vj, N is the size of E, and impurity may be either entropy or gini. 

#   When learning the tree, we will select the attribute with the greatest
#   gain (and we will use entropy or gini as impurity, depending on the
#   value of the input argument impurity_func).

# - max_freq_split is a number between 0 and 1.0 (default 1.0). If in a given
#   node the proportion of the most frequent class is greater or equal than
#   max_freq_split, then we make that node a leaf, classificationing that majority
#   class.

# - min_prop_examples is a number between 0 and 1.0 (default 0). If the
#   proportion of examples in a node is less or equal than min_prop_examples,
#   then we make that node a leaf, classificationing the most frequent class.

# The last two arguments (max_freq_split and min_prop_examples) provide a way
# of "early stopping" when learning the tree, to avoid overfitting by means of
# pre-pruning. In the next section, we will also implement post-pruning, an
# alternative way to avoid overfitting.  

# Some examples:
# --------------

# Play tennis:

# >>> pt_tree=learn_tree(play_tennis.train,play_tennis.attributes)

# >>> print_DT(pt_tree,play_tennis.attributes,play_tennis.class_name)

# Root node (no: 5  yes: 9)
#  Outlook = Sunny. (no: 3  yes: 2)
#       Humidity = High. (no: 3)
#            Play Tennis: no.
#       Humidity = Normal. (yes: 2)
#            Play Tennis: yes.
#  Outlook = Overcast. (yes: 4)
#       Play Tennis: yes.
#  Outlook = Rainy. (yes: 3  no: 2)
#       Wind = Weak. (yes: 3)
#            Play Tennis: yes.
#       Wind = Strong. (no: 2)
#            Play Tennis: no.

# >>> classify_DT(["Sunny","Mild","High","Strong"],pt_tree)
# 'no'

# >>> accuracy_DT(pt_tree,play_tennis.train)
# 1.0

# ------------------

# Contact lenses:

# >>> cl_tree=learn_tree(contact_lenses.train,contact_lenses.attributes)
# >>> print_DT(cl_tree,contact_lenses.attributes,contact_lenses.class_name)                

#Root node (None: 15  Soft: 5  Hard: 4)
# Tear rate = Reduced. (None: 12)
#      Lens: None.
# Tear rate = Normal. (Soft: 5  Hard: 4  None: 3)
#      Astigmatic = +. (Hard: 4  None: 2)
#           Prescription = Myope. (Hard: 3)
#                Lens: Hard.
#           Prescription = Hypermetrope. (Hard: 1  None: 2)
#                Age = Young. (Hard: 1)
#                     Lens: Hard.
#                Age = Pre-presbyopic. (None: 1)
#                     Lens: None.
#                Age = Presbyopic. (None: 1)
#                     Lens: None.
#      Astigmatic = -. (Soft: 5  None: 1)
#           Age = Young. (Soft: 2)
#                Lens: Soft.
#           Age = Pre-presbyopic. (Soft: 2)
#                Lens: Soft.
#           Age = Presbyopic. (None: 1  Soft: 1)
#                Prescription = Myope. (None: 1)
#                     Lens: None.
#                Prescription = Hypermetrope. (Soft: 1)
#                     Lens: Soft.

# >>> classify_DT(["Pre-presbyopic","Hypermetrope","-","Normal"],cl_tree)
# 'Soft'

# >>> accuracy_DT(cl_tree,contact_lenses.train)
# 1.0

# >>> cl_tree_2=learn_tree(contact_lenses.train,contact_lenses.attributes,
#                          impurity_func=gini,
#                          max_freq_split=0.75,
#                          min_prop_examples=0.15)

# >>> print_DT(cl_tree_2,contact_lenses.attributes,contact_lenses.class_name)

# Root node (None: 15  Soft: 5  Hard: 4)
#  Tear rate = Reduced. (None: 12)
#       Lens: None.
#  Tear rate = Normal. (Soft: 5  Hard: 4  None: 3)
#       Astigmatic = +. (Hard: 4  None: 2)
#            Prescription = Myope. (Hard: 3)
#                 Lens: Hard.
#            Prescription = Hypermetrope. (Hard: 1  None: 2)
#                 Lens: None.
#       Astigmatic = -. (Soft: 5  None: 1)
#            Lens: Soft.


# >>> classify_DT(["Pre-presbyopic","Hypermetrope","-","Normal"],cl_tree_2)
# 'Soft'

# >>> accuracy_DT(cl_tree_2,contact_lenses.train)
# 0.9166666666666666

# ----------------

# Congressional voting:

# >>> votes_tree=learn_tree(votes.train,votes.attributes)

# >>> print_DT(votes_tree,votes.attributes,votes.class_name)
# Root node (republican: 107  democrat: 172)
#  vote4 = y. (republican: 103  democrat: 6)
#       vote3 = y. (republican: 10  democrat: 4)
#            vote7 = y. (republican: 9)
#                 Party: republican.
#            vote7 = n. (democrat: 4  republican: 1)
#                 vote2 = y. (democrat: 3)
#                      Party: democrat.
#                 vote2 = n. (democrat: 1)
#                      Party: democrat.
#                 vote2 = ?. (republican: 1)
#                      Party: republican.
#            vote7 = ?. (No examples)
#                 Party: republican.
#       vote3 = n. (republican: 92  democrat: 1)
# ...
# ... 
# ... (a big tree, we do not show it complete here)
# ...


# >>> accuracy_DT(votes_tree,votes.train)
# 1.0
# >>> accuracy_DT(votes_tree,votes.valid)
# 0.9420289855072463
# >>> accuracy_DT(votes_tree,votes.test)
# 0.9195402298850575


# >>> votes_tree_2=learn_tree(votes.train,votes.attributes,
#                             max_freq_split=0.95,
#                             impurity_func=gini,
#                             min_prop_examples=0.05)
# >>> print_DT(votes_tree_2,votes.attributes,votes.class_name)
# Root node (republican: 107  democrat: 172)
#  vote4 = y. (republican: 103  democrat: 6)
#       vote3 = y. (republican: 10  democrat: 4)
#            vote7 = y. (republican: 9)
#                 Party: republican.
#            vote7 = n. (democrat: 4  republican: 1)
#                 Party: democrat.
#            vote7 = ?. (No examples)
#                 Party: republican.
#       vote3 = n. (republican: 92  democrat: 1)
#            Party: republican.
#       vote3 = ?. (republican: 1  democrat: 1)
#            Party: republican.
#  vote4 = n. (democrat: 163  republican: 2)
#       Party: democrat.
#  vote4 = ?. (democrat: 3  republican: 2)
#       Party: democrat.


# >>> accuracy_DT(votes_tree_2,votes.train)
# 0.974910394265233
# >>> accuracy_DT(votes_tree_2,votes.valid)
# 0.9565217391304348
# >>> accuracy_DT(votes_tree_2,votes.test)
# 0.9195402298850575


# ------------

# Bank credit:

# >>> ct_tree=learn_tree(credit.train,credit.attributes)

# >>> print_DT(ct_tree,credit.attributes,credit.class_name)

#Root node (study: 116  not grant: 107  grant: 102)
# Income = low. (not grant: 73  study: 19  grant: 11)
#      Employment = official. (not grant: 9  study: 8  grant: 9)
#           Real estate = none. (not grant: 9)
#                Loan: not grant.
#           Real estate = one. (study: 6)
#                Loan: study.
#           Real estate = more. (study: 2  grant: 9)
#                Marital status = single. (grant: 4)
#                     Loan: grant.
#                Marital status = married. (grant: 1)
#                     Loan: grant.
# ....
# ....
# .... (very big tree, not shown complete).
    

# >>> accuracy_DT(ct_tree,credit.train)
# 1.0
# >>> accuracy_DT(ct_tree,credit.valid)
# 0.9197530864197531
# >>> accuracy_DT(ct_tree,credit.test)
# 0.8650306748466258

# >>> ct_tree_2=learn_tree(credit.train,credit.attributes,
#                          max_freq_split=0.75,
#                          min_prop_examples=0.1)

# >>> print_DT(ct_tree_2,credit.attributes,credit.class_name)
# Root node (study: 116  not grant: 107  grant: 102)
#  Income = low. (not grant: 73  study: 19  grant: 11)
#       Employment = official. (not grant: 9  study: 8  grant: 9)
#            Loan: not grant.
#       Employment = employed. (not grant: 17  study: 7)
#            Loan: not grant.
#       Employment = unemployed. (study: 2  grant: 1  not grant: 24)
#            Loan: not grant.
#       Employment = retired. (study: 2  grant: 1  not grant: 23)
#            Loan: not grant.
#  Income = medium. (grant: 37  not grant: 34  study: 36)
#       Real estate = none. (not grant: 23  grant: 1  study: 14)
#            Employment = official. (study: 6)
#                 Loan: study.
#            Employment = employed. (grant: 1  not grant: 1  study: 6)
#                 Loan: study.
#            Employment = unemployed. (study: 2  not grant: 13)
#                 Loan: not grant.
#            Employment = retired. (not grant: 9)
#                 Loan: not grant.
#       Real estate = one. (not grant: 11  study: 22  grant: 1)
#            Products = none. (study: 1  grant: 1  not grant: 7)
#                 Loan: not grant.
#            Products = one. (study: 14)
#                 Loan: study.
#            Products = more. (not grant: 4  study: 7)
#                 Loan: study.
#       Real estate = more. (grant: 35)
#            Loan: grant.
#  Income = high. (study: 61  grant: 54)
#       Employment = official. (grant: 26)
#            Loan: grant.
#       Employment = employed. (study: 3  grant: 25)
#            Loan: grant.
#       Employment = unemployed. (grant: 3  study: 29)
#            Loan: study.
#       Employment = retired. (study: 29)
#            Loan: study.


#>>> accuracy_DT(ct_tree_2,credit.train)
#0.8584615384615385
#
#>>> accuracy_DT(ct_tree_2,credit.valid)
#0.9012345679012346
#
#>>> accuracy_DT(ct_tree_2,credit.test)
#0.8834355828220859




# ---------------------------------------------------------------------------
# SECTION 2: Reduced error pruning
# ---------------------------------------------------------------------------

# Overfitting is a phenomenon typically ocurring in supervised learning, when
# the learned model is so fitted to a particular training data, that it does
# not generalize well to predict on data that were not used for training.

# A way to avoid overfitting when learning decision trees is to prune the
# learned tree, trying to improve the accuracy on a set of examples different
# from the one used for training. This can be done in the training phase,
# applying some early stopping criteria (as shown in the previous section),
# but the most common way to do it is by post-pruning the learned tree.  

# For that purpose, in the cases when we have enough data, we are going to
# split them in three different parts: training, validation and test sets. We
# will learn the tree using the training data, the validation examples will be
# used to prune the tree and finally we will measure its accuracy on the test
# set. Note that the examples on votes.py and credit.py are already splitted
# in these three parts.

# One of the basic pruning techniques is implemented by the "reduced error
# pruning" algorithm described in unit 3, slide 32. In this section we ask you
# to implement that algorithm in python. For that, the following auxiliary
# functions may be useful:

# * The function "inner_nodes_DT" receives a decision tree a returns a list
# with "paths" to all the inner nodes of the tree.

def inner_nodes_DT_rec(Tree_dt,current_path,acum_nodes):
    if Tree_dt.clas is not None:
        return acum_nodes
    else:
        acum_nodes.append(current_path)
        for val in Tree_dt.branches:
            acum_nodes=inner_nodes_DT_rec(Tree_dt.branches[val],current_path+[val],acum_nodes)
        return acum_nodes

def inner_nodes_DT(Tree_DT):
    return inner_nodes_DT_rec(Tree_DT,[],[])


# Examples:


# >>> inner_nodes_DT(pt_tree)
# [[], ['Sunny'], ['Rainy']]
# >>> inner_nodes_DT(cl_tree)
# [[], ['Normal'], ['Normal', '+'], ['Normal', '+', 'Hypermetrope'], 
#  ['Normal', '-'], ['Normal', '-', 'Presbyopic']]

# Note that every path to an inner node can be characterized by the labels
# (values of attributes) of the branches leading to that node. The path
# corresponding to the root node is the empty list.  


# * The function "prune_node_DT(tree,node)" receives a decision tree and a
# path to an inner node (in the form returned by the previous function), and
# returns a COPY of the tree in which that node has been pruned and replaced by
# a leaf with the majority class in that node (note that you must define the
# function "most_frequent_class")

import copy

def prune_node_DT(tree,node):
    if node==[]:
        return NodeDT(clas=most_frequent_class(tree.distr),distr=copy.copy(tree.distr))
    else:
        val_node=node[0]
        pruned_tree=NodeDT(attribute=tree.attribute,distr=copy.copy(tree.distr))
        dict_subtrees={}
        for val in tree.branches:
            if val_node==val:
                dict_subtrees[val]=prune_node_DT(tree.branches[val],node[1:])
            else:
                dict_subtrees[val]=copy.deepcopy(tree.branches[val])
        pruned_tree.branches=dict_subtrees
        
        return pruned_tree

def most_frequent_class(distr):
    clas = ""
    class_cont = 0
    for choose in distr:
        if distr[choose] > class_cont:
            clas = choose
            class_cont = distr[choose]
    
    return clas

# Example:
# >>> print_DT(prune_node_DT(cl_tree,['Normal','+']),
#              contact_lenses.attributes,
#              contact_lenses.class_name)

# Root node (None: 15  Soft: 5  Hard: 4)
#  Tear rate = Reduced. (None: 12)
#       Lens: None.
#  Tear rate = Normal. (Soft: 5  Hard: 4  None: 3)
#       Astigmatic = +. (Hard: 4  None: 2)
#            Lens: Hard.
#       Astigmatic = -. (Soft: 5  None: 1)
#            Age = Young. (Soft: 2)
#                 Lens: Soft.
#            Age = Pre-presbyopic. (Soft: 2)
#                 Lens: Soft.
#            Age = Presbyopic. (None: 1  Soft: 1)
#                 Prescription = Myope. (None: 1)
#                      Lens: None.
#                 Prescription = Hypermetrope. (Soft: 1)
#                      Lens: Soft.


# FUNCTION ASKED
# ==============

# * A function "prune_tree(tree,examples)" such that receiving as input a
# decision tree and a set of examples, apply reduced error pruning as
# described in slide 32, unit 3. 

    

def prune_tree(tree, examples):
    #get the actual accuracy of the main tree
    accuracy = accuracy_DT(tree, examples)
    actual_tree = copy_tree_DT(tree)
    candidate = copy_tree_DT(tree)
    retry = True
    while retry:
        #while a better tree is chosen this will continue iterating, if not the loop will stop
        retry = False
        #inner_nodes_DT return a list with all paths to reach each inner node
        general_list = inner_nodes_DT(actual_tree)
        
        #A new tree for each path is created prunning until the end of that path
        #and if the accuracy of this new tree is better than the candidate it is substituted
        for route in general_list:
            
            #prune_node_DT receives one path from inner_nodes_DT and return a new tree prunning
            #the node given by the path
            prunned = prune_node_DT(actual_tree, route)
            new_accuracy = accuracy_DT(prunned, examples)
            #if the new tree has a better accuracy than the reference this becomes the reference tree
            if new_accuracy >= accuracy:
                 accuracy = new_accuracy
                 candidate = copy_tree_DT(prunned)
                 #If no changes --> stop iterating
                 retry = True
        
        #now the reference tree is the best candidate of the iteration
        actual_tree = copy_tree_DT(candidate)
        
    return candidate

gen = []    

#return a deepcopy of a tree structure 
def copy_tree_DT(tree):
    tree_dict = {}
    if tree.clas != None:
        return NodeDT(tree.attribute,tree.distr,tree.branches,tree.clas)
    else:
        for branch in tree.branches:
            tree_dict[branch] = copy_tree_DT(tree.branches[branch])
    return NodeDT(tree.attribute, tree.distr, tree_dict, tree.clas)


# Examples:

# >>> votes_pruned=prune_tree(votes_tree,votes.valid)
# >>> print_DT(votes_pruned,votes.attributes,votes.class_name)
# Root node (republican: 107  democrat: 172)
#  vote4 = y. (republican: 103  democrat: 6)
#       Party: republican.
#  vote4 = n. (democrat: 163  republican: 2)
#       Party: democrat.
#  vote4 = ?. (democrat: 3  republican: 2)
#       Party: democrat.



#>>> ct_pruned=prune_tree(ct_tree,credit.valid)

#>>> print_DT(ct_pruned,credit.attributes,credit.class_name)

#Root node (study: 116  not grant: 107  grant: 102)
# Income = low. (not grant: 73  study: 19  grant: 11)
#      Employment = official. (not grant: 9  study: 8  grant: 9)
#           Real estate = none. (not grant: 9)
#                Loan: not grant.
#           Real estate = one. (study: 6)
#                Loan: study.
#           Real estate = more. (study: 2  grant: 9)
#                Loan: grant.
#      Employment = employed. (not grant: 17  study: 7)
#           Products = none. (not grant: 8)
#                Loan: not grant.
#           Products = one. (not grant: 9)
#                Loan: not grant.
#           Products = more. (study: 7)
#                Loan: study.
#      Employment = unemployed. (study: 2  grant: 1  not grant: 24)
#           Loan: not grant.
#      Employment = retired. (study: 2  grant: 1  not grant: 23)
#           Loan: not grant.
# Income = medium. (grant: 37  not grant: 34  study: 36)
#      Real estate = none. (not grant: 23  grant: 1  study: 14)
#           Employment = official. (study: 6)
#                Loan: study.
#           Employment = employed. (grant: 1  not grant: 1  study: 6)
#                Loan: study.
#           Employment = unemployed. (study: 2  not grant: 13)
#                Loan: not grant.
#           Employment = retired. (not grant: 9)
#                Loan: not grant.
#      Real estate = one. (not grant: 11  study: 22  grant: 1)
#           Products = none. (study: 1  grant: 1  not grant: 7)
#                Loan: not grant.
#           Products = one. (study: 14)
#                Loan: study.
#           Products = more. (not grant: 4  study: 7)
#                Loan: study.
#      Real estate = more. (grant: 35)
#           Loan: grant.
# Income = high. (study: 61  grant: 54)
#      Employment = official. (grant: 26)
#           Loan: grant.
#      Employment = employed. (study: 3  grant: 25)
#           Loan: grant.
#      Employment = unemployed. (grant: 3  study: 29)
#           Loan: study.
#      Employment = retired. (study: 29)
#           Loan: study.




# ---------------------------------------------------------------------------
# SECTION 3: Classifiers
# ---------------------------------------------------------------------------

# In this project, a "classifier" will be a python class with methods for
# learning from examples and for classificationing the class of new examples,
# together with other possible methods (like the evaluation of its
# performance). Specifically, a classifier will be a subclass of the following
# generic python class:



class Classifier:
    """
    Base class for classifiers
    """

    def __init__(self, class_name,classes,attributes):

        """
        Constructor.
        
        Input arguments (see play_tennis.py, for example)
         
        * class_name: name of the classification attribute
        * classes: list of the different classes
        * attributes: list of pairs of attributes and its values
        """

        self.class_name = class_name
        self.classes = classes
        self.attributes = attributes
        


    def fit(self,train,valid=None):
        """
        Generic method for learning and tuning the classifier. 
        This must be defined for each particular classifier, which may add
        extra input arguments. 
        
        Input arguments:

        * train: examples of the training set
        * valid: examples of the validation set. Some basic classifiers 
                 do not use validation sets, so in those cases this argument 
                 will be omitted.
        """
        pass

    def classification(self, example):
        """
        Generic method to classify an example, once the classifier have been
        trained. It should be defined for each particular classifier.  

        If this method is called without fitting (training) the model
        previously, it has to return an exception ClassifierNotTrained
        (included below).
        """
        pass

    def print_classifier(self):
        """
        Generic method to print the learned classifier. It should be defined
        for each particular classifier.   

        If this method is called without fitting (training) the model
        previously, it has to return an exception ClassifierNotTrained
        (included below).
        """
        pass
        



# Exception returned when the classification or print_classifier methods are called
# without being trained previously.
        
class ClassifierNotTrained(Exception): pass

# CLASSES TO IMPLEMENT:
# =====================

# * Implement a class ClassifierTree as a subclass of the class
#   Classifier above, with the following methods:
#   - Train: the learn_tree algorithm implemented in Part I
#   - Classification: classification using the learned tree
#   - Print classifier: print the learned tree
#   In addition to the variable attributes of the parent class Classifier,
#   other attributes can be included if needed (for example, a variable
#   attribute to store the learned tree).

class ClassifierTree(Classifier):
    
    def __init__(self, class_name, classes, attributes):
        Classifier.__init__(self, class_name, classes, attributes)
        self.tree = None    #Added to check if the classifier was trained or not
    
    def fit(self, train):
        self.train(train)
    
    def train(self, train):
        Classifier.fit(self, train)
        #tree is stored in tree attribute from classifier
        self.tree = learn_tree(train, self.attributes) #train the classifier
        
    def classification(self, example):
        Classifier.classification(self, example)
        if type(self.tree) == type(NodeDT()):
            #If tree attribute from classifier is a node then classify it
            return classify_DT(example, self.tree)
        else:
            #If tree attribute is not inicialized then print and raise an error
            print("\t\t\t# Error, it is not trained yet")
            raise ClassifierNotTrained(Exception)

    def print_classifier(self):
        Classifier.print_classifier(self)
        if type(self.tree) == type(NodeDT()):
            #If tree attribute from classifier is a node then print it
            
            #print the tree stored in the tree attribute
            print_DT(self.tree, self.attributes, self.class_name)
        else:
            #If tree attribute is not inicialized then print and raise an error
            print("\t\t\t# Error, it is not trained yet")
            raise ClassifierNotTrained(Exception)
    

        

# * Implement a class ClassifierTreePrune, similar to the previous one, but
#   in which the tree finally used is obtained after applying reduced error
#   pruning on a learned tree.

class ClassifierTreePrune:
    
    def __init__(self, class_name, classes, attributes):
        Classifier.__init__(self, class_name, classes, attributes)
        self.tree = None
    
    def train(self, train, valid = None, max_freq_split = 1.0, min_prop_examples = 0):
        Classifier.fit(self, train, valid)
        self.tree = learn_tree(train, self.attributes, max_freq_split = max_freq_split, min_prop_examples = min_prop_examples) #train the classifier
        if valid != None:
            #if valid is not None there is a valid list to prune the tree
            
            #the pruned tree is stored removing the train tree
            self.tree = prune_tree(self.tree, valid) #prune the classifier
        
    def classification(self, example):
        Classifier.classification(self, example)
        if type(self.tree) == type(NodeDT()):
            #If tree attribute from classifier is a node then classify it
            return classify_DT(example, self.tree)
        else:
            #If tree attribute is not inicialized then print and raise an error
            print("\t\t\t# Error, it is not trained yet")
            raise ClassifierNotTrained(Exception)

    def print_classifier(self):
        Classifier.print_classifier(self)
        if type(self.tree) == type(NodeDT()):
            #If tree attribute from classifier is a node then print it
            
            #print the tree stored in the tree attribute
            print_DT(self.tree, self.attributes, self.class_name)
        else:
            #If tree attribute is not inicialized then print and raise an error
            print("\t\t\t# Error, it is not trained yet")
            raise ClassifierNotTrained(Exception)

# FUNCTION ASKED
# ===============

# * Implement the function "accuracy(classifier,examples)" that computes the
# accuracy of a (trained) classifier on a set of examples whose class is
# known.  
        

def accuracy(classifier, examples):
    #prints the accuracy from the tree from the classifier comparing with a list of examples
    print(accuracy_DT(classifier.tree, examples))  


# EXPERIMENTATION ASKED
# =====================

# In the case of votes.py and credit.py, compare the accuracy of both
# classifiers (without pruning, with prepruning using several parameters, with
# post pruning, with both...)  on the training, validation and test sets,
# discussing the results obtained.



# -----------

# Some examples:

# Play tennis:

# >>> classifier_pt=ClassifierTree(play_tennis.class_name,
#                                     play_tennis.classes,
#                                     play_tennis.attributes)
# >>> classifier_pt.classification(['Sunny','Mild', 'High','Strong'])
#                    # Error, it is not trained yet
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/usr/tmp/python3-33217RM.py", line 761, in classification
# __main__.ClassifierNotTrained

# >>> classifier_pt.train(play_tennis.train)

# >>> classifier_pt.print_classifier()
# Root node (no: 5  yes: 9)
#  Outlook = Sunny. (no: 3  yes: 2)
#       Humidity = High. (no: 3)
#            Play Tennis: no.
#       Humidity = Normal. (yes: 2)
#            Play Tennis: yes.
#  Outlook = Overcast. (yes: 4)
#       Play Tennis: yes.
#  Outlook = Rainy. (yes: 3  no: 2)
#       Wind = Weak. (yes: 3)
#            Play Tennis: yes.
#       Wind = Strong. (no: 2)
#            Play Tennis: no.

# >>> classifier_pt.classification(['Sunny','Mild', 'High','Strong'])
# 'no'

# >>> accuracy(classifier_pt,play_tennis.train)
# 1.0

# ----------

# Bank credit:

# >>> classifier_ct=ClassifierTree(credit.class_name,credit.classes,
#                                  credit.attributes)
# >>> classifier_ct.train(credit.train)
# >>> classifier_ct.print_classifier()
# .... very big tree, not displayed ........ 
# >>> accuracy(classifier_ct,credit.train)
# 1.0
# >>> accuracy(classifier_ct,credit.valid)
# 0.9197530864197531
# >>> accuracy(classifier_ct,credit.test)
# 0.8650306748466258

# -----
 
# Bank credit with pre and post pruning:

# >>> classifier_ctp=ClassifierTreePrune(credit.class_name,
#                                        credit.classes,
#                                        credit.attributes)
# >>> classifier_ctp.train(credit.train,credit.valid,
#                        max_freq_split=0.85,min_prop_examples=0.05)
# >>> classifier_ctp.print_classifier()
# Root node (study: 116  not grant: 107  grant: 102)
#  Income = low. (not grant: 73  study: 19  grant: 11)
#       Employment = official. (not grant: 9  study: 8  grant: 9)
#            Real estate = none. (not grant: 9)
#                 Loan: not grant.
#            Real estate = one. (study: 6)
#                 Loan: study.
#            Real estate = more. (study: 2  grant: 9)
#                 Loan: grant.
#       Employment = employed. (not grant: 17  study: 7)
#            Products = none. (not grant: 8)
#                 Loan: not grant.
#            Products = one. (not grant: 9)
#                 Loan: not grant.
#            Products = more. (study: 7)
#                 Loan: study.
#       Employment = unemployed. (study: 2  grant: 1  not grant: 24)
#            Loan: not grant.
#       Employment = retired. (study: 2  grant: 1  not grant: 23)
#            Loan: not grant.
#  Income = medium. (grant: 37  not grant: 34  study: 36)
#       Real estate = none. (not grant: 23  grant: 1  study: 14)
#            Employment = official. (study: 6)
#                 Loan: study.
#            Employment = employed. (grant: 1  not grant: 1  study: 6)
#                 Loan: study.
#            Employment = unemployed. (study: 2  not grant: 13)
#                 Loan: not grant.
#            Employment = retired. (not grant: 9)
#                 Loan: not grant.
#       Real estate = one. (not grant: 11  study: 22  grant: 1)
#            Products = none. (study: 1  grant: 1  not grant: 7)
#                 Loan: not grant.
#            Products = one. (study: 14)
#                 Loan: study.
#            Products = more. (not grant: 4  study: 7)
#                 Loan: study.
#       Real estate = more. (grant: 35)
#            Loan: grant.
#  Income = high. (study: 61  grant: 54)
#       Employment = official. (grant: 26)
#            Loan: grant.
#       Employment = employed. (study: 3  grant: 25)
#            Loan: grant.
#       Employment = unemployed. (grant: 3  study: 29)
#            Loan: study.
#       Employment = retired. (study: 29)
#            Loan: study.

# >>> accuracy(classifier_ctp,credit.train)
# 0.9261538461538461
# >>> accuracy(classifier_ctp,credit.valid)
# 0.9753086419753086
# >>> accuracy(classifier_ctp,credit.test)
# 0.9815950920245399







# ---------------------------------------------------------------------------
# SECTION 4: Explaining survival in the Titanic 
# ---------------------------------------------------------------------------

# In this part, you will have to use some of previous classifiers for
# explaining the reasons for survival in the Titanic sinking, from the
# available data about the passengers (downloadable from links in the web
# page). 


# For that, you should do the following steps: 

# - Data preprocessing: we have "raw data", so they have to be prepared to be
#   input for our classifiers. 
# - Learning and tuning the learned model, using the corresponding classifier
#   method. 
# - Evaluating the learned classifier


# We now give some suggestions for the first step (preprocessing):

# In the data set provided there are a number of attributes that obviously
# have no influence on survival (for example, the name of the passenger). This
# makes necessary to select as attributes the features that are actually
# believed relevant. This is usually done using some statistical techniques,
# but in this assignment only we are going to ask you to manually choose(in a
# reasonable way, or by testing several alternatives) THREE ATTRIBUTES that
# are considered to be the ones that best determine survival or not.


# The "Age" attribute is numeric, and our implementation does not treat well
# attributes with numerical values. There are techniques for treating
# numerical attributes, which basically divide the possible values to be taken
# into intervals, in the best possible way. In our case, for the sake of
# simplification, we will do it directly with the following criteria:
# transform the AGE value into a binary value, in which we only annotate if
# the passenger is 13 YEARS OLD OR YOUNGER, or if the passenger is OLDER than
# 13.


# In the data, there are some values from some examples, which appear as NA
# (unknown). Two very simple techniques for treating missing or unknown
# values: replace NA by the most frequent value in examples of the
# same class, or by the arithmetic mean of that value in the class (this last
# option only makes sense with numeric attributes).  

# To carry out training, pruning and performance measurement,you need to split
# the data into three parts: training, validation and testing. It is necessary
# to decide on the appropriate proportion of the data for each of these three
# parts. In addition, care has also to be taken to ensure that the partition
# is stratified: the proportion of examples according to the different values
# of the attributes must be in each part similar to the proportion in the
# whole set of examples.


# The final result of this last section should be:

# * A file titanic.py, with a format similar to the data files that has been
# provided (votes.py or credit.py, for example), in which we include the data
# resulted obtained after the preprocessing phase.  

# * A decision tree (the one obtained with the best performance), explaining
# survival in the Titanic sinking. Include comments explaining all the steps
# and experimentations carried out until this final tree has been
# obtained. Include the printed tree and the coments also in the file
# titanic.py 

def prepare_attributes():
    raw_attributes = {}
    titanic_textfile = open('titanic.txt', 'r')
    titanic_rows = titanic_textfile.read().split("\n")
    titanic_rows.remove('')
    
    attributes = titanic_rows[0].replace('"','')
    attributes = attributes.split(',')
    
    for attribute in attributes:
        #only iterate over chosen attributes
        if attribute !='pclass' and attribute !='age' and attribute != 'sex':
            continue   #jump to next iteration
        
        attrib_pos = attributes.index(attribute)
        raw_attributes[attribute] = []
        
        for row in titanic_rows[1:]:    #avoid the title row (1st one)
            #to avoid problems with the name of passengers
            pre_array = row.replace(', ','. ')
            #reconstruct posible damaged separators
            pre_array = pre_array.replace('". ', '",')
            #remove unnecesary '"'
            pre_array = pre_array.replace('"','')
            #separate by commas
            row_array = pre_array.split(',')
            #special classsification for 'age' --> if >13 -> Old else -> Young
            if attribute == 'age':
                #We only add the first possibility for each attribute
                if row_array[attrib_pos] == 'NA':   #to avoid no information attributes
                    pass
                elif float(row_array[attrib_pos]) <= 13.000 and 'young' not in raw_attributes[attribute]:
                    raw_attributes[attribute].append("young")
                elif 'old' not in raw_attributes[attribute]:
                    raw_attributes[attribute].append("old")
            else:
                if row_array[attrib_pos] not in raw_attributes[attribute]:
                    raw_attributes[attribute].append(row_array[attrib_pos])
    
    final_attrib = []
    
    #Prepare attribute in the same format as the one given in examples
    for key in raw_attributes:
        final_attrib.append((key,raw_attributes[key]))
    #No need to use raw input
    titanic_textfile.close()
    
    #Now reconstruct attributes in the objective file
    first = True #avoid writing in the first iteration
    titanic_file = open('titanic.py','a')
    titanic_file.write('attributes=[')
    for attrib in final_attrib:
        if first == True:
            first = False
        else:
            titanic_file.write(',\n\t\t\t')
        titanic_file.write(str(attrib))
    titanic_file.write(']')
    titanic_file.close()
    
    return final_attrib #Return the attributes list

def prepare_class():
    titanic_file = open('titanic.py','a')
    titanic_file.write("\n\nclass_name='Survived'\nclasses=['yes','no']")
    
def prepare_train():
    raw_train = []
    titanic_textfile = open('titanic.txt', 'r')
    titanic_rows = titanic_textfile.read().split("\n")
    titanic_rows.remove('')
    
    attributes = titanic_rows[0].replace('"','')
    attributes = attributes.split(',')
    
    
        
    for row in titanic_rows[1:]:    #avoid the title row (1st one)
        #to avoid problems with the name of passengers
        pre_array = row.replace(', ','. ')
        #reconstruct posible damaged separators
        pre_array = pre_array.replace('". ', '",')
        #remove unnecesary '"'
        pre_array = pre_array.replace('"','')
        #separate by commas
        row_array = pre_array.split(',')
        
        #store each 
        row_buffer = []
        for word in row_array:
            if (row_array.index(word) != attributes.index('pclass') and
            row_array.index(word) != attributes.index('age') and
            row_array.index(word) != attributes.index('sex')):
                continue
            else:
                row_buffer.append(word)
        row_buffer.append('yes' if int(row_array[2])==1 else 'no')
        raw_train.append(row_buffer)
    
    acum = 0.0
    cont = 0
    #Now we get the average 'age'
    for row in raw_train:
        if row[1] != 'NA':
            cont += 1
            acum += float(row[1])
    na = acum / cont
    #Transform the average 'age' in 'young' to avoid extra operations
    if na <= 13.0:
        na = 'young'
    else:
        na = 'old'
    
    #Lastly convert 'age' in 'young' or 'old'
    for row in raw_train:
        if row[1] == 'NA':
            row[1] = na
        else:
            if float(row[1]) <= 13.0:
                row[1] = 'young'
            else:
                row[1] = 'old'
    
    random.shuffle(raw_train)
    
    length = int(len(raw_train)/3)
    
    train = raw_train[:length]
    valid = raw_train[length:length*2]
    test = raw_train[length*2:]
    
    #Now reconstruct train in the objective file
    first = True #avoid writing in the first iteration
    titanic_file = open('titanic.py','a')
    titanic_file.write('\n\n\ntrain=[')
    for row in train:
        if first == True:
            first = False
        else:
            titanic_file.write(',\n\t\t\t')
        titanic_file.write(str(row))
    titanic_file.write(']')
    
    #Now reconstruct valid in the objective file
    first = True #avoid writing in the first iteration
    titanic_file = open('titanic.py','a')
    titanic_file.write('\n\n\nvalid=[')
    for row in valid:
        if first == True:
            first = False
        else:
            titanic_file.write(',\n\t\t\t')
        titanic_file.write(str(row))
    titanic_file.write(']')    
    
    #Now reconstruct test in the objective file
    first = True #avoid writing in the first iteration
    titanic_file = open('titanic.py','a')
    titanic_file.write('\n\n\ntest=[')
    for row in test:
        if first == True:
            first = False
        else:
            titanic_file.write(',\n\t\t\t')
        titanic_file.write(str(row))
    titanic_file.write(']')
    
    titanic_file.close()
    
    return raw_train

#modified version of print_DT to write on titanic.py fille the tree commented
def print_titanic(tree,attributes,class_name):
    titanic_doc = open('titanic.py','a')
    #first it is prepared the root node print 
    root_str = "\n\n#Titanic tree:\n#Root node ("
    not_first = False
    
    for one in tree.distr:
        if not_first:
            root_str += " "
        else:
            not_first = True
        
        root_str += one + ": "+str(tree.distr[one])
        
    
    root_str +=")\n"
    titanic_doc.write(root_str)
    #the next action is call the main method to print the tree recursively
    sub_print_titanic(titanic_doc,tree, attributes, class_name, 1)
    titanic_doc.write("\n")
    titanic_doc.close()
            
#the main function of print_titanic
def sub_print_titanic(titanic_doc,tree, attributes, class_name, tabs):
    #buffer to prepare the string to print
    pre_print = "#"
    
    
    #its added a tab for each iteration to easily read the tree printed
    for i in range(0,tabs):
        pre_print += "\t"
    
    #its checked if it is a leaf node and print it depending on that
    if tree.clas != None:
        pre_print += class_name + ": " + tree.clas + ".\n"
        titanic_doc.write(pre_print)
        
    elif attributes != None:
        #if there is attributes it is an inner node
        next_attribute = attributes[tree.attribute]
        
        #for each value for the attribute
        for option in next_attribute[1]:
            print_buf = pre_print
            print_buf += next_attribute[0] + " = " + option + ". ("
            
            cont = False #the first blank space is avoid
            
            if option in tree.branches.keys():
                #for each branch of the current node (only if it exists):
                for clas in tree.branches[option].distr:
                    
                    if not cont:
                        cont = True
                        
                    else:
                        print_buf += " "
                    #prepare in the buffer distribution of the node
                    print_buf += clas + ": " + str(tree.branches[option].distr[clas])
                print_buf += ")\n"
                #write the buffer and call the recursive function to print the tree adding 1 to the tabs
                #and a subtree for each option (for each call to the recursive function)
                titanic_doc.write(print_buf)
                sub_print_titanic(titanic_doc,tree.branches[option], attributes, class_name, tabs+1)

#calls every function that reconstruct the titanic.py file
def prepare_titanic():
    titanic_file = open('titanic.py','w') #remove all text
    titanic_file.write('# SURNAMES: Barea Rodríguez\n# NAME: Alejandro\n\n\n')
    titanic_file.close()
    prepare_attributes()
    prepare_class()
    prepare_train()
    ct = ClassifierTreePrune(titanic.class_name,titanic.classes,titanic.attributes)
    ct.train(titanic.train, titanic.valid)
    print_titanic(ct.tree, ct.attributes, ct.class_name)
    titanic_file = open('titanic.py','a') #remove all text
    
    #explanation of the process as comments
    titanic_file.write("\n\n'''\nI have prepared the raw set from titanic.txt iterating to extract attributes \nand its posible values.\nLater I get the class and its possible values from survived column (survived)\nand traduct the 1->yes 0->no.\nThen we prepare examples:\n\t-First I extract and prepare the set to iterate over it and construct a \n\tlist with the same format required for learn_tree.\n\t-Secondly 'NA' from age is substituted by the average age that is old in \n\tthis case. Now it is almost ready\n\t-Lastly I mix all examples because they are ordered by id but this is also \n\trelated to the pclass. It is easy to notice that if the examples are \n\tdirectly divided in 3 list the first (train) will contain mostly 1st class,\n\t2nd class would be in valid set and the rest in test set.\nAfter this we can use classifiers to learn a tree, prune it and \nprint it and analysing it.\nhe reason of choosing these attributes are simple:\n\t-One of them is sex is asociated with the possibility of surviving or not.\n\t-The other is the class because 1st class had priority over the other,\n\tin fact it is easy to notice that mainly the 3rd class did not survived.\n\t-Other attributes as the name, the ticket, embark or the origin are not really \n\timportant so they are omitted.\n\t-Boat and destiny are dificult to analize because there are many\n\tposibilities in both. In the boat case there are many options but the most\n\timportant one is having used a boat or not (if not they have not many\n\tprobabilities to survive) and picking or no the boat is also related with\n\tthe class and the sex.\n\thad many time to embark in boats before 3rd class and this is supported by \n\tthe data set.\n'''")
    titanic_file.close()
    