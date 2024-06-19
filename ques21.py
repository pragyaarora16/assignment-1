def count_occurrences(lst, element):

    return lst.count(element)


if __name__ == "__main__":
    sample_list = [1, 2, 3, 2, 4, 2, 5, 2, 6, 2]
    element_to_count = 2
    occurrences = count_occurrences(sample_list, element_to_count)
    print(f"The element {element_to_count} occurs {occurrences} times in the list.")
