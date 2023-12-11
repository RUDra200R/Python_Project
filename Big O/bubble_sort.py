def bubble_sort(data: list) -> None:
    """sorts a list in place."""
    n = len(data)
    comparison_count = 0

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            comparison_count += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True

        print(f"End of pass {i}. `data` is now {data}")
        if not swapped:
            break

    print(f"comparison_count is {comparison_count}")


# numbers = [7, 6, 5, 4, 3, 2, 1]
# numbers = list(range(70, 0, -1))
# print(len(numbers))
# numbers = [1, 2, 3, 4, 5, 6, 7]
numbers = [7, 6, 5, 4, 3, 2, 1]
print(len(numbers))
print(f"sorting {numbers}")
bubble_sort(numbers)
print(f"The sorted data is {numbers}")
