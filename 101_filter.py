#!/usr/bin/env python3
# File: 101_filter.py
# Usage:

fellowship = ["gibberish","indecent","adolecense", "adult"]
print("Before:")
print(fellowship)
result = filter(lambda member: len(member) > 6, fellowship)
print("After apply filter:")
print(list(result))
