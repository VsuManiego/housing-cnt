# File: G402_Caberos,Noval,Tadura.py
# Author: Charlene Noval, Jared Caberos, Franz Ian Tadura
# Date created: 2021/11/29
#Cost-Efficient Indicator on Constructing A Housing Project
print("Welcome!")
print("This is a Cost-Efficient Indicator on Constructing A 4m x 6m Housing Project.")
print()


#Asking the User for the total amount spent
print("Enter the Amount Spent on:")
print()


#The user is instructed to input the total amount of each of the following: construction supervision, materials, supplies, labour cost, tools, equipment, and transportation.
construction_supervision_fee = float(input("Construction Supervision Fee: "))
materials = float(input("Materials: "))
supplies = float(input("Supplies: "))
labor = float(input("Labor: "))
tools = float(input("Tools: "))
equipment = float(input("Equipment: "))
transportation = float(input("Transportation: "))


#Total Amount Spent
total_cost = construction_supervision_fee + materials + supplies + labor + tools + equipment + transportation
print("----------------------------------------------")
print(f"\nThe total cost of the project is: ₱{total_cost:,.2f}")

#Check the total cost whether it is cost-efficient or not
#Check the total cost whether it is cost-efficient or not
if total_cost <= 30000:
    print("The project is Cost-Efficient.")
    print("------------------------------")
else:
    print("The project is not Cost-Efficient.")
    print("----------------------------------")