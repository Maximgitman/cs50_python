def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Replace the leading $ from the input
    dollars = d.replace("$", "")

    # Convert string format into float and round 
    float_dollars = round(float(dollars), 1)

    return float_dollars


def percent_to_float(p):
    """
    percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), 
    remove the trailing %, and return the percentage as a float. For instance, given 15% as input, 
    it should return 0.15.
    """
    # Replace the trailing % from the input
    percentage = p.replace("%", "")

    # Convert to float
    float_percent = round(float(percentage), 1) / 100

    return float_percent

main()