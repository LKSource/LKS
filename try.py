#lex_auth_01269442545042227276

def find_ten_substring(num_str):
    listv = list(num_str)
    resultl = []
    for i in range(0,len(num_str)):
        sum = 0
        temp = ''
        j = i
        while sum <= 10 and j < len(num_str):
            sum += int(num_str[j])
            temp = temp + num_str[j]
            if sum == 10:
                resultl.append(temp)
            j+=1
            
             
    return (resultl)
    #Remove pass and write your logic here

num_str="3523014"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)
___

#lex_auth_01269442760027340879

def find_smallest_number(num):
    #start writing your code here    
    for value in range(1,1000):
        listv = []
        for n in range(1,value+1):
            if value%n == 0:
                listv.append(n)
        if len(listv) == num:
            return value

num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)

____

import turtle
wn = turtle.Screen()
wn.setup(500,500)
turtle = turtle.Turtle()
turtle.speed("fastest")

step = 100
def draw_square(length,angle,step):
    if step == 100:
        return
    else:    
        for b in range (0,4):
            turtle.forward(length+step)
            turtle.right(angle+b)
        draw_square(length, angle, step + 1)
            
draw_square(100,90,0)

_____

#lex_auth_01269442963365068878

def Largest_Prime_Factor(n):
    prime_factor = 1
    i = 2

    while i <= n / i:
        if n % i == 0:
            prime_factor = i
            n /= i
        else:
            i += 1

    if prime_factor < n:
        prime_factor = n
    return prime_factor

def find_factors(num):
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors

def is_prime(num, i):
    #Accepts the number num and num/2 --> i and returns True if the number is prime ,else returns False
    if(i==1):
        return True
    elif(num%i==0):
        return False;
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    return
    #Accepts the list of factors and returns the largest prime factor

def find_f(num):
    return
    #Accepts the number and returns the largest prime factor of the number

def find_g(num):
    print(Largest_Prime_Factor(num))
    #Accepts the number and returns the sum of the largest prime factors of the 9 consecutive numbers starting from the given number

#Note: Invoke function(s) from other function(s), wherever applicable.

print(find_g(12))

_____

#lex_auth_01269442114344550475

def rev(word,i):
    if i == 0:
        return word[0]
    else:
        return word[i] + rev(word,i-1)

def is_palindrome(word):
    revw = rev(word, len(word)-1)
    if word.upper() == revw.upper() :
        return True
    else:
        return False
    #Remove pass and write your logic here

#Provide different values for word and test your program
result=is_palindrome("Malayalam")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
    
______

#lex_auth_01269437527007232044

def human_pyramid(no_of_people):
    if (no_of_people) == 1:
        return 1 * 50
    else:
        return (no_of_people * 50) + human_pyramid(no_of_people - 2)
    #remove pass and place the recursive code the you had written earlier for this function

def find_maximum_people(max_weight):
    no_of_people=-1
    weight = 0
    #write your logic here. You may invoke recursive function human_pyramid() wherever applicable
    while weight <= max_weight:
        no_of_people += 2
        weight = human_pyramid(no_of_people) 
    return no_of_people - 2

#Provide different values for max_weight and test your program
max_people=find_maximum_people(1250)
print(max_people)

______

def human_tower(no_of_people):
    if (no_of_people == 1):
        return 1*(50)
    else:
        return no_of_people * (50) + human_tower(no_of_people - 2)
    
print ("total weight of human tower: ", human_tower(35))

def fun(number):
    if(number<2):
        return 1
    elif(number/2==2):
        return fun(number-1)
    else:
        return (number-1)*fun(number-1)

print(fun(7))

_____

#lex_auth_01269437504257228837
    
def find_average(mark_list):
    try:
        total=0
        for i in range(0, len(mark_list)+1):
            total += mark_list[i]
        marks_avg=total/len(mark_list)
        return marks_avg
    except TypeError:
        print("Type Error")
    except NameError:
        print("Name Error")
    except ZeroDivisionError:
        print("Zero Division Error")
    except IndexError:
        print("Index Error")

try:
    m_list=[]        
    print("Average marks:", find_average(m_list))
