def create_roman(value):
    roman = ""
    for letters, val in (("M", 1000),
                         ("CM", 900), ("D", 500), ("CD", 400), ("C", 100),
                         ("XC", 90), ("L", 50), ("XL", 40), ("X", 10),
                         ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)):
        while value >= val:
            roman += letters
            value -= val
    return roman


units = " I II III IV V VI VII VIII IX".split(" ")
tens = " X XX XXX XL L LX LXX LXXX XC".split(" ")
hundreds = " C CC CCC CD D DC DCC DCCC CM".split(" ")
thousands = " M MM MMM".split(" ")

def solution(n):
    return thousands[n//1000] + hundreds[n%1000//100] + tens[n%100//10] + units[n%10]