# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 15:05:50 2020

@author: 33849
"""
# Ch 4 in P4e - loops
TARGET = 100000
INTERESTRATE = 0.02
year = 0
balance = 5000
while balance < TARGET:
    year = year + 1
    interest = INTERESTRATE * balance
    balance = balance + interest
    print(balance,year)
    
count = 0
while count < 10:
    count += 1
    print(count)
    
# Hvilket år vil et bankinnskudd på 50.000 kroner til 5% årlig rente
# bli likt eller høyere enn et bankinnskudd på 100.000 kroner til 2 % årlig rente? 
INNSKUDD_A = 50000
INNSKUDD_B = 100000
RENTE_A = 0.05
RENTE_B = 0.02
balanse_a = INNSKUDD_A
balanse_b = INNSKUDD_B
renteinntekt_a = balanse_a * RENTE_A
renteinntekt_b = balanse_b * RENTE_B
aar = 0

while balanse_a < balanse_b:
    balanse_a = balanse_a + renteinntekt_a
    balanse_b = balanse_b + renteinntekt_b
    aar += 1
#    print(balanse_a, end="  ")
#    print(balanse_b, end="  ")
#    print(aar)
print("Det tar", aar, "år før det lavere bankinnskuddet blir minst like høyt som det andre")
    