except ValueError:
    print("Value Error")
    
_____

balance=1000
amount="300Rs"
def take_card():
    print("Take the card out of ATM")
try:
    if balance>=int(amount):
        print("Withdraw")
    else:
        print("Invalid amount")

except TypeError:
    print("Type Error Occurred")
except ValueError:
    print("Value Error Occurred")
except:
    print("Some error Occurred")
finally:
    take_card()

    _____
    
def calculate_expenditure(list_of_expenditure):
    total=0
    try:
        for expenditure in list_of_expenditure:
            total+=expenditure
        print("Total:",total)
        avg=total/num_values
        print("Average:",avg)
    except ZeroDivisionError:
        print("Divide by Zero error")
    except TypeError:
        print("Wrong data type")
    except:
        print("Some error occured")
list_of_values=[100,200,300,"400",500]
num_values=0
calculate_expenditure(list_of_values)

_____

#calculating airport expenditure
def calculate_expenditure(list_of_expenditure):
    total=0
    try:
        for expenditure in list_of_expenditure:
            total+=expenditure
        print(total)
    except:
        print("Some error occured")
    print("Returning back from function.")

list_of_values=[100,200,300,"400",500]
calculate_expenditure(list_of_values)

____


#calculating airport expenditure
def calculate_expenditure(list_of_expenditure):
    total=0
    for expenditure in list_of_expenditure:
        if (type(expenditure) is int):
            total+=expenditure
        else:
            print("Wrong data type")
            break            
    print(total)
list_of_values=[100,200,300,"400",500]
calculate_expenditure(list_of_values)

____


#lex_auth_01269438947391897654

#Global variable
list_of_marks=(12, 18, 25, 24, 2, 5, 18, 20, 20, 21)

def find_more_than_average():
    sum = 0
    rslt_list = []
    for i in range(0,len(list_of_marks)):
        sum += list_of_marks[i]
    avrg = sum / len(list_of_marks)
    for i in range(0,len(list_of_marks)):
        if list_of_marks[i] > avrg :
            rslt_list.append(list_of_marks[i])
    return (len(rslt_list)/len(list_of_marks))*100
    #Remove pass and write your logic here

def sort_marks():
    #print([item for item in list_of_marks])
    sortlist = list([item for item in list_of_marks])
    sortlist.sort()
    #print(sortlist.sort())
    return sortlist
    #Remove pass and write your logic here

def generate_frequency():
    reslutl = []
    for i in range(0,26):
        if i in list_of_marks:
            reslutl.append(list_of_marks.count(i))
        else:
            reslutl.append(0)
        
    return reslutl

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())

______

#lex_auth_012693816779112448160

def calculate(distance,no_of_passengers):
    if (no_of_passengers * 80)-(distance/10 * 70) <= 0:
        return -1
    return (no_of_passengers * 80)-(distance/10 * 70)
    #Remove pass and write your logic here

#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))

______

#lex_auth_01269441810970214471

def check_double(number):
    #pass
    #Remove pass and write your logic here
    if len(str(number)) != len(str(number*2)):
        return False
    else:
        number1 = number*2
        check = True
        while number > 0:
            temp = number % 10
            number = number // 10
            if str(temp) not in str(number1):
                check = False
                break
        return check
        
#Provide different values for number and test your program
print(check_double(125874))

________

#lex_auth_0127382164803993601239

#This verification is based on string match.

def sum_of_numbers(list_of_num,filter_func=None):
    #pass #Remove pass and write the logic here
    if filter_func == None :
        return sum(list_of_num)
    else:
        return sum(filter_func(list_of_num))
        
def even(data):
    #pass #Remove pass and write the logic here
    filtlist = []
    for i in range(0 , len(data)):
        if (data[i]%2 == 0):
            filtlist.append(data[i])
    return filtlist

def odd(data):
    #pass #Remove pass and write the logic here
    filtlist = []
    for i in range(0 , len(data)):
        if (data[i]%2 != 0):
            filtlist.append(data[i])
    return filtlist    

sample_data = range(1,11)

print(sum_of_numbers(sample_data,odd))

_______

