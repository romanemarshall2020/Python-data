def show_balance(balance):
  print("****************")
  print(f"Available balance:  + ${balance:.2f}")
  print("****************")
def deposit():
  amount = float(input("How much would you like to deposit?: "))
 
  if amount < 0:
    print("That is not a valid amount")
    return 0
  else:
    return amount

def withdraw(balance):
  print("****************")
  amount = float(input("Enter amount to withdraw: "))
  print("****************")

  if amount > balance:
    print("****************")
    print("insufficient funds")
    print("****************")
    return 0
  elif amount < 0:
    print("Amount must be greater than 0")
    return 0
  else:
    return amount
    
def main():
  balance = 0
  is_running = True
  
  while is_running:
    print("****************")
    print("Banking program")
    print("****************")
    
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    print("****************")
  
  
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
      show_balance(balance)
    elif choice == '2':
      balance += deposit()
    elif choice == '3':
      balance -= withdraw(balance)
    elif choice == '4':
      is_running = False
    else:
      print("That is not a valid choice")
  
  
  print("Thank you! have a nice day!")

if __name__ == '__main__':
  main()