
"""
Created on Wed Nov 20 16:57:43 2019

@author: vanne
"""

'''
D1 params [best = 33 generations] = N 70   P 100   G 500   mRate 0.01
'''

import random
import matplotlib.pyplot as plt

###     CHANGE CODE VARIABLES HERE     #############################

N = 70
# Number of bits in the chromosome

P = 100
# Population size / Number of individuals

G = 500
# Number of MAX generations

mutationRate = 0.01
# Rate generating the chances of a bit changing in an individual


###################################################################



population = []
# Initialise individual arrarys where "0" and "1" integers are stored
fitness_scores = []
# List to store the scores of all fitness in inital population
winnerList = []
# List to store all winners from selection process
mutList = []
# List to store all chromosomes after mutation
offspringList =[]
# List to store all offsprings from crossover process
average_fitness = []
# List to store all averages on current fitness using sum and division
best_scores =[]
# A list to record all best fitness that comes up during the run
best = []
# List to store best
tempBest = []
# Temporary list to compare fitness of previously stored best and new current best
worst = []
# List to store worst

tempList2 = []
data = []

################    OPEN TEXT FILES    ################
def data1():
    data1 = list()
    with open("data1.txt") as f:
        for line in f:
            data1.append(line)
        data1 = [line.rstrip('\n') for line in open("data1.txt")]
        
        for item in data1:
            data.append(item)


def data2():    
    data2 = list()
    with open("data2.txt") as f:
        for line in f:
            data2.append(line)
        data2 = [line.rstrip('\n') for line in open("data2.txt")]
        
        for item in data2:
            data.append(item)

# User input to what dataset they want to classify
dataset = input("Which dataset would you like to open? ")
if dataset == '1':
    data1()
elif dataset == '2':
    data2()

########################################################


############     INITIATE POPULATION     ###############
print("\nInitial Population")
    
for i in range(P):
    population.append([])      # Append P amount of individuals to create the pop size
    
for i in population:
    for z in range(N):
        mod = z % 7            # every 7th bit can only be a 1 or a 0
        if mod-6 == 0:
            value = random.randint(0,1)
            i.append(value)
        else:
            value = random.randint(0,2)     # every bit that is not a multiple of 7, add 1s and 0s
            i.append(value)

"""
for i in population:
    print(i)
"""

tempList = population.copy()
#######################################################


############    FITNESS FUNCTION    ###################
def fitnessFunc(list):
    ruleList = []                       # List to store rules
    temp_scores = []
    calculateAverage = []               # copies fitness_scores to do sum and get average
    
    evaluationList = list.copy()        # Whatever list come in the parameter becomes localised
    
    while len(evaluationList) != 0:     # for all individuals in the list, pop out of list and split into rules
        for i in range(int(N/7)):       
            ruleList.append([])         # number of rules an individual needs
        for i in evaluationList:
            single_chromosome = i
        for rule in ruleList:
            for genes in single_chromosome[:int(7)]:    
                rule.append(genes)
            single_chromosome = single_chromosome[int(7):]          # Splits every 7
            
        evaluationList.pop()
        
        # Calculates fitness
        fitness = 0
        for item in data:               # uses items from data set and prepares to match
            for rule in ruleList:
                k = 0
                while k < 6:
                    if int(item[k]) == rule[k] or rule[k] == 2:     # Checks if every bit has the same value or if a 2 appears
                        k += 1                                      # then continues to next index
                    else:
                        break       # if condition does not match, proceed and don't check output
                else:
                    if int(item[-1]) == rule[-1]:       # checks 7th bit output
                        fitness += 1                    # if a match fitness increases by 1
                    break
        
        fitness_scores.append(fitness)
        calculateAverage.append(fitness)
        temp_scores.append(fitness)

        # append all fitness to use for later
        
        ruleList.clear()
        

    bestFitness = max(temp_scores)      # Max fitness
    worstFitness = min(temp_scores)     # Min fitness

    for i in list:
        i.append(temp_scores.pop())     # appending corresponding fitness to last position for all chromosomes
        
    temp_scores.clear()                 # to use again in generation
        
    if best == []:
        for i in list:
            if (int(bestFitness) in i):
                best.append(i)          # if best empty then append first best, only occurs first time
                while len(best) != 1:
                    best.pop()          # if more than one of the same number of best fitness exist - only want one
        for i in best:
            print("Best chromosome with fitness of ", i[-1])
    else:
        if tempBest == []:              # runs throughout generation
            for i in list:
                if (int(bestFitness) in i):
                    tempBest.append(i)
                    while len(tempBest) != 1:
                        tempBest.pop()          # if more than one best fitness in that generation - only want one
        # Comparing previous best fitness to newest best fitness in current generation
        for i in best:
            for j in tempBest:
                if i[-1] >= j[-1]:
                    tempBest.clear()
                    best_scores.append(i[-1])