#lex_auth_01269438594930278448

def find_pairs_of_numbers(num_list,n):
    #Remove pass and write your logic here
    count = 0
    for i in range(0,len(num_list)):
        for j in range(0, len(num_list)):
            if i != j:
                if num_list[i] + num_list[j] == n:
                    count += 1
    if count != 0 :
        count = count // 2
    return count

num_list=[3, 4, 1, 8, 5, 9, 0, 6]
n=9
print(find_pairs_of_numbers(num_list,n))

______

#lex_auth_01269437118923571233

def factorial(number):
    #remove pass and write your logic to find and return the factorial of given number
    fact = 0
    if number == 0 : return 1
    while number > 0:
        digit = number % 10
        number = number // 10
        temp = 1
        for i in range(1,digit+1):  
            temp *= i
        fact += temp
    return fact

def find_strong_numbers(num_list):
    #remove pass and write your logic to find and return the list of strong numbers from the given list
    strong_numbers = []
    for i in num_list:
        if i == factorial(i) :
            strong_numbers.append(i)
    return strong_numbers

num_list=[145,375,0,100,2]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)

_____

def display1(flight_number, seating_capacity):
    print("Flight Number:", flight_number)
    print("Seating Capacity:", seating_capacity)

print("code-1: positional arguments")
display1("AI789",200)
#Uncomment and execute the below function call statement and observe the output
#display1(300,"BA123")


def display2(flight_number, seating_capacity):
    print("Flight Number:", flight_number)
    print("Seating Capacity:", seating_capacity)

print("-------------------------------------------------")
print("code-2: keyword arguments")
display2(seating_capacity=250, flight_number="AI789")

def display3(flight_number, flight_make="Boeing", seating_capacity=150):
    print("Flight Number:", flight_number)
    print("Flight Make:", flight_make)
    print("Seating Capacity:", seating_capacity)

print("-------------------------------------------------")
print("code-3: default arguments")
display3("AI789","Eagle")
#Uncomment and execute the below function call statements one by one and observe the output
#display3("BA234")
#display3("SI678","Qantas",200)


def display4(passenger_name, *baggage_tuple):
    print("Passenger name:",passenger_name)
    total_wt=0
    for baggage_wt in baggage_tuple:
        total_wt+=baggage_wt
    print("Total baggage weight in kg:", total_wt)

print("-------------------------------------------------")
print("code-4: variable argument count")
display4("Jack",12,8,5)
#Uncomment and execute the below function call statements one by one and observe the output
#display4("Chan",20,12)
#display4("Henry",23)

_____

def check_in(baggage,boarding_pass):
    if(baggage>=1 and baggage<=30):
            boarding_pass="Issued"

def update_seat(seat_list):
    seat_list[1]=25

boarding_pass="Not Issued"
print("boarding_pass before function call:", boarding_pass)
check_in(25, boarding_pass)
print("boarding_pass after function call:", boarding_pass)
print("boarding_pass, a string is immutable")
print("-------------------------------------------------------")

passenger_seat=["Jack","NA"]
print("passenger_seat before function call:", passenger_seat)
update_seat(passenger_seat)
print("passenger_seat after function call:", passenger_seat)
print("passenger_seat, a list is mutable")

_____

#lex_auth_0127382283825971201450

def max_frequency_word_counter(data):
    word=""
    frequency=0

    #start writing your code here
    #Populate the variables: word and frequency
    data = data.replace(',',' ')
    #print(data.split())
    uniqstr = set(data.casefold().split())
    #print(uniqstr)
    rsltstr = {}
    for str in uniqstr:
        #if str not in rsltstr.keys():
        rsltstr.update({str:data.casefold().split().count(str.casefold())})
        #rsltstr.update({str:sum(str in s for s in data.split())})
    
    maxvalues = max(rsltstr.items(), key=lambda x: x[1])   
    #print(maxvalues[0],maxvalues[1])
    listOfKeys = [key  for (key, value) in rsltstr.items() if value == maxvalues[1]]
    #print(listOfKeys)
    
    if len(listOfKeys) > 1:
        print(max(listOfKeys, key=len),maxvalues[1])
    else:
        print(maxvalues[0],maxvalues[1])
        
    #print(rsltstr)

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #print(word,frequency)


