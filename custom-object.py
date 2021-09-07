class Purchase(object):
    def __init__(self, amount):
        self.amount = amount
        
    def taxfind(self, taxPercent):
        return self.amount * taxPercent/100.0
    
    def tipfind(self, tipPercent):
        return self.amount * tipPercent/100.0
    
    def calculateTotal(self, taxPercent, tipPercent):
        return self.amount * (1 + taxPercent/100.0 + tipPercent/100.0)
    
purchase = Purchase(100)

taxPercent = 7.5
tipPercent = 20.0

tax = purchase.taxfind(taxPercent)
tip = purchase.tipfind(tipPercent)

print('Tax:', tax)
print('Tip:', tip)
print('Final Bill:', purchase.calculateTotal(taxPercent, tipPercent))
