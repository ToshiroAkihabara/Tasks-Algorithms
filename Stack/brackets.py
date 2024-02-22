
def lifo(item: str) -> bool:
    stack = []
    status = True
    for i in item:
        if i in "({[":
            stack.append(i)
        if i in ")}]":
            if not stack:
                status = False
                break
            compare = stack.pop()
            if compare == "(" and i == ")":
                continue
            elif compare == "[" and i == "]":
                continue
            elif compare == "{" and i == "}":
                continue
    if len(stack) != 0:
        status = False
    return status

