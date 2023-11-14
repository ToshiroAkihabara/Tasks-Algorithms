

main = "Hello world hello"
target = "hello"

def count_occurrences(main_str: str, sub_str: str) -> int:
    main_str = main_str.lower()
    sub_str = sub_str.lower()
    targets = []
    for i in range(len(main_str)):
        if main_str.startswith(sub_str, i):
            targets.append(i)
    return len(targets)

print(count_occurrences(main, target))