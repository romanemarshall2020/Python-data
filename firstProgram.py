# guess = int(input("When was Python 1,0 released"))

# correct_answer = 1994

# if guess < correct_answer:
#     print("It was later than that")
#     input("when was Python 1.0 released: ")

# elif guess > correct_answer:
#      print("It was earlier than that")
#      input("when was Python 1.0 released: ")

# else:
#      print("Correct")
     


spending = [1346.0, 987.50, 1734.40,25670.0, 3271.45, 2500.0, 2130.0, 2510.30, 3400.0, 2586.7, 3961.22, 1000.0]
lower = 0
higher = 0
normal = 0
for i in spending:
    if i < 1000:
        lower += 1
        # print("the amonut of lower spending was: ", lower)
    elif i <= 2500:
        normal += 1
        # print("the amonut of normal spending was: ", normal)
    else:
        higher += 1
        # print("the amonut of higher spending was: ", higher)

print("numbers of months with low spending: " + str(lower) + ", normal spending: " + str(normal) + ", high spending: " + str(higher) + ".")

  