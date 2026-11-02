class StockLookup:
    """A tool that looks up product inventory."""

    def __init__(self, products):
        self.products = products

    def find_product(self, text):
        text = text.lower()

        for product in self.products:
            if product.lower() in text:
                return product

        return None

    def count_for(self, product):
        if product in self.products:
            return self.products[product]

        return None