#                        print("Best is still = ", best)
                else:
                    best.clear()
                    for j in tempBest:
                        best.append(j)          # tempBest becomes best so that this line can run continuously
                    tempBest.clear()
                    best_scores.append(j[-1])
#                        print("New best = ", best)
#        print(best_scores)
         
        for j in list:                   
            if j[-1] == int(worstFitness):      # check to see for all items in list if int exists in last position
                                                # if worst = 0 or 1 or 2, all individuals have these integers in all positions
                worst.append(j)                 # keep track of worst
                while len(worst) != 1:
                    worst.pop()                 # get rid of more than one worst
        for i in worst:
            print("\nWorst chromosome with fitness of ", i[-1], "removed")
        for i in worst:
            for j in list:
                if i == j:
                    list.remove(j)  
                    # compares to see if item in worst storing minimum fitness exists in item in list
                    
        worst.clear()       # to use again
                    
        for i in best:
            list.append(i)  # add best
            print("Added best with fitness of ", i[-1], "\n")
            
        # calculate average from fitness since they were all appended onto pop list - use this list to calculate
        average = sum(calculateAverage) / P     
        average_fitness.append(average)
#        best_scores.append(int(bestFitness))
                
        for j in list:
            tempList2.append(j)
            
    mutList.clear()
fitnessFunc(tempList)
##################################################
    
     
#####              SELECTION              #####
def selection():
    tempWinner = []
    for i in range(P):   
            individual_1 = random.choice(tempList)      
            individual_2 = random.choice(tempList)

            
            # Randomly chosen two individuals for tournament selection
            # appends highest fitness
            if individual_1[-1] > individual_2[-1]:
                tempWinner.append(individual_1)
            else:
                tempWinner.append(individual_2)

    for i in tempWinner:
        winnerList.append(i[:-1])   # gets rid of fitness appended on end
        
    tempList.clear()
#    print("\n")
#    for i in winnerList:
#        print(i)
selection()
################################################
    

######               CROSSOVER             #####
def crossover():
#    print("Offspring list")
    tempList = winnerList.copy()
    winnerList.clear()
    
    # for all individuals in list, picks parents by pairs and chooses crossover point
    for i in tempList:
        parent1 = tempList[0]
        tempList.remove(parent1)
        parent2 = tempList[0]
        tempList.remove(parent2)
        crossPoint = random.randint(1, len(parent1)-1)
        offspring1 = parent1[:crossPoint] + parent2[crossPoint:]
        offspring2 = parent2[:crossPoint] + parent1[crossPoint:]
        offspringList.append(offspring1)
        offspringList.append(offspring2)
        
    # Have to run twice to get all individuals in list for some reason
    for i in tempList:
        parent1 = tempList[0]
        tempList.remove(parent1)
        parent2 = tempList[0]
        tempList.remove(parent2)
        crossPoint = random.randint(1, len(parent1)-1)
        offspring1 = parent1[:crossPoint] + parent2[crossPoint:]
        offspring2 = parent2[:crossPoint] + parent1[crossPoint:]
        offspringList.append(offspring1)
        offspringList.append(offspring2)
    
    tempList.clear()
    """
    for i in offspringList:
        print(i)
    """    
crossover()    
#################################################


#######               MUTATION              #####
def mutation():
    tempList = offspringList.copy()
    offspringList.clear()
#    print("Mutation list")
    for i in tempList:
        for index, z in enumerate(i):
            if random.random() < mutationRate:
                if (index % 7)-6 != 0:  # mutates all genes not in 7th bit
                    if z == 1:
                        i[index] = random.choice([0,2])
                    elif z == 0:
                        i[index] = random.choice([1,2])
                    elif z == 2:
                        i[index] = random.choice([0,1])
                else:   # mutates 7th bit making sure it never becomes a 2
                    if z == 1:
                        i[index] = 0
                    elif z == 0:
                        i[index] = 1
                    
        mutList.append(i)
    tempList.clear()
 
mutation()
fitnessFunc(mutList)
#################################################


############     GENERATIONS         ###########
counter = 0 
GOAL = 60   # fitness we need to get
while counter < G:
    print("\nGENERATION ", counter+1)    
    tempList = tempList2.copy()
    tempList2.clear()

    selection()
    crossover()
    mutation()
    fitnessFunc(mutList)
    counter+=1
    
    if GOAL in fitness_scores:
        print(GOAL, "fitness found in generation", counter )
        print("Found in", int(N/7), "rules")
        print("Pop size =", int(P), "     Mutation rate =", float(mutationRate))
        break
    else:
        print("Parameters:\n")
        print("Rules =", int(N/7), "     Pop size =", int(P), "     Mutation rate =", float(mutationRate))
    
#######################################################
      
  
####################    GRAPH   #######################
plt.plot(best_scores, label="Best")
plt.plot(average_fitness, label="Average")        
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.legend(fancybox=True, shadow=True, loc="lower right", ncol=2)
plt.show()
#####################################################
    