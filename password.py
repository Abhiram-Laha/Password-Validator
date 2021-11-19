""" Password Validator  """
#by Abhiram Laha

print("------PASSWORD VALIDATOR-----\n")
password = input("Enter your Password : ");
print()

sym = ('@',"#","$","*","!","~","&")

count_digit=0;
count_spec=0;
cout_upper=0;
lent=len(password)

if lent < 4:
    print("WEAK PASSWORD")
    
for i in password:
    if i.isdigit():
        count_digit+=1;
    if i in sym:
        count_spec+=1;
    if i.isupper():
        cout_upper+=1;
        

if (count_digit>2 and count_spec>0 and cout_upper>0):
    print("STRONG PASSWORD")
    

        