#Provide different values for data and test your program.
data="Listen to the big clock Tick tock tick"
max_frequency_word_counter(data)

_____

#lex_auth_01269444961482342489

def sms_encoding(data):
    #start writing your code here
    vowel_set = set("aeiouAEIOU")
    final_list=[]
    word=data.split()
    for i in range(0,len(word)):
        vowels = list()
        consonants = list()
        for letter in word[i]:
            if letter in vowel_set:
                vowels.append(letter)
            else:
                consonants.append(letter)
                
        if len(vowels) == len(word[i]):
            final_list.append ("".join(vowels))
        else:
            final_list.append("".join(consonants))
                
        #new_string = "".join(consonants) + "".join(vowels)
        #final_list.append(new_string)
    return ' '.join(final_list)    

data="MSD says I love cricket and tennis too"
print(sms_encoding(data))

_____

#lex_auth_012693816757551104165

def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    count=[0,0,0]
    temp = list(medical_speciality.keys())
    #print(temp)
    intx = 0
    for key in medical_speciality.keys():        
        for i in range(0,len(patient_medical_speciality_list),2):
            if (patient_medical_speciality_list[i+1] == key):
                count[intx]+=1
        intx += 1
    #speciality = medical_speciality.get(count.index(max(count))) 
    #print(max(count))
    #print(temp[count.index(max(count))])
    speciality = medical_speciality[temp[count.index(max(count))]]   
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)

______

#lex_auth_01269444890062848087

def find_correct(word_dict):
    #start writing your code here
    result_list=[0,0,0]
    for key, value in word_dict.items():
        if len(key) != len(value):
            result_list[2] += 1
            continue
        if key == value:
            result_list[0] += 1
            continue        
        crtcnt = 0
        for i in range(0,len(key)):
            if key[i] == value[i]:
                crtcnt += 1
        if (len(key) - crtcnt) <= 2:
            result_list[1] += 1
        else:
            result_list[2] += 1
    return result_list

word_dict={'COME': 'COME', 'MOST': 'MICE', 'GET': 'GOT', 'THREE': 'TRICE'}
print(find_correct(word_dict))

_____

#lex_auth_01269444195664691284
from commctrl import CBEMAXSTRLEN

def encrypt_sentence(sentence):
    #start writing your code here
    vowel_set = set("aeiouAEIOU")
    final_list=[]
    word=sentence.split()
    for i in range(0,len(word)):
        if((i%2)==0):
            final_list.append(word[i][::-1])
        else:  # do rearrangement
            vowels = list()
            consonants = list()
            for letter in word[i]:
                if letter in vowel_set:
                    vowels.append(letter)
                else:
                    consonants.append(letter)
            new_string = "".join(consonants) + "".join(vowels)
            final_list.append(new_string)
    return ' '.join(final_list)
    #return final_list

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)

_____

#lex_auth_012693825794351104168

def find_common_characters(msg1,msg2):
    #Remove pass and write your logic here
    msg11 = msg1.replace(' ','')
    msg22 = msg2.replace(' ','')
    comchar = ''
    #print(msg11.capitalize())
    for i in range(0,len(msg11)):
        if msg11[i] in comchar:
            break
        for j in range(0,len(msg22)):
            if msg11[i] == msg22[j]:
                comchar += msg11[i]
                break
                
    if comchar == '': return -1
    return comchar

#Provide different values for msg1,msg2 and test your program
msg1="moto"
msg2="moto"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)

______

import time
import datetime

#To get current GM time
print("Current GM time:",time.gmtime())
#This returns a time structure containing 9 values - year, month,day, hour, minute, sec, day of week, day of year and daylight savings.

#To get current local time
print("Current local time:",time.localtime())
#This also returns a time structure containing 9 values - year, month,day, hour, minute, sec, day of week, day of year and daylight savings.

#To extract today's date in a specified string format
print("Today's date using time module",time.strftime("%m-%m/%Y"))

#Python additionally allows use of  datetime module
#Prints today's date
print("Today's date using datetime module:", datetime.date.today())

