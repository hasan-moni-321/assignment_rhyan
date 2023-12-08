# checking is palendrome or not 
def isPalindrome(s):
    return s == s[::-1]

# traversing each string and finding square of each string 
def find_max_difference_in_power(l):
    squares = []
    for s in l:
        palindrome_ = isPalindrome(s)  
        if palindrome_:
            square_string = len(s) // 2 + 5
        else: 
            square_string = len(s) // 2 + 1
        squares.append(square_string) 

    # sorting squares list and finding minimum and maximum number 
    squares.sort()    
    squares_min = squares[0]
    squares_max = squares[-1]   
    # returning maximum difference 
    return squares_max - squares_min


# input total number of string 
total_string = int(input("Enter total number of string: "))
string_list = []

# input string and keep in string_list 
for i in range(0, total_string): 
    str = input()
    string_list.append(str) 


print("Inputed strings are: ", string_list) 
max_difference = find_max_difference_in_power(string_list)
print("maximum difference is: ", max_difference) 
