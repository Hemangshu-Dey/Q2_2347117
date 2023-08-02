
#Is the given list divisible by 3 or NOT?
age=[3,30,2,5]
number_list=[x for x in age if x%3==0]
print("The numbers divisible by 3 is",number_list)


#Square of even numbers in a list
product_price=[3,45,20,180]
sum=0
number_list=[x for x in product_price if x%2==0]
for i in number_list:
    sum=sum+i
print(sum)


#Sum of digits of all EVEN numbers in a list
product_weight=[50,10 ,37, 89]
new_list=[]
number_list=[x for x in product_weight if x%2==0]
for i in number_list:
    square=i*i
    new_list.append(square)
print(new_list)


#Remove duplicate numbers in a list
age=[44,55,92,44,29]
new_age=[]
for i in age:
    if i not in new_age:
        new_age.append(i)
print(new_age)



# Create a dictionary to store the details of your company employees (name as key and
# birthdate as value).
# { ‘Virat Kohli’: ‘5 November 1988’, ‘Umesh Yadav’: ‘25 October 1987’, ‘Manish Pandey’:
# ‘10 September 1989’, ‘Rohit Sharma’: ‘30 April 1987’, ‘Ravindra Jadeja’: ‘6 December
# 1988’, ‘Hardik Pandya’: ‘11 October 1993’ }
# Write a function birthDate() that takes the full name of your employees(as a string) and
# displays the given employee’s birthdate.
# >>>birthDate(‘Rohit Sharma’)
# ‘30 April 1987’
def birthDate(name):
    emp_names={"Sanjay Yadav":"20 September 1997","Ravi Kumar":"12 January 2000","Amar Shah":"30 July 1996"}
    for i in emp_names.keys():
        if i==name:
            print(emp_names[name])
            break

name=input("Enter the employee name:")
birthDate(name)



