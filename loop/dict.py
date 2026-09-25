users=[
    {"name":"Alice", "total":120, "coupon":"DISCOUNT10"},
    {"name":"Bob", "total":200, "coupon":"DISCOUNT20"   },
    {"name":"Charlie", "total":150, "coupon":"DISCOUNT15"}
]

discount_codes = {
    "DISCOUNT10": (0.10,10),
    "DISCOUNT15": (0.15,20),
    "DISCOUNT20": (0.50,0)
}

for user in users:
    discount_percentage, discount_amount = discount_codes.get(user["coupon"],(0,0))
    discounted_total = user["total"] * discount_percentage - discount_amount
    print(f"{user['name']} has a total of {user['total']}, with coupon {user['coupon']} applied, the discounted total is: {discounted_total}")