#To extract today's date in a specified string format
print("Today's date (dd/mm/yyyy) using datetime module:", datetime.date.today().strftime("%d/%m/%Y"))


#To convert a date in string format to datetime value
print("Today's date (dd/mm/yyyy):", datetime.datetime.strptime("17/04/1","%y/%d/%m"))

_____

import random,math,time,datetime

print(len(''.join(set("BUSINESS") - set("BISINESS"))))

def my_function(x):
  return x[::-1]

mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)

x=10
y=50
print(random.randrange(x,y)+1)

x = 9.6
print(datetime.date.today().strftime("%d/%m/%y"))
print(math.ceil(x))
print(math.floor(x))
print(math.factorial(int(x)))
print(math.fabs(x))

math.comb

num1=234.01
num2=1
num3=-27.01


print("The smallest integer greater than or equal to num1,",num1,":",math.ceil(num1))
print("The largest integer smaller than or equal to num1,",num1,":",math.floor(num1))
print("The factorial of num2,",num2,":", math.factorial(num2))
print("The absolute value of num3",num3,":",math.fabs(num3)) 

______

#lex_auth_012693774187716608134

def translate(bilingual_dict,english_words_list):
    #Write your logic here
    swedish_words_list = []
    for i in range(0,len(english_words_list)):
        swedish_words_list.append(bilingual_dict.get(english_words_list[i]))
    return swedish_words_list


bilingual_dict= {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
english_words_list=["merry","christmas"]
print("The bilingual dict is:",bilingual_dict)
print("The english words are:",english_words_list)

swedish_words_list=translate(bilingual_dict, english_words_list)
print("The equivalent swedish words are:",swedish_words_list)

____

#lex_auth_01269442027919769669

#Global variables
child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates():
    total_chocolates = 0
    global chocolates_received,child_id
    #print(len(chocolates_received))
    for i in range(0,len(chocolates_received)):
        total_chocolates += int(chocolates_received[i-1])
        #print(total_chocolates)
    return total_chocolates
    #Remove pass and write your logic here to find and return the total number of chocolates

def reward_child(child_id_rewarded,extra_chocolates):    
    #Remove pass and write your logic here
    global chocolates_received,child_id
    if (child_id_rewarded in (child_id)):
        if (extra_chocolates<1):
            print("Extra chocolates is less than 1")
        else:
            #print(chocolates_received[child_id.index(child_id_rewarded)],child_id.index(child_id_rewarded))
            chocolates_received[child_id.index(child_id_rewarded)] += extra_chocolates
            #print(chocolates_received)
            print(chocolates_received)
    else:
        print("Child id is invalid")
        return 
    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print("Extra chocolates is less than 1")
    #print("Child id is invalid")
    #print(chocolates_received)


print(calculate_total_chocolates())
#Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(20,2)

___

#lex_auth_012693816331657216161

def encode(message):
    encoded_message = ""
    count = 0
    if len(message) == 1:
        encoded_message = str(1)+message[0]
    for i in range(1,len(message)):
        count += 1 
        if message[i-1] != message[i]:
            encoded_message += str(count)+message[i-1]
            count = 0       
        
        if (i==len(message)-1):   
            if message[i-1] != message[i]:
                count += 1                
                encoded_message += str(count)+message[i]
                count = 0            
            else:
                encoded_message += str(count+1)+message[i-1] 
                
    return encoded_message              
'''        if (i!=len(message)-1):
            if message[i-1] != message[i]:
                encoded_message += str(count)+message[i-1]
                count = 0
        else:
            if message[i-1] != message[i]:
                encoded_message += str(count)+message[i]
                count = 0            
            else:
                encoded_message += str(count+1)+message[i-1] 
'''

    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("M")
print(encoded_message)

____

#lex_auth_012693819159732224162

def check_palindrome(word):
    status = True
    print(len(word))
    for i in range(0,len(word)//2):
        if word[i] != word[len(word)-1-i]:
            status = False
            break
    return status        
    #Remove pass and write your logic here

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
    
    ______
    
#lex_auth_01269441913243238467

def create_largest_number(number_list):
    number_list.sort()
    number_list.reverse()    
    print (number_list)
    num =""
    for i in range(0,len(number_list)):
        num += str(number_list[i])
    return(int(num))
    #remove pass and write your logic here


number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)

____

#lex_auth_012693795044450304151

def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    #Write your logic here
    for rg in reqd_gems:
        if rg in gems_list:
            bill_amount += price_list[gems_list.index(rg)] * reqd_quantity[reqd_gems.index(rg)] 
            #print (type(price_list[gems_list.index(rg)]))
        else:
            bill_amount = -1
            break
    if bill_amount == 0: bill_amount = -1
    if bill_amount > 30000 : bill_amount = bill_amount * 0.95
        
    return bill_amount

#List of gems available in the store
gems_list=['Moonstone', 'Sapphire', 'Quartz']

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[3498, 1257, 5467]

#List of gems required by the customer
reqd_gems=['Ivory', 'Quartz']

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[5, 8]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)

