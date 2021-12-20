import math

input_file = "example_input"
input_file = "input"

input_parts = open(input_file).read().splitlines()


class Node:
    def __init__(self, value=None, pair=None) -> None:
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        if pair is not None:
            self.set_pair(*pair)

    def set_pair(self, left, right):
        if self.left is not None:
            self.left.parent = None
        if self.right is not None:
            self.right.parent = None
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def remove_pair(self):
        if self.left is not None:
            self.left.parent = None
            self.left = None
        if self.right is not None:
            self.right.parent = None
            self.right = None

    def __repr__(self) -> str:
        l = self.left.value if self.left is not None else None
        r = self.right.value if self.left is not None else None
        return f'Node<v={self.value} l={l} r={r}>'

    @property
    def is_pair(self):
        return self.value is None and self.left and self.right

    @classmethod
    def from_pair(cls, pair):
        children = []
        for item in pair:
            if isinstance(item, list):
                children.append(cls.from_pair(item))
            else:
                children.append(cls(value=item))
        return cls(pair=children)

    def depth(self):
        d = 0
        node = self.parent
        while node:
            d += 1
            node = node.parent
        return d

    def get_number_to_left(self):
        if not self.parent:
            return None
        if self.parent.right is self:
            if self.parent.left.value is not None:
                return self.parent.left
            node = self.parent.left
            while node.right is not None:
                node = node.right
            return node
        return self.parent.get_number_to_left()

    def get_number_to_right(self):
        if not self.parent:
            return None
        if self.parent.left is self:
            if self.parent.right.value is not None:
                return self.parent.right
            node = self.parent.right
            while node.left is not None:
                node = node.left
            return node
        return self.parent.get_number_to_right()

    def explode(self):
        left2 = self.left.get_number_to_left()
        right2 = self.right.get_number_to_right()
        if left2:
            left2.value += self.left.value
        if right2:
            right2.value += self.right.value
        self.remove_pair()
        self.value = 0

    def split(self):
        if self.value is None:
            raise ValueError("value must be set to split")
        left = Node(value=self.value // 2)
        right = Node(value=int(math.ceil(self.value / 2)))
        self.set_pair(left, right)
        self.value = None


def build_tree(snailfish):
    for pair in snailfish:
        pass


# node = Node.from_pair([1, 2])
# print(node.value, node.left.value, node.right)

# print(Pair)





def find_deep_pair(node, depth=0):
    deep = []
    for subnode in [node.left, node.right]:
        if subnode.value is None:
            if depth == 3:
                deep.append(subnode)
            deep.extend(find_deep_pair(subnode, depth + 1))

    return deep


def explode(snailfish):
    parent, pair = find_deep_pair(snailfish)



def depth_iter(node):
    stack = [node]
    while stack:
        n = stack.pop()
        yield n
        if n.right:
            stack.append(n.right)
        if n.left:
            stack.append(n.left)


def get_as_list(node):
    if node.value is not None:
        return node.value
    return [get_as_list(node.left), get_as_list(node.right)]



def add_nodes(node_a, node_b):
    return Node(pair=(node_a, node_b))


# for inp, oup in (
#         ([[[[[9,8],1],2],3],4], [[[[0,9],2],3],4]),
#         ([7,[6,[5,[4,[3,2]]]]], [7,[6,[5,[7,0]]]]),
#         ([[6,[5,[4,[3,2]]]],1], [[6,[5,[7,0]]],3]),
#         ([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]], [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]),
#         ([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]], [[3,[2,[8,0]]],[9,[5,[7,0]]]])
#     ):
#     node = Node.from_pair(inp)
#     change = True
#     while change:
#         change = False
#         for n in depth_iter(node):
#             if n.is_pair and n.depth() == 4:
#                 n.explode()
#                 change = True
#                 break
#             elif n.value is not None and n.value >= 10:
#                 n.split()
#                 change = True
#                 break
#         break



def get_magnitude(node):
    values = []
    for n in (node.left, node.right):
        if n.value is None:
            v = get_magnitude(n)
        else:
            v = n.value
        values.append(v)
    return values[0] * 3 + values[1] * 2


def reduce_snailfish(node):
    change = True
    while change:
        explodesies = []
        splitsies = []
        for n in depth_iter(node):
            if n.is_pair and n.depth() == 4:
                explodesies.append(n)
                break
            elif n.value is not None and n.value >= 10:
                splitsies.append(n)
        change = True
        if explodesies:
            explodesies[0].explode()
        elif splitsies:
            splitsies[0].split()
        else:
            change = False

node = Node.from_pair([0, [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]])
reduce_snailfish(node)
print(get_as_list(node))

def test():
    ops = '''[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]'''.splitlines()
    # ops = '''[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
    # [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
    # [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
    # [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
    # [7,[5,[[3,8],[1,4]]]]
    # [[2,[2,2]],[8,[8,1]]]
    # [2,9]
    # [1,[[[9,3],9],[[9,0],[0,7]]]]
    # [[[5,[7,4]],7],1]
    # [[[[4,2],2],6],[8,7]]'''.splitlines()[:2]
    # ops = '''[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
    # [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]'''.splitlines()
    ops = '''[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]'''.splitlines()
    node = Node.from_pair(eval(ops[0]))
    for line in ops[1:]:
        new_node = add_nodes(node, Node.from_pair(eval(line)))
        reduce_snailfish(new_node)
        node = new_node

    print(get_as_list(node))
    print(get_magnitude(node))

# test()

def run_it(input_parts):
    node = Node.from_pair(eval(input_parts[0]))
    for line in input_parts[1:]:
        new_node = add_nodes(node, Node.from_pair(eval(line)))
        reduce_snailfish(new_node)
        node = new_node

    print(get_as_list(node))
    print(get_magnitude(node))

# input_parts = '''[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
# [[[5,[2,8]],4],[5,[[9,9],0]]]
# [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
# [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
# [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
# [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
# [[[[5,4],[7,7]],8],[[8,3],8]]
# [[9,3],[[9,9],[6,[4,9]]]]
# [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
# [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]'''.splitlines()

mags = {}
for i in range(len(input_parts)):
    for j in range(len(input_parts)):
        a = Node.from_pair(eval(input_parts[i]))
        if j != i:
            b = Node.from_pair(eval(input_parts[j]))
            c = add_nodes(a, b)
            reduce_snailfish(c)
            mags[get_magnitude(c)] = (i, j)

print(sorted(mags.items())[-1])






# node = Node.from_pair([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]])
# print(get_magnitude(node))
