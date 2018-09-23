# ==========================================================
# Artificial Intelligence.  ETSII (University of Seville).
# Course 2017-18
# Deliverable 02 
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


# 

# This assignment consists in finishing the practice 03, partially done in the
# lab class on Nov 23rd (we did until exercise 06). The main goal of the
# practice is to define a genetic algorithm (the one presented in slide 17 of
# unit 5) and apply it to solve some instances of a simple knapsack problem. 

# The exercises 1 to 6 in Practice 3 were done in that class. The definitions
# of the functions asked in those exercises have to be included here. If you
# did not attend the class (or even if you did), you can ask for the solutions
# of those exercises to the teacher (by email), or even to some of your
# classmates. But ONLY THOSE EXERCISES. THE REST OF THE EXERCISES HAVE TO BE
# DONE INDIVIDUALLY.

# ------------------------------------------------------------------

# ==============================================
# Part I: Implementation of a genetic algorithm 
# ==============================================

# We will need again the random module
import random



# Include here the definitions of the functions of exercises 1 to 6.

class Problem_Genetic():
    
    def __init__(self, genes, individuals_length, decode, fitness):
        self.genes = genes
        self.individuals_length = individuals_length
        self.decode = decode
        self.fitness = fitness
        
        
    def mutation(self, chromosome, probability):
        chromosomeMutated = chromosome[:] #Copy, not a pointer to chromosome
        
        for i in range(self.individuals_length):
            
            if random.random()<probability:
                chromosomeMutated[i] = random.choice(self.genes)
        
        return chromosomeMutated
    
    
    def crossover(self, chromosome1, chromosome2):
        position = random.randrange(1,self.individuals_length-1)
        chromosomeM1 = chromosome1[:position]+chromosome2[position:]
        chromosomeM2 = chromosome2[:position]+chromosome2[position:]
        return chromosomeM1,chromosomeM2

def binary_to_decimal(x):
    return sum(b*(2**i) for (i,b) in enumerate(x)) 

sq_gen = Problem_Genetic([0,1],10,binary_to_decimal,lambda chromosome: (binary_to_decimal(chromosome))**2)

def initial_population(problem_genetic, size):
    return [[random.choice(problem_genetic.genes)
             for _ in range(problem_genetic.individuals_length)]
             for _ in range(size)]

def crossover_parents(Problem_Genetic, parents):
    kids = []
    for j in range(0, len(parents)-1,2):
        
        kids.extend(Problem_Genetic.crossover(parents[j],parents[j+1]))
        #incompleto
    return kids

def mutate_individuals(Problem_Genetic,population,prob):
    return [Problem_Genetic.mutation(c,prob) for c in population]

def select_one_by_tournament(problem_genetic, population, k, opt): #opt is MAX or MIN
    participants = random.sample(population, k)  #copy, but with no repetitions
    return opt(participants, key = problem_genetic.fitness) #opt -> pointer to function (it should be min or max)

def tournament_selection(problem_genetic, population, n, k, opt):
    genes = []
    for _ in range(n):
        genes.append(select_one_by_tournament(problem_genetic, population, k, opt))
    
    return genes


# -----------
# Exercise 7
# -----------

# Using the previous auxiliary functions, define a function new_generation_t
# for computing a new generation from a given one, as described in the slide
# 17 of unit 5 (the genetic algorithm that uses tornement selection).

# We will assume the following seven input arguments: 
 
# new_generation_t(problem_genetic,k,opt,population,
#                  n_parents,n_direct,prob_mutate)

# where:

# * problem_genetic: an instance of the class Problem_Genetic, with
#     the optimization problem that we want to solve.
# * k: number of participants in the selection tournaments.
# * opt: max or min, indicating if it is a maximization or a
#     minimization problem.
# * population:the current generation
# * n_parents: the number of parents 
# * n_direct: the number of individuals taken directly for the 
#             next generation 
# * prob_mutate: probability that a gene mutation will take place.

# NOTE: we will assume that n_parents+n_direct is equal to the size of the
# population. These numbers n_parents and n_direct will be computed in the
# function of the next exercise, that uses new_generation_t.


# =========== Solution:

def new_generation_t(problem_genetic,k,opt,population, n_parents,n_direct,prob_mutate):
    
    tournament_winners = tournament_selection(problem_genetic, 
                                              population, n_parents, k, opt) #get the best chromosomes (n_parents) from population
    
    random_selection = random.sample(population, n_direct) #get a random group from the population (given the population and the proportion)
    
    sons = crossover_parents(problem_genetic, tournament_winners) #get sons from the tournament winners
    
    prepopulation = sons + random_selection #join sons and direct individuals to get a new population
    
    population = mutate_individuals(problem_genetic, prepopulation, prob_mutate) #randomly mutate given the problem, the population and the prob of mutating
    
    return population
    




# =======================



# -----------
# Exercise 8
# -----------


