# Condition mapping based on platform rules
def map_condition(condition):
    mapping = {
        "Like New": {
            "X": "New",
            "Y": "3 Stars (Excellent)",
            "Z": "New"
        },
        "Good": {
            "X": "Good",
            "Y": "2 Stars (Good)",
            "Z": "Good"
        },
        "Fair": {
            "X": "Scrap",
            "Y": "1 Star (Usable)",
            "Z": "As New"
        }
    }

    return mapping.get(condition, {
        "X": "Unknown",
        "Y": "Unknown",
        "Z": "Unknown"
    })


# Price after subtracting platform-specific fee
def calculate_price_after_fee(price, platform):
    if platform == "X":
        return price * 0.90  # 10% fee
    elif platform == "Y":
        return (price * 0.92) - 2  # 8% + ₹2
    elif platform == "Z":
        return price * 0.88  # 12% fee
    else:
        return price  # default case


# Check if selling on platform gives profit
def is_profitable(price, platform):
    profit_margin = 500  
    after_fee_price = calculate_price_after_fee(price, platform)
    profit = price - (price - after_fee_price)
    return profit >= profit_margin


# Get phones ready to list (only if stock is available and not sold)
def get_listable_phones(phone_list):
    result = []

    for phone in phone_list:
        if phone["stock"] == 0 or phone["sold"]:
            continue  # skip this phone

        phone_info = {
            "model": phone["model"],
            "condition": phone["condition"],
            "base_price": phone["base_price"],
            "platforms": []
        }

        for platform in ["X", "Y", "Z"]:
            mapped = map_condition(phone["condition"])[platform]
            final_price = round(calculate_price_after_fee(phone["base_price"], platform), 2)
            profitable = is_profitable(phone["base_price"], platform)

            if profitable:
                status = "Listed"
            else:
                status = "Not Listed (Low Profit)"

            phone_info["platforms"].append({
                "platform": platform,
                "mapped_condition": mapped,
                "final_price": final_price,
                "status": status
            })

        result.append(phone_info)

    return result