# green_analysis.py

def compute_co2_efficiency(co2_reduction, investment_cost):
    try:
        return co2_reduction / (investment_cost * 1_000_000)
    except ZeroDivisionError:
        return "Cannot compute"
