#r = open("employee-list", "r") # read the file
#w = open("employee-list", "w") # over write the file
#r+ = open("employee-list", "r+") # Read and Write
#a = open("employee-list", "a") # append the file

employee_file = open("employee-list", "w")
print(employee_file.readable())

employee_file.close()
employ = open("employee-list", "r")
print(employ.readable())
print(employ.read())


employ.close()

employe = open("employee-list", "r")
print(employe.read())
print(employe.readlines())
print(employe.readline())# its gonna read the first line
print(employe.readline())# its gonna read second line, like wise
print(employe.readline()[5]) #its gonna read the 5th line

for employy in employe.readlines():
    print(employy)
employe.close()
emmployee_file = open("employee-list")
emmployee_file.write("toby - Human")
emmployee_file.close()


