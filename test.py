import unittest
from billing_system import Item, Receipt


class TestBillingSystem(unittest.TestCase):

    def test_item_subtotal(self):
        """Test that the subtotal for an item is calculated correctly.""" 
        item = Item("Apple", 1.00, 5)
        self.assertEqual(item.subtotal(), 5.00)

    def test_receipt_calculation(self):
        """Test the receipt's total calculation without discount."""
        receipt = Receipt()  
        receipt.add_item(Item("Apple", 1.00, 5))
        receipt.add_item(Item("Banana", 0.50, 10))
        receipt.add_item(Item("Orange", 0.75, 4))
        
        subtotal, tax, total = receipt.calculate_totals()
        
        # Check calculations
        self.assertEqual(subtotal, 13.00)
        self.assertEqual(tax, 1.30)     # 10% of 13.00
        self.assertEqual(total, 14.30)  # Total including tax


    def test_receipt_with_discount(self):
        """Test the receipt's total calculation with discount applied."""
        receipt = Receipt()
        receipt.add_item(Item("Apple", 1.00, 5))
        receipt.discount = 1.00     # Apply a $1 discount
        
        subtotal, tax, total = receipt.calculate_totals()

        # Check calculations
        self.assertEqual(subtotal, 5.00)
        self.assertEqual(tax, 0.50)     # 10% of 5.00
        self.assertEqual(total, 4.50)   # Total after discount

    def test_receipt_with_multiple_items_and_discount(self):
        """Test the receipt's total calculation with multiple items and discount."""
        receipt = Receipt()
        receipt.add_item(Item("Apple", 1.00, 5))     # 5.00
        receipt.add_item(Item("Banana", 0.50, 10))   # 5.00
        receipt.add_item(Item("Orange", 0.75, 4))    # 3.00
        receipt.discount = 2.00                      # Apply a $2 discount
        
        subtotal, tax, total = receipt.calculate_totals()

        # Check calculations
        self.assertEqual(subtotal, 13.00)
        self.assertEqual(tax, 1.30)  # 10% of 13.00
        self.assertEqual(total, 12.30) # Total after discount


    def test_receipt_generation(self):
        """Test the receipt generation output."""
        receipt = Receipt()
        receipt.add_item(Item("Apple", 1.00, 5))
        receipt.add_item(Item("Banana", 0.50, 10))
        receipt.discount = 1.00

        expected_output = (
            "Receipt\n" +
            "=" * 40 + "\n" +
            "Apple: $1.00 x 5 = $5.00\n" +
            "Banana: $0.50 x 10 = $5.00\n" +
            "=" * 40 + "\n" +
            "Subtotal: $10.00\n" +
            "Tax (10%): $1.00\n" +
            "Discount: -$1.00\n" +
            "Total: $10.00\n"
        )

        self.assertEqual(receipt.generate_receipt().strip(), expected_output.strip())


if __name__ == '__main__':
    unittest.main()


