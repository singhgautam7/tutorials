def divide(numerator, denominator):
    if denominator == 0:
        return float('-inf')
    return int(numerator/denominator)

if __name__ == '__main__':
    print(divide(4,0))
