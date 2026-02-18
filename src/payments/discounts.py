def apply_discount(amount: float, percentage: float) -> float:
    if percentage < 0 or percentage > 100:
        raise ValueError("Invalid discount")
    return amount * (1 - percentage / 100)
