#lex_auth_01269437118923571233

def factorial(number):
    #remove pass and write your logic to find and return the factorial of given number
    fact = 1
    for i in range(1,number+1):
        fact *= i
    return fact

def find_strong_numbers(num_list):
    #remove pass and write your logic to find and return the list of strong numbers from the given list
    res_list = []
    for data in num_list:
        num = data
        factvalue = 0
        while num != 0:
            factvalue += factorial(num % 10)
            num = int(num / 10)
        
        if data == factvalue:
            res_list.append(data)
    return res_list


num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
