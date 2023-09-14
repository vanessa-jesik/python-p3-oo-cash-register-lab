#!/usr/bin/env python3
class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        
    def add_item(self, title, price, quantity = 1):
        self.total = self.total + (price * quantity)
        self.last_transaction = price * quantity
        for q in range(quantity):
            self.items.append(title)
        
    def apply_discount(self):
        if self.discount:
            self.total = self.total - (self.total * self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")
            
    def void_last_transaction(self):
        self.total = self.total - self.last_transaction
        