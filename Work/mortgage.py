# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0; 


while principal > 0:
	if month < 12: 
		principal = principal + 1000 + (principal  * rate/12) - payment
    	
   

	else:
		principal = principal + (principal  * rate/12) - payment
	total_paid = total_paid + payment   
	month = month + 1	 





print('Total paid', total_paid)

print("months taken", month)



