def extract_unique_letters(full_name: str) -> list[str]:
    """Extracts alphabetic characters only (excluding spaces/symbols) and removes duplicates."""
    unsorted_letters = []
    seen = set()

    for ch in full_name.upper():
        if "A" <= ch <= "Z" and ch not in seen:
            seen.add(ch)
            unsorted_letters.append(ch)

    return unsorted_letters


def bubble_sort_letters(letters: list[str]) -> list[str]:
    """Returns a new list sorted in ascending alphabetical order using Bubble Sort."""
    arr = letters.copy()
    n = len(arr)

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


def main():
    full_name = "JANNICA AYSON NATURAL"

    unsorted_array = extract_unique_letters(full_name)

    sorted_array = bubble_sort_letters(unsorted_array)

    print(f"Full Name:       {full_name}")
    print(f"Unsorted Array:  {unsorted_array}")
    print(f"Sorted Array:    {sorted_array}")


if __name__ == "__main__":
    main()