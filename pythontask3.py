############# program1: Odd and Even function ############
list1 = [10, 501, 22, 37, 100,999,87,351]
listOdd = []
listEven = []
for i in list1:
    if i % 2 == 0:
        listEven.append(i)
    else:
        listOdd.append(i)
print("list1:    ", list1)
print("listEven: ", listEven)
print("listOdd:  ", listOdd)

######    program 2: Prime number ##############

def prime(n):
    if n <= 0:
        return "Not defined"
    elif n == 1:
        return "Not prime"
    for i in range(2, n):
        if n % i == 0:
            return "not prime"
    return "prime"


def list_prime(list):
    prime_list = []
    for i in list:
        x = prime(i)
        if x == "prime":
            prime_list.append(i)
    return prime_list


print(list_prime([10, 501, 22, 37, 100,999,87,351]))


################ Program 3: Happy numbers ###############

list1 = [10, 501, 22, 37, 100,999,87,351]
list2 = []
def is_happy(list1):
    for i in range (len(list1)):
        sum = list1[i]
        while sum!=1 and sum !=4:
            tempsum = 0
            for digit in str(sum):
                tempsum += int(digit) ** 2
            sum = tempsum
        if sum == 1:
            list2.append(list1[i])
    return list2
print(is_happy(list1))

###########    Program 4: Sum of first and last digit of an integer#################

number = 12345678
number = str(number)
first_digit_number= int(number[0])
last_digit_number= int(number[-1])
addition = first_digit_number + last_digit_number
print("Addition of first and last digit of the number is", addition)

############# Program6: Duplicates in three given list ##############

def IntersecOfSets(list1, list2, list3):
    result = []
    for i in list1:
        if i in list2 and i in list3:
            result.append(i)
    print(list(set(result)))
list1 = [10, 501, 22, 37, 100,999,87,351]
list2 = [10,501,22,37,100]
list3 = [ 10,999,501,22,37,100]
common = IntersecOfSets(list1, list2, list3)


########## Program7: First non-repeating element in a list #############

def first_non_repeated_el(list1):
    dict = {}
    for i in list1:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for i in list1:
        if dict[i] == 1:
            return i
numbers =  [1, 2, 1, 3, 3, 4, 5, 6, 7, 8]
print("Original list:")
print(numbers)
result = first_non_repeated_el(numbers)
print("First non-repeated element in list is:")
print(result)

################### Program8: Minium element in the sorted list #############3

list = [10, 501, 22, 37, 100,999,87,351]
smallest = list[0]
for value in list:
    if value < smallest:
        smallest = value
print("The minimum element in the list is " + str (smallest))

############## Program9: Triplet and its sum is equal to the given value ###########

def find3Numbers(list, arr_size, sum):
    for i in range(0, arr_size - 2):
        for j in range(i + 1, arr_size - 1):
            for k in range(j + 1, arr_size):
                if list[i] + list[j] + list[k] == sum:
                    print("Triplet is", list[i],
                          ", ", list[j], ", ", list[k])
                    return True
    return False
list = [10,20,30,9]
sum = 59
arr_size = len(list)
find3Numbers(list, arr_size, sum)

############# Program 10: Sublist with sum equal to zero ###########3


def subArrayExists(list, number):
    for i in range(number):
        sum = list[i]
        if sum == 0:
            return True
        for j in range(i + 1, number):
            sum += list[j]
            if sum == 0:
                return True
    return False
if __name__ == "__main__":
    list = [4,2,-3,1,6]
    number = len(list)
    if subArrayExists(list, number):
        print("Found a subarray with 0 sum")
    else:
        print("No Such Sub Array Exists!")


################# Program 5##################

def binomial_coefficient(n, m):
    res = 1

    if m > n - m:
        m = n - m

    for i in range(0, m):
        res *= (n - i)
        res /= (i + 1)

    return res
def calculate_ways(m, n):
    if m < n:
        return 0
    ways = binomial_coefficient(n + m - 1, n - 1)
    return int(ways)

if __name__ == '__main__':
    m = 7; n = 5
    result = calculate_ways(m, n)
    print(result)
m = int(input())
n = int(input())
print(calc_ways(m, n))







