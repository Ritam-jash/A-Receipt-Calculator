import os


class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def subtotal(self):
        return self.price * self.quantity
    


class Receipt:  
    def __init__(self):
        self.items = []
        self.tax_rate = 0.1  # Example tax rate 10%
        self.discount = 0      # Example discount (flat amount) 

    def add_item(self, item):
        self.items.append(item)

    def calculate_totals(self):
        subtotal = sum(item.subtotal() for item in self.items)
        tax = subtotal * self.tax_rate
        total = subtotal + tax - self.discount
        return subtotal, tax, total

    def generate_receipt(self):
        subtotal, tax, total = self.calculate_totals()
        receipt_lines = []
        receipt_lines.append("Receipt")
        receipt_lines.append("=" * 40)
        for item in self.items:
            receipt_lines.append(f"{item.name}: ${item.price:.2f} x {item.quantity} = ${item.subtotal():.2f}")
        
        receipt_lines.append("=" * 40)
        receipt_lines.append(f"Subtotal: ${subtotal:.2f}")
        receipt_lines.append(f"Tax (10%): ${tax:.2f}")
        receipt_lines.append(f"Discount: -${self.discount:.2f}")
        receipt_lines.append(f"Total: ${total:.2f}")
        return "\n".join(receipt_lines)

    def save_receipt(self, filename="receipt.txt"):
        with open(filename, 'w') as file:
            file.write(self.generate_receipt())
        print(f"Receipt saved as {filename}")
        


def main():
    receipt = Receipt()
    while True:
        name = input("Enter item name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        try:
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: ")) 
            item = Item(name, price, quantity)
            receipt.add_item(item)
        except ValueError:
            print("Invalid input. Please enter numeric values for price and quantity.")

    # Optional: Set discount (we may modify it based on our needs)
    receipt.discount = float(input("Enter discount amount (if any, else enter 0): "))
    
    # Generate and display receipt
    print("\n" + receipt.generate_receipt())
    
    # Save receipt to a file
    save_option = input("Would you like to save the receipt? (y/n): ")
    if save_option.lower() == 'y':
        filename = input("Enter filename to save the receipt (default is 'receipt.txt'): ") or "receipt.txt"
        receipt.save_receipt(filename)


if __name__ == "__main__":
    main()