# Implement the genetic algorithm described in slide 17 of unit 5. That is,
# define a function:  

# genetic_algorithm_t(problem_genetic,k,opt,ngen,size,
#                      ratio_cross,prob_mutate)

# where the input arguments are:

# * problem_genetic: an instance of the class Problem_Genetic, with
#     the optimization problem that we want to solve.
# * k: number of participants on the selection tournaments.
# * opt: max or min, indicating if it is a maximization or a
#     minimization problem.
# * ngen: number of generations (halting condition)
# * size: number of individuals for each generation
# * ratio_cross: portion of the population which will be obtained by
#     means of crossovers. 
# * prob_mutate: probability that a gene mutation will take place.

# The function genetic_algorithm_t should return the phenotype of the best
# individual in the last generation computed, along with its fitness. 

# After defining it, run the previous genetic algorithm to solve the
# sq_gen problem (both in its minimization and maximization variants).

# For example:

# >>> genetic_algorithm_t(sq_gen,3,min,20,10,0.7,0.1)
# (0, 0)
# >>> genetic_algorithm_t(sq_gen,3,max,20,10,0.7,0.1)
# (1023, 1046529)


# ============= Solution:


def genetic_algorithm_t(problem_genetic,k,opt,ngen,size,ratio_cross,prob_mutate):
    
    n_parents = int(ratio_cross * size) #proportion of parents
    
    n_direct = int((1 - ratio_cross) * size) #proportion of individuals that directly pass to the next generation
    
    cont = 0
    
    
    population = initial_population(problem_genetic, size) #generate the population randomly
    #eval
    best = select_one_by_tournament(problem_genetic, population, len(population), opt) #get the best
    
    while cont < ngen:#continue until a number of iteration is done
        population = new_generation_t(problem_genetic, k, opt, population,
                                      n_parents, n_direct, prob_mutate) #get a new gen 
        #eval
        best = select_one_by_tournament(problem_genetic, population, len(population), opt) #get the best
        
        cont = cont + 1 #next iteration
    
    return problem_genetic.decode(best),problem_genetic.fitness(best)#return the chromosome and its value

#fitness_knapsack(chromosome, n_objects, weights, capacity, values)
#decode_knapsack(chromosome, n_objects, weights, capacity)

# ===============


# ================================================
# Part II: Representation of the Knapsack problem
# ================================================


# The Knapsack problem can be stated as follows: given n objects of
# weights w_i and value v_i (i=1,...,n), select which objects should
# be carried in a knapsack having a maximum weight P, in such a way
# that the value of the selected objects is maximum.

# We will use the following representation:
# GENES: [0,1]
# INDIVIDUALS-LENGTH: N
# DECODE(X): we read the chromosome from left to right, a 1 at
#    position i means that the i-th object is selected, with the
#    following exception:
#    If by selecting the object we go beyond the max weight, then this
#    object is not selected (and neither is none of the remaining).
# F-OBJECTIVE(X): sum of the values of the selected objects
#    (note that no penalty is required because of our decode function)


# -----------
# Exercise 8
# -----------

# Define a function 
# decode_knapsack(chromosome, n_objects, weights, capacity)
# that receives as input:

# - a chromosome (i.e. a list of 0s and 1s, of length equal to
#     n_objects) 
# - n_objects: total number of available objects
# - weights: a list with the weight of each object
# - capacity: maximum weight of the knapsack.

# The output of this function is a list of 0s and 1s representing the
# set of selected objects (the i-th object is selected if and only if
# there is a 1 at position i). This list is obtained from the
# chromosome, filtering the objects that are discarded according to
# the DECODE description.


# ========== Solution:


def decode_knapsack(chromosome, n_objects, weights, capacity):
    
    actual_weight = 0
    representation = []
    
    for i in range(n_objects):
        if chromosome[i]*weights[i]+actual_weight <= capacity:
            #if the new object can be represented (there is weigth enough) it is added
            representation.append(chromosome[i])
            actual_weight = actual_weight + weights[i]*chromosome[i]
        else:
            #if the object is too heavy the object is not added (add 0 in its place)
            representation.append(0) 
    
    return representation



# ==============================================


# -----------
# Exercise 9
# -----------

# Define a function 

# fitness_knapsack(chromosome, n_objects, weights, capacity, values)

# that calculates the total value of the objects carried out inside the knapsack
# represented by the chromosome, according to the codification
# explained in the previous exercise.
# The function receives as input the same arguments as the previous
# function, together with 'values', which is a list with the value of
# each object.


# ============== Solution:

def fitness_knapsack(chromosome, n_objects, weights, capacity, values):
    
    acum = 0
    real_chromosome = decode_knapsack(chromosome, n_objects, weights, capacity) #to get the correct expression of the chromosome
    for i in range(n_objects):
        acum = acum + (real_chromosome[i] * values[i]) #acum the value of each object in the chromosome
    
    return acum



