def simple_interest(principal,rate,time):
    interest = (principal*rate*time)/100
    amount = principal + interest
    return amount
def compound_interest(principal,rate,time,period):
    amount = principal * (1+ (rate/period)) ** (period * time)
    return amount
def annunity_plan(pmt,rate,time,period):
    amount = pmt * ((((1 + (rate/period))) ** (period * time) - 1)) / (rate/period)
    return amount
def main():
    while True:
        print("Please choose a financial plan to calculate")
        print("1. Simple Interest")
        print("2. Compund Interst")
        print("3. Annuity Plan")
        print("4. None")
        
        
        choice = int(input("Enter choice (1/2/3/4): "))
        
        if choice == 1:
            
            p = float(input("Enter principal amount:"))
            r = float(input(" Enter interest rate(as a deciaml):"))
            t = float(input(" Enter time period (in years):"))
            result = simple_interest(p,r,t)
            print("Your amount totals to:", result )
        elif choice == 2:
            p = float(input("Enter principal amount:"))
            r = float(input(" Enter interest rate(as a deciaml):"))
            t = float(input(" Enter time period (in years):"))
            n = int(input(" Enter period:"))
            result = compound_interest(p,r,t,n)
            print("Your amount totals to:", result)
        elif choice == 3:
            pmt = float(input("Enter yout total payment:"))
            r = float(input(" Enter interest rate(as a deciaml):"))
            t = float(input(" Enter time period (in years):"))
            n = int(input(" Enter period:"))
            result = annunity_plan(pmt,r,t,n)
            print("Your total amount is", result)
        elif choice == 4:
            print("Exiting the program. Thank you and Goodbye <3")
            break
        else:
            print("Invalid input.Please enter the following values 1,2,3,4")
if __name__ == "__main__":
    main()
            
    
                

            

            
            
            
    
        
        
    

    