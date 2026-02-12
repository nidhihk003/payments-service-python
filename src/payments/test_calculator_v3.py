# Test generation failed: LLM output for src/payments/calculator.py is not valid JSON. Response: [
  {
    "name": "calculate_payment_fee_zero_amount",
    "input": "calculate_payment_fee(0.0)",
    "expected": 0.0
  },
  {
    "name": "calculate_payment_fee_small_positive_amount",
    "input": "...