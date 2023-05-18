def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args, **kwargs):
            nonlocal count
            count += 1
            if (count > limit):
                print(f"Error: {function} call too many times")
            else:
                function(*args, **kwargs)
        return limit_function
    return callLimiter


def main():
    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g(a="idk"):
        print(f"g({a})")

    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
