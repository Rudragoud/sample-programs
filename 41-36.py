cal_op = {"1":"Addition","2":"Substraction","3":"Multiplication","4":"Devision"}

print(cal_op)

operation = input("Enter Operation index: ")
num1 =  int( input("Enter First Number:"))
num2 =  int( input("Enter Second Number:"))

switcher={
	"Addition": (num1 + num2),
	"Substraction": (num1 - num2),
	"Multiplication": (num1 * num2),
    "Devision": (num1 / num2),
}

print(switcher.get(cal_op[operation],"In-valid operation"))
