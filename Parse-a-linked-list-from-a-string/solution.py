def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == "None":
        return None
    lst_repr = list(list_repr.split(' -> '))[:-1]
    node = Node(int(lst_repr.pop()))
    while lst_repr:
        node = Node(int(lst_repr.pop()), node)
    return node
