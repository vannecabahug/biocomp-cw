# biocomp-cw
Data mining exercise - Building a Genetic Algorithm

This algorithm will initialise a population (P) which consists of randomly generated binary integers (N);
Data is then read in from external text files provided that include a set of 'rules', this being 6-digit binary strings and a 7th placeholder of either 0 or 1.
The aim for this algorithm is to match the generated population with the ruleset and if so, increments fitness by 1
the goal is to reach a fitness of 60 as each dataset contains 60 rules.

! IMPORTANT !
Will need to download data1.txt and data2.txt source codes and place in the same file directory as the assignment python file in order to work and read in data.
You are only allowed to change values of variables: N, P, G and mutationRate.
Running the program will ask which dataset file would you like to open and will require user input; simply type either 1 or 2 for corresponding text files.


The algorithm includes selection, crossover and mutation and will try to reach a fitness of 60 in the least amount of generations.
