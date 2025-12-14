# Comment

"Nice! Good comments explain why a particular line of code is doing what it's doing; it's typically not beneficial to comment what code is doing."


Descriptive comments are helpful for understanding complex logic or decisions made in the code. However, avoid redundant comments that simply restate what the code does, as they can clutter the codebase and reduce readability.


```python
# Good comment explaining the purpose of the function
def calculate_discount(price, discount_rate):
    return price * (1 - discount_rate)
# Bad comment that restates what the code does
def calculate_discount(price, discount_rate):
    # This function calculates the discount
    return price * (1 - discount_rate)
```

Descriptive naming conventions for variables and functions can often eliminate the need for comments altogether. Choose clear and meaningful names that convey the purpose of the code.

```python
# Clear and descriptive naming
def calculate_total_price(item_price, tax_rate):
    return item_price + (item_price * tax_rate)
```