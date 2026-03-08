def score(impact:int, effort:int, risk:int)->float:
    # Higher impact/risk and lower effort => higher priority
    return round((impact*0.45 + risk*0.35 + max(1,10-effort)*0.20),2)
