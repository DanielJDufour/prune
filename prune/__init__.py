def prune(tree, branches):
    for branch in branches:
        current = tree
        parts = branch.split(".")
        last = parts.pop()
        for part in parts:
            current = current[part]
            if current is None: break
        if current: del current[last]
    return tree

