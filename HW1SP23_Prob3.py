# region imports
import random as rnd


# endregion

# region functions
def between(num, low, high, inclusivelow=True, inclusivehigh=True):
    """
    Returns a boolean indicating if num is within the given range.
    """
    if inclusivelow and inclusivehigh:
        return low <= num <= high
    elif inclusivelow:
        return low <= num < high
    elif inclusivehigh:
        return low < num <= high
    else:
        return low < num < high


def main():
    """
    Generates an array of numbers from a normally distributed population and checks their distribution.
    """
    N = 10000  # Size of array
    mean = 0  # Mean value
    stdev = 1  # Standard deviation

    arr = [rnd.gauss(mean, stdev) for _ in range(N)]

    bin1low, bin1high = mean - stdev, mean + stdev
    bin2low, bin2high = mean - 2 * stdev, mean + 2 * stdev
    bin3low, bin3high = mean - 3 * stdev, mean + 3 * stdev

    bin1 = sum(1 for num in arr if between(num, bin1low, bin1high))
    bin2 = sum(1 for num in arr if between(num, bin2low, bin2high))
    bin3 = sum(1 for num in arr if between(num, bin3low, bin3high))

    print("{:.1f}% of data within +/-1 StDev of mean.".format(100 * bin1 / N))
    print("{:.1f}% of data within +/-2 StDev of mean.".format(100 * bin2 / N))
    print("{:.1f}% of data within +/-3 StDev of mean.".format(100 * bin3 / N))


# endregion

if __name__ == "__main__":
    main()
