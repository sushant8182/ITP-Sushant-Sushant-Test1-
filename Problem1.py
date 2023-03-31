
n1=0
tax=0
print(("Melanie Dental Clinic").center(100))
p_name=input(("Enter Patient's name: "))
clean=input("Was Cleaning performed? (Y/N):")
cavi=input("Was Cavity filling performed? (Y/N)")
x_ray=input("Was the X-Ray performed? (Y/N): ")

if clean=="Y":
  n1+=60
if cavi=="Y":
  n1+=200
if x_ray=="Y":
  n1+=100
  
if n1>300:
  n1=n1-n1*(0.10)

elif n1>200:
  n1=n1-n1*(0.5)


else:
  pass

output=n1*0.15
print("\n")
print("Melanie Dental Clinic")
print("Receipt for Patient name: ",p_name)   
print("-"*100) 
print("Subtotal without Tax: ",n1)
print("Tax: ",output)
print("   Total:",n1+output)
