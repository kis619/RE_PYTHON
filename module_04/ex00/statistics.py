def get_mean(nums):
    """
    return the mean of a list of numbers
    """
    length = len(nums)
    if length == 0:
        return 0

    return sum(nums) / length


def get_median(nums):
    """
    return the median of a list of numbers
    """
    length = len(nums)

    if not length:
        return 0

    sorted_list = sorted(nums)
    median = 0
    if length % 2 == 0:
        num1 = sorted_list[int(length / 2) - 1]
        num2 = sorted_list[length // 2]
        median = get_mean((num1, num2))
    else:
        median = sorted_list[length // 2]

    return median


def get_quartile_25_75(nums: tuple):
    """
    return the quartile 25 and 75 of a list of numbers
    """
    sorted_nums = sorted(nums)
    length = len(sorted_nums)
    if length % 2 == 1:
        median_idx = length // 2
        h1 = sorted_nums[:median_idx + 1]
        h2 = sorted_nums[median_idx:]
        if len(h1[1:-1]) % 2 == 0:
            return [get_median(h1), get_median(h2)]
        return [sorted_nums[length // 4], sorted_nums[length // 4 * 3]]

    rank_25 = .25 * (length - 1)
    rank_75 = .75 * (length - 1)
    return [sorted_nums[round(rank_25)], sorted_nums[round(rank_75)]]


def get_standard_deviation(nums: tuple):
    """
    The standard deviation is the square root of the variance.
    """
    return get_variance(nums) ** .5


def get_variance(nums: tuple):
    """
    The variance is the average of the squared distances from the mean.
    Step 1: Find the mean.
    Step 2: For each data point, find the square of its distance to the mean.
    Step 3: Sum the values from Step 2.
    Step 4: Divide by the number of data points.
    """
    mean = get_mean(nums)
    sum_of_distances = sum([(num - mean) ** 2 for num in nums])
    divided_by_num_of_data_points = sum_of_distances / len(nums)
    return divided_by_num_of_data_points


acceptable_answers = {
    'mean': get_mean,
    'median': get_median,
    'quartile': get_quartile_25_75,
    'std': get_standard_deviation,
    'var': get_variance,
}


def are_all_numeric(arr):
    """
    Check if all elements in arr are numeric
    """
    for element in arr:
        if not isinstance(element, (int, float)):
            raise TypeError("ft_statistics: All arguments must be numeric")
    return True


def ft_statistics(*args, **kwargs):
    """
    ft_statistics prints the mean, median, quartile,
    standard deviation and variance of a list of numbers
    Args:
        *args: a list of numbers
        **kwargs: a list of strings
    """
    try:
        are_all_numeric(args)
    except TypeError as e:
        print(e)
        return

    if not isinstance(args, tuple):
        print("get_median: The argument passed to get_mean must be a tuple")
        return
    for val in kwargs.values():
        func = acceptable_answers.get(val, "No such function")
        if func == "No such function":
            continue
        elif not args:
            print("ERROR")
        else:
            print(f"{val} : {func(args)}")


def main():
    ft_statistics(1, 2, 4, 5, 6, 7, 36, toto="mean",
                  tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == '__main__':
    main()
