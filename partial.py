from functools import partial

def calculate_price(base_price, tax_rate):
    return base_price * (1 + tax_rate)

price_with_gst = partial(calculate_price, tax_rate = 0.18)



print(price_with_gst(1000))
print(price_with_gst(500))