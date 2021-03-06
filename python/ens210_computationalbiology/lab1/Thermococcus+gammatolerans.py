
# coding: utf-8

# In[11]:

import pandas as pd 


# In[12]:

my_file_name = "C:/Users/Sena Cetin/Downloads/Streptomyces_coelicolor.txt"
my_file = open(my_file_name)
my_file_contents = my_file.read()
my_dna = my_file_contents.rstrip("\n")
#dna_length = len(my_file_contents)
#print("sequence is " + my_file_contents + " and the number of nucleotides is " + str(dna_length))


# In[13]:

print("#A = " + str(my_dna.count('A')))
print("#C = " + str(my_dna.count('C')))
print("#G = " + str(my_dna.count('G')))
print("#T = " + str(my_dna.count('T')))


# In[14]:

number_of_nucleotides = my_dna.count('A') + my_dna.count('C') + my_dna.count('G') + my_dna.count('T')
print(number_of_nucleotides)


# In[15]:

percentage_of_A = ((my_dna.count('A')/number_of_nucleotides) * 100)
percentage_of_A = round(percentage_of_A, 1)

percentage_of_C = ((my_dna.count('C')/number_of_nucleotides) * 100)
percentage_of_C = round(percentage_of_C, 1)

percentage_of_G = ((my_dna.count('G')/number_of_nucleotides) * 100)
percentage_of_G = round(percentage_of_G, 1)

percentage_of_T = ((my_dna.count('T')/number_of_nucleotides) * 100)
percentage_of_T = round(percentage_of_T, 1)


# In[16]:

print("A% = " + str(percentage_of_A))
print("C% = " + str(percentage_of_C))
print("G% = " + str(percentage_of_G))
print("T% = " + str(percentage_of_T))


# In[17]:

my_file.close()

