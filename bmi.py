
# LeBron James: 6'9", 250 lbs.
# Arnold Schwarzenegger, 6'2", 235 lbs. (in season)
# Simone Biles: 4'8", 104 lbs.
# Taylor Swift: 5'10", 119 lbs.

def readHeightWeight() -> tuple[float, float]:
    height = float(input('Please enter your height in inches: '))
    weight = float(input('Please enter your weight in pounds: '))
    return height, weight

def bmi(h: float, w: float) -> float:
    return (w/h**2) * 703

def classifyBMI(bmi: float) -> str:
    result = ''
    if bmi < 18.5:
        result = 'underweight'
    elif bmi < 25:
        result = 'healthy'
    elif bmi < 30:
        result = 'overweight'
    else:
        result = 'obese'
    return result

def main(args: list[str]) -> int:
    # Read height and weight
    height, weight = readHeightWeight()
    # Find BMI
    BMI: float = bmi(height, weight)
    # Classify BMI
    print('A BMI of', BMI, 'is classed as', classifyBMI(BMI))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
