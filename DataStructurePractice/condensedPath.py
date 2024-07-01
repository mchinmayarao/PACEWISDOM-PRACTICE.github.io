def condense(path):

    components = path.split('/')
    stack = []

    for c in components:
        if c == '..':
            if stack:
                stack.pop()
        elif c and c != '.':
            stack.append(c)

    return "/"+ "/".join(stack)

paths = [
    "/home/",
    "/../",
    "/home//foo/",
    "/a/./b/../../c/",
    "/a/../../b/../c//.//",
    "/./././a/b/c/",
    "/a/./b/././c/d/",
    "/a/../b/./c/../../d/",
    "////a////b////.////.////c//d///",
    "/a//b//c///../d/././e/../../f/"
]

for path in paths:
    print(f"'{path}'   : {condense(path)}\n")