# Tip Calculator

print("Welcome to the Tip Calculator!")
bill = float(input("What is the Total Bill? : $"))
tip = int(input("How Much Tip Would You Like to Give? 10%, 12% or 15% : "))
num_persons = int(input("How Many People to Split the Bill : "))
bill_w_tip = tip/100 * bill + bill
bill_p_person = bill_w_tip / num_persons
final_amount = round(bill_p_person, 2)
print(f"Each Person Should Pay : ${final_amount}")