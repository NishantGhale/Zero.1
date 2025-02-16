def linear_search(arr, key):
    """Perform linear search on the array."""
    for index, value in enumerate(arr):
        if value == key:
            return index  # Return the index if found
    return -1  # Return -1 if not found


def binary_search(arr, key):
    """Perform binary search on the sorted array."""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        if arr[mid] == key:
            return mid  # Return the index if found
        elif arr[mid] < key:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half
    return -1  # Return -1 if not found


def main():
    while True:
        print("\n1. Linear Search")
        print("2. Binary Search")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            n = int(input("Enter number of elements: "))
            arr = []
            print("Enter elements:")
            for _ in range(n):
                arr.append(int(input()))
            key = int(input("Enter search key: "))
            pos = linear_search(arr, key)
            if pos != -1:
                print(f"Element found at position: {pos}")
            else:
                print("Element not found")

        elif choice == '2':
            n = int(input("Enter number of elements (sorted): "))
            arr = []
            print("Enter elements in sorted order:")
            for _ in range(n):
                arr.append(int(input()))
            key = int(input("Enter search key: "))
            pos = binary_search(arr, key)
            if pos != -1:
                print(f"Element found at position: {pos}")
            else:
                print("Element not found")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