_____

#lex_auth_012693797166096384149

def find_leap_years(given_year):

    # Write your logic here
    list_of_leap_years = []
    while len(list_of_leap_years) < 15:
        
        if (given_year%4 == 0):
            if (given_year%100 == 0):
                if (given_year%400 == 0):
                    list_of_leap_years.append(given_year)
            else:
                list_of_leap_years.append(given_year)
        
#        if ((given_year%4 == 0) and (given_year%100 == 0 and given_year%400 == 0)):
#            list_of_leap_years.append(given_year)
        given_year+=1
    return list_of_leap_years

list_of_leap_years=find_leap_years(2004)
print(list_of_leap_years)

___

#lex_auth_01269438070259712046

def count_names(name_list):
    count1=0
    count2=0
    
    #start writing your code here
    #Populate the variables: count1 and count2
    for name in name_list:
        if (name.endswith('at') and (len(name)==3)):
            count1+=1
        if (name.count('at')):
            count2+=1
    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    print("_at -> ",count1)
    print("%at% -> ",count2)


#Provide different names in the list and test your program
name_list=["Hat","Cat","rabbit","matter"]
count_names(name_list)

___

#lex_auth_012693763253788672132

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    num = 101
    #Write your logic here
    for i in range(0,no_of_passengers):
        ticket_number_list.append((str)(airline+':'+source[0:3]+':'+destination[0:3]+':'+str(num)))
        num+=1
    #print(ticket_number_list)
    #Use the below return statement wherever applicable
    if no_of_passengers>5:
        return ticket_number_list[len(ticket_number_list)-5:len(ticket_number_list)]
    else:
        return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("BA","Australia","France",2))

____

# lex_auth_012693813706604544157


