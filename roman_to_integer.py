roman_to_int = {"I":1, "V": 5, "X": 10, "L": 50, "C" :100, "D": 500, "M":1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
sum = 0
s = "MMMCDXC" ##Sample string you want to convert to roman
count = len(s)

if count < 1 or count > 15:
    print("length of string should be greater than 1 and less than 15")
    sys.exit(1)
else:
    while count > 0:
        if count != 1:
            if s[count-1] in roman_to_int:
                if (s[count-2]+s[count-1]) in roman_to_int:
                    #print("if: {} - {}".format(s[count-2]+s[count-1], roman_to_int[s[count-2]+s[count-1]])) ##Added for debugging
                    print("if: {} - {}".format(s[count-2]+s[count-1], roman_to_int[s[count-2]+s[count-1]]))
                    sum = sum + roman_to_int[s[count-2]+s[count-1]]
                    count = count - 2
                else:
                    #print("else: {} - {}".format(s[count-1], roman_to_int[s[count-1]])) ##Added for debugging
                    print("else: {} - {}".format(s[count-1], roman_to_int[s[count-1]]))
                    sum = sum + roman_to_int[s[count-1]]
                    count = count - 1
        else:
            #print("else: {} - {}".format(s[count-1], roman_to_int[s[count-1]])) ##Added for debugging
            print("else: {} - {}".format(s[count-1], roman_to_int[s[count-1]]))
            sum = sum + roman_to_int[s[count-1]]
            count = count - 1

print("Integer of {} ==> {}".format(s, sum))
