
stock_prices = {
    "AAPL": 180.50,
    "TSLA": 250.00,
    "GOOGL": 140.25,
    "MSFT": 400.10,
    "AMZN": 175.30
}

def run_stock_tracker():
    print("===================================")
    print("     Stock Portfolio Tracker       ")
    print("===================================")
    print("Available stocks and prices:")
    for stock, price in stock_prices.items():
        print(f" - {stock}: ${price}")
    print("-----------------------------------")
    
    portfolio = {}
    total_investment = 0.0

  
    while True:
        stock_name = input("Enter stock name (or type 'done' to finish): ").upper()
        
        if stock_name == 'DONE':
            break
            
       
        if stock_name not in stock_prices:
            print("Sorry, that stock is not in our system. Please try again.\n")
            continue
            
        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            if quantity <= 0:
                print("Quantity must be greater than 0.\n")
                continue
        except ValueError:
            print("Invalid quantity. Please enter a whole number.\n")
            continue

        
        price = stock_prices[stock_name]
        cost = price * quantity
        total_investment += cost
        
        
        if stock_name in portfolio:
            portfolio[stock_name] += quantity
        else:
            portfolio[stock_name] = quantity
            
        print(f"Added {quantity} shares of {stock_name} (${cost:.2f})\n")

    
    if not portfolio:
        print("\nYou didn't buy any stocks. Goodbye!")
        return

    print("\n===================================")
    print("         Portfolio Summary         ")
    print("===================================")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares @ ${stock_prices[stock]:.2f}")
    
    print("-----------------------------------")
    print(f"TOTAL INVESTMENT: ${total_investment:.2f}")
    print("===================================")

    
    save_choice = input("Do you want to save this report to a file? (y/n): ").lower()
    
    if save_choice == 'y':
        filename = "portfolio_report.txt"
        with open(filename, "w") as file:
            file.write("Stock Portfolio Report\n")
            file.write("======================\n")
            for stock, qty in portfolio.items():
                file.write(f"{stock}: {qty} shares @ ${stock_prices[stock]:.2f}\n")
            file.write("----------------------\n")
            file.write(f"TOTAL INVESTMENT: ${total_investment:.2f}\n")
        print(f"\nReport successfully saved to '{filename}' in your current folder!")


if __name__ == "__main__":
    run_stock_tracker()