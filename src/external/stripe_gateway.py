import os

def charge_with_stripe(token: str, amount: float):
    api_key = os.getenv("STRIPE_API_KEY")
    if not api_key:
        raise RuntimeError("Missing STRIPE_API_KEY")

    # External side-effect
    return True