# ===============================================



# =====================================================
# Part III: Solving instances of the  Knapsack problem
# =====================================================


# Below you can find three particular instances of the Knapsack
# problem. Their corresponding optimal solutions are also given, in
# order to compare them against the results obtained by the genetic
# algorithm:

# _______________________________________________________
# Knapsack problem 1:
# 10 objects, maximum weight 165
weights1 = [23,31,29,44,53,38,63,85,89,82]
values1 = [92,57,49,68,60,43,67,84,87,72]
#fitness_knapsack([1,1,1,1,0,1,0,0,0,0], 10, weights1, 165, values1)
# Optimal solution= [1,1,1,1,0,1,0,0,0,0], value= 309
# _______________________________________________________

# _______________________________________________________
# Knapsack problem 2:
# 15 objects, maximum weight 750

weights2 = [70,73,77,80,82,87,90,94,98,106,110,113,115,118,120]
values2 = [135,139,149,150,156,163,173,184,192,201,210,214,221,229,240]
#fitness_knapsack([1,0,1,0,1,0,1,1,1,0,0,0,0,1,1], 15, weights2, 750, values2)
# Optimal solution= [1,0,1,0,1,0,1,1,1,0,0,0,0,1,1], value= 1458
# _______________________________________________________


# _______________________________________________________
# Knapsack problem 3:
# 24 objects, maximum weight 6404180
weights3 = [382745,799601,909247,729069,467902, 44328,
       34610,698150,823460,903959,853665,551830,610856,
       670702,488960,951111,323046,446298,931161, 31385,496951,264724,224916,169684]
values3 = [825594,1677009,1676628,1523970, 943972,  97426,
       69666,1296457,1679693,1902996,
       1844992,1049289,1252836,1319836, 953277,2067538, 675367,
       853655,1826027, 65731, 901489, 577243, 466257, 369261]
#fitness_knapsack([1,1,0,1,1,1,0,0,0,1,1,0,1,0,0,1,0,0,0,0,0,1,1,1], 24, weights3, 6404180, values3)
# Optimal solution= [1,1,0,1,1,1,0,0,0,1,1,0,1,0,0,1,0,0,0,0,0,1,1,1], value= 13549094

# _______________________________________________________
#k1g = [1, 1, 1, 1, 0, 1, 0, 0, 0, 0]

# -----------
# Exercise 10
# -----------

# Define variables k1g, k2g and k3g, containing the instances of
# Problem_Genetic corresponding, respectively, to the previous three
# instances of the knapsack problem.

# Use the genetic algorithm to solve these problems.

# For example:

# >>> genetic_algorithm_t(k1g,3,max,100,50,0.8,0.05)
# ([1, 1, 1, 1, 0, 1, 0, 0, 0, 0], 309)

# >>> genetic_algorithm_t(k2g,3,max,100,50,0.8,0.05)
# ([1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0], 1444)
# >>> genetic_algorithm_t(k2g,3,max,200,100,0.8,0.05)
# ([0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0], 1439)
# >>> genetic_algorithm_t(k2g,3,max,200,100,0.8,0.05)
# ([1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1], 1458)

# >>> genetic_algorithm_t(k3g,5,max,400,200,0.75,0.1)
# ([1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0], 13518963)
# >>> genetic_algorithm_t(k3g,4,max,600,200,0.75,0.1)
# ([1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], 13524340)
# >>> genetic_algorithm_t(k3g,4,max,1000,200,0.75,0.1)
# ([1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], 13449995)
# >>> genetic_algorithm_t(k3g,3,max,1000,100,0.75,0.1)
# ([1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], 13412953)
# >>> genetic_algorithm_t(k3g,3,max,2000,100,0.75,0.1)
# ([0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 13366296)
# >>> genetic_algorithm_t(k3g,6,max,2000,100,0.75,0.1)
# ([1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1], 13549094)



# =========== Solution:

#lambda function are needed to prepare knapsack decode and fitness function with correct weigths and values

k1g = Problem_Genetic([0,1], 10,lambda y: decode_knapsack(y,10,weights1,165), lambda x: fitness_knapsack(x,10,weights1,165,values1))

k2g = Problem_Genetic([0,1], 15, lambda x:decode_knapsack(x, 15, weights2, 750),lambda x: fitness_knapsack(x, 15, weights2, 750, values2))

k3g = Problem_Genetic([0,1], 24,lambda x: decode_knapsack(x,24, weights3, 6404180),lambda x:fitness_knapsack(x, 24, weights3, 6404180, values3))

#Extra example

#define a weigth and value for each objct (they must be in the same possition)
weights4 = [2,1,4,1,12]
values4 = [2,1,10,2,4]
k4g = Problem_Genetic([0,1], 24,lambda x: decode_knapsack(x,5, weights4, 15),lambda x:fitness_knapsack(x, 5, weights4, 15, values4))


# ===================================

# End of file

