# functions.py

def calculate_savings(current_age, retirement_age, current_savings, annual_savings, annual_return):
    years_to_retirement = retirement_age - current_age
    future_value = current_savings
    for _ in range(years_to_retirement):
        future_value = future_value * (1 + annual_return / 100) + annual_savings
    return future_value

def calculate_adjustment(target_savings, estimated_savings, years_to_retirement, annual_return):
    shortfall = target_savings - estimated_savings
    if shortfall > 0:
        adjusted_savings = (shortfall / ((1 + annual_return / 100)**years_to_retirement - 1)) / annual_return
        suggestion = f"Increase annual savings by ${adjusted_savings:,.2f}"
    else:
        suggestion = "You are on track or ahead of schedule. 👍"
    return shortfall, suggestion
