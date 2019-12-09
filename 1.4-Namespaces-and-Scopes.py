namespace_dict = {}
n_commands = int(input())
for command in range(n_commands):
    com, n_space, var = input().split()
    if com == 'add':
        if n_space in namespace_dict:
            namespace_dict[n_space].append(var)
        else:
            namespace_dict.update({n_space: var})
    if com == 'create':
        