def find_max(num1, num2):
    max_num = -1
    lst = []
    # Write your logic here
    if num1 >= num2:
        return max_num

    for i in range(num1, num2 + 1):
        if (len(str(i)) == 2) and (i % 5 == 0) and ((i % 10 + i // 10) % 3 == 0):
            lst.append(i)

    if len(lst) == 0:
        return max_num

    print(max(lst))
    return "N/A"


# Provide different values for num1 and num2 and test your program.
max_num = find_max(3, 60)
print(max_num)

___


import turtle

wn = turtle.Screen()  # creates a graphics window
wn.setup(500, 500)  # set window dimension

alex = turtle.Turtle()  # create a turtle named alex
alex.shape("turtle")  # alex looks like a turtle

"""
alex.color("black")    # alex has a color
alex.right(60)         # alex turns 60 degrees right
alex.left(60)          # alex turns 60 degrees left
alex.circle(50)        # draws a circle of radius 50
#draws circles
for counter in range(1,3):
    alex.circle(20*counter)
"""

# Write the logic to create the given pattern
# Refer the statements given above to draw the pattern

for counter in range(1, 5):
    alex.circle(20 * counter)

alex.right(120)

for counter in range(1, 5):
    alex.circle(20 * counter)

alex.right(120)

for counter in range(1, 5):
    alex.circle(20 * counter)

    _____
    
# lex_auth_012693810762121216155


def solve(heads, legs):
    error_msg = "No solution"
    chicken_count = 0
    rabbit_count = 0
    # Start writing your code here
    # Populate the variables: chicken_count and rabbit_count

    for chicken_count in range(heads + 1):
        rabbit_count = heads - chicken_count
        if (2 * chicken_count) + (4 * rabbit_count) == legs:
            print(chicken_count, rabbit_count)
            return
    print(error_msg)

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    # print(chicken_count,rabbit_count)
    # print(error_msg)


# Provide different values for heads and legs and test your program
solve(5, 10)

________

# lex_auth_012693788748742656146


def calculate_loan(
    account_number,
    salary,
    account_balance,
    loan_type,
    loan_amount_expected,
    customer_emi_expected,
):
    eligible_sal_amount = 0
    bank_emi_expected = 0
    eligible_loan_amount = 0

    # Start writing your code here
    # Populate the variables: eligible_loan_amount and bank_emi_expected

    if (len(str(account_number)) != 4) or (account_number // 1000 != 1):
        print("Invalid account number")
        return

    if account_balance < 100000:
        print("Insufficient account balance")
        return

    if loan_type == "Car":
        eligible_sal_amount = 25000
        bank_emi_expected = 36
        eligible_loan_amount = 500000
    elif loan_type == "House":
        eligible_sal_amount = 50000
        bank_emi_expected = 60
        eligible_loan_amount = 6000000
    elif loan_type == "Business":
        eligible_sal_amount = 75000
        bank_emi_expected = 84
        eligible_loan_amount = 7500000
    else:
        print("Invalid loan type or salary")
        return

    if salary > eligible_sal_amount:
        if (loan_amount_expected <= eligible_loan_amount) and (
            customer_emi_expected <= bank_emi_expected
        ):
            print("Account number:", account_number)
            print("The customer can avail the amount of Rs.", eligible_loan_amount)
            print("Eligible EMIs :", bank_emi_expected)
            print("Requested loan amount:", loan_amount_expected)
            print("Requested EMI's:", customer_emi_expected)
        else:
            print("The customer is not eligible for the loan")
    else:
        print("Invalid loan type or salary")

    # Use the below given print statements to display the output, in case of success
    # print("Account number:", account_number)
    # print("The customer can avail the amount of Rs.", eligible_loan_amount)
    # print("Eligible EMIs :", bank_emi_expected)
    # print("Requested loan amount:", loan_amount_expected)
    # print("Requested EMI's:",customer_emi_expected)

    # Use the below given print statements to display the output, in case of invalid data.
    # print("Insufficient account balance")
    # print("The customer is not eligible for the loan")
    # print("Invalid account number")
    # print("Invalid loan type or salary")
    # Also, do not modify the above print statements for verification to work


# Test your code for different values and observe the results
calculate_loan(1005, 90000, 100000, "Business", 7500000, 80)

_______

# lex_auth_012693782475948032141


def calculate_bill_amount(food_type, quantity_ordered, distance_in_kms):
    bill_amount = 0
    # write your logic here
    if (
        (food_type != "V" and food_type != "N")
        or (distance_in_kms <= 0)
        or (quantity_ordered < 1)
    ):
        return -1

    if food_type == "V":
        bill_amount = quantity_ordered * 120
    else:
        bill_amount = quantity_ordered * 150

    if distance_in_kms >= 3:
        if distance_in_kms <= 6:
            bill_amount = bill_amount + 3 * (distance_in_kms - 3)
        else:
            bill_amount = bill_amount + 3 * 3 + 6 * (distance_in_kms - 6)

    return bill_amount


# Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount = calculate_bill_amount("N", 2, 7)
print(bill_amount)

_____

# lex_auth_012693780491968512136


def make_amount(rupees_to_make, no_of_five, no_of_one):
    five_needed = 0
    one_needed = 0

    # Start writing your code here
    # Populate the variables: five_needed and one_needed

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    five_needed = rupees_to_make // 5
    one_needed = rupees_to_make % 5

    if (five_needed <= no_of_five) and (one_needed <= no_of_one):
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    else:
        print(-1)


# Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(52, 8, 5)

______

def to_f(c):
    f=c*(9/5)+32
    return int(f)

def to_c(f):
    c=(f-32)*(5/9)
    return int(c)

print(to_f(32),"F")
print(to_c(90),"C")

def calculate_sum(data1, data2):
    #All the statements in the block of code must have the same level of indentation
    result_sum=data1+data2
    return result_sum

result=calculate_sum(10,20)
print(result)

'''

import turtle
wn = turtle.Screen()        # creates a graphics window
wn.setup(540,508)           # set window dimension

alex = turtle.Turtle()      # create a turtle named alex
alex.shape("turtle")        # alex looks like a turtle
alex.color('red')           # alex has a color


alex.circle(50)              # draws a circle of radius 50
alex.forward(100)             # alex moves 50 positions forward
alex.left(90)                # alex turns 60 degrees left
alex.forward(100)             # alex moves 50 positions forward
alex.left(90)                # alex turns 60 degrees left
alex.forward(200)             # alex moves 50 positions forward
alex.left(90)                # alex turns 60 degrees left
alex.forward(100)             # alex moves 50 positions forward
alex.left(90)                # alex turns 60 degrees left
alex.forward(100)             # alex moves 50 positions forward
#alex.right(60)               # alex turns 60 degrees right
#alex.backward(50)            # alex moves 50 positions backward

'''
rev = 0
num = 78900987
temp = num

while (num !=0):
    rem = num % 10
    num = int(num / 10)
    print(rem,num)
    rev = rev * 10 + rem 
print(temp)
print(rev)
if temp == rev:
    print("palindrome")
else:
    print("not palindrome")

print("\n")

num1 = 3
num2 = 4
num3 = 2

if (num1 < num2):
    if(num1 < num3):
        print("num1 is smallest")
    else:
        print("num3 is smallest")
elif (num2<num3):
    print("num2 is smallest")
else:
    print("num3 is smallest")
      
print("________________________________________________________________________")
print("BREAD BASKET")
print("\"Looking for a healthy breakfast, this is the place for you!!\"")
print("________________________________________________________________________")
print("Raisin Toast$2.50")
print("French Toast$2.80")
print("Mushroom Toast$3.00")
print("Pancake$4.00")
print("Pancake with Ice-cream$7.50")
print("Chef's speciality$10.00")
print("__________________________________________________________________________")

radius = 5.0
area=3.14*radius*radius
print(area) 

print (int(11/2))
print (11%2)
print (11//2)

'''
import turtle # allows us to use the turtles library

wn = turtle.Screen() # creates a graphics window
wn.setup(400,400) # set window dimension

circle_rad=60 # set the radius
rectangle_width=240 #set the width
rectangle_height=30 #set the height

alex = turtle.Turtle() # create a turtle named alex
alex.shape("turtle") # alex looks like a turtle
alex.color('red') # alex has a color
alex.circle(circle_rad)
alex.backward(rectangle_width/2)
alex.forward(rectangle_width)
alex.right(90)
alex.forward(rectangle_height)
alex.right(90)
alex.forward(rectangle_width)
alex.right(90)
alex.forward(rectangle_height) '''

no_of_landings=356
no_of_takeoffs=245
initial_no_of_flights=100
current_no_of_flights=initial_no_of_flights+no_of_landings-no_of_takeoffs
print("Current number of flights:",current_no_of_flights)

print(type(3))
print(type("Hello World"))
print(type(False))
print(type(2.0))

no_of_passengers=3
ticket_number=1001
print("Ticket Numbers for all the Passengers:")
while(no_of_passengers>0):
    print("T -",ticket_number)
    ticket_number=ticket_number+1
    no_of_passengers=no_of_passengers-1

airline="AirIndia"
luggage_weight=28
AI_weight_limit=30
EM_weight_limit=35
if(airline=="AirIndia"):
    if(luggage_weight<=AI_weight_limit):
        print("Check-in cleared")
    else:
        print("Remove some luggage and come back")
elif(airline=="Emirates"):
    if(luggage_weight<=EM_weight_limit):
        print("Check in cleared")
    else:
        print("Remove some luggage and come back")
else:
    print("Invalid airline")
    
