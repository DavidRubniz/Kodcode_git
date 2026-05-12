#1
def is_even(n: int) -> bool:
    return n%2==0

#2
def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

#3
def count_vowels(s: str) -> int:
    counter3 = 0
    for i in s:
        if i in 'aeuiw':
            counter3 += 1
    return counter3

#4
def reverse_string(s: str) -> str:
    new_string4 = ''
    for i in reversed(s):
        new_string4 += i
    return new_string4

#5
def find_max(lst: list) -> int:
    max5 = 0
    for i in lst:
        if i > max5:
            max5 = i
    return max5

#6
def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9/5) + 32

#7
def is_palindrome(s: str) -> bool:
    return reversed(s) == s

#8
def list_of_even(lst: list) -> list:
    new_list8 = []
    for i in lst:
        if i % 2 == 0:
            new_list8.append(i)
    return new_list8

#9
def is_anagrams(s1: str, s2: str) -> bool:
    new_s1 = s1.replace(' ', '').lower()
    new_s2 = s2.replace(' ', '').lower()
    return sorted(new_s1) == sorted(new_s2)

#10
def words_count(snt: str) -> dict:
    dict10 = {}
    splited10 = snt.split(' ')
    for i in splited10:
        dict10[i] = splited10.count(i)
    return dict10

#11
def calculate_resource_drain(cost: float, waste_factor: float) -> float:
    return cost * waste_factor

def get_net_resources(cost: float, waste_factor: float) -> float:
    return cost - calculate_resource_drain(cost, waste_factor)

#12
def intercept_length(packet: str) -> int:
    return len(packet.encode())

def verify_transmission(packet: str) -> None:
    print(f'Intercepted packet contains {intercept_length(packet)} bytes of data')

#13
import math
def convert_to_decibels(signal_strength: float) -> float:
    return 20 * math.log10(signal_strength / 1)

def is_threat_detected(signal_strength: float) -> bool:
    return convert_to_decibels(signal_strength) > 90

#14
def get_fuel_surcharge(distance: float) -> float:
    return (((distance/10) * 8) / 100) * 17

def get_hazard_pay(distance: float) -> float:
    return distance * 0.05

def calculate_mission_cost(distance: float) -> float:
    return distance / 10 * 8 + get_fuel_surcharge(distance) + get_hazard_pay(distance)

