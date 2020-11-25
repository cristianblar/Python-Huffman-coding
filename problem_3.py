import sys


class Node:

    def __init__(self, character=None, frequency=None):
        self.character = character
        self.frequency = frequency
        self.left_child = None
        self.right_child = None

    def set_left_child(self, node):
        self.left_child = node

    def set_right_child(self, node):
        self.right_child = node

    def get_character(self):
        return self.character

    def get_frequency(self):
        return self.frequency

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child


class Tree:

    def __init__(self, root=None):
        self.root = root

    def set_root(self, node):
        self.root = node

    def get_root(self):
        return self.root

    def binary_codes_traversal(self):
        binary_codes = {}

        if (self.root.get_left_child() is None) and (
                self.root.get_right_child() is None):
            binary_codes[self.root.get_character()] = '1'
            return binary_codes

        path = []

        def traverse(node):
            if node:

                if node.get_character() is not None:
                    binary_codes[node.get_character()] = "".join(path)

                path.append('0')
                traverse(node.get_left_child())

                path.append('1')
                traverse(node.get_right_child())

                if path != []:
                    path.pop()
            else:
                if path != []:
                    path.pop()

        traverse(self.root)
        return binary_codes


# ENCODING:

def huffman_encoding(data):

    data = str(data)

    # List of chars without duplicates:
    chars_list = list(set(data))

    nodes_list = []

    for char in chars_list:
        char_frequency = data.count(char)
        new_node = Node(character=char, frequency=char_frequency)
        nodes_list.append(new_node)

    # "Priority Queue", from lowest to highest frequency:
    sorted_list = sorted(nodes_list, key=lambda node: node.get_frequency())

    while len(sorted_list) > 1:
        left_popped_node = sorted_list.pop(0)
        right_popped_node = sorted_list.pop(0)
        merged_frequency = (left_popped_node.get_frequency() +
                            right_popped_node.get_frequency())
        new_node = Node(frequency=merged_frequency)
        new_node.set_left_child(left_popped_node)
        new_node.set_right_child(right_popped_node)
        # Re-insert the merged node keeping order:
        if sorted_list != []:
            for idx, node in enumerate(sorted_list):
                if node.get_frequency() > new_node.get_frequency():
                    sorted_list.insert(idx, new_node)
                    break
                elif idx == len(sorted_list) - 1:
                    sorted_list.append(new_node)
                    break
                else:
                    continue
        else:
            sorted_list.append(new_node)

    huffman_tree = Tree(root=sorted_list.pop())

    # Dictionary for binary codes:
    binary_codes = huffman_tree.binary_codes_traversal()

    encoded_data = ''

    for character in data:
        encoded_data += binary_codes[character]

    return (encoded_data, huffman_tree)


# DECODING:

def huffman_decoding(encoded_data, tree):

    current_node = tree.get_root()

    decoded_data = ''

    if (current_node.get_left_child() is None) and (
            current_node.get_right_child() is None):
        decoded_data += current_node.get_character() *\
            current_node.get_frequency()
        return decoded_data

    for idx, bit in enumerate(encoded_data):
        if bit == '0':
            current_node = current_node.get_left_child()
        else:
            current_node = current_node.get_right_child()
        if current_node.get_character() is not None:  # If it's a leaf...
            decoded_data += current_node.get_character()
            current_node = tree.get_root()

    return decoded_data


if __name__ == "__main__":

    # TEST CASE 1:
    print('TEST CASE 1:')
    a_great_sentence = 'AAAAAAABBBCCCCCCCDDEEEEEE'

    print('The content of the data to encode is: {}.\n'.format(
        a_great_sentence))
    print('The size of the data to encode is: {}.\n'.format(
        sys.getsizeof(a_great_sentence)))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print('The data has been encoded.\n')

    print('The content of the encoded data is: {}.\n'.format(encoded_data))
    print('The size of the encoded data is: {}.\n'.format(
        sys.getsizeof(int(encoded_data, base=2))))

    decoded_data = huffman_decoding(encoded_data, tree)

    print('The data has been decoded.\n')

    print('The content of the decoded data is: {}.\n'.format(decoded_data))
    print('The size of the decoded data is: {}.\n'.format(
        sys.getsizeof(decoded_data)))

    # TEST CASE 2:
    print('TEST CASE 2:')
    a_great_sentence = 'cristian'

    print('The content of the data to encode is: {}.\n'.format(
        a_great_sentence))
    print('The size of the data to encode is: {}.\n'.format(
        sys.getsizeof(a_great_sentence)))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print('The data has been encoded.\n')

    print('The content of the encoded data is: {}.\n'.format(encoded_data))
    print('The size of the encoded data is: {}.\n'.format(
        sys.getsizeof(int(encoded_data, base=2))))

    decoded_data = huffman_decoding(encoded_data, tree)

    print('The data has been decoded.\n')

    print('The content of the decoded data is: {}.\n'.format(decoded_data))
    print('The size of the decoded data is: {}.\n'.format(
        sys.getsizeof(decoded_data)))

    # TEST CASE 3:
    print('TEST CASE 3:')
    a_great_sentence = 'Cristian Julian B'

    print('The content of the data to encode is: {}.\n'.format(
        a_great_sentence))
    print('The size of the data to encode is: {}.\n'.format(
        sys.getsizeof(a_great_sentence)))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print('The data has been encoded.\n')

    print('The content of the encoded data is: {}.\n'.format(encoded_data))
    print('The size of the encoded data is: {}.\n'.format(
        sys.getsizeof(int(encoded_data, base=2))))

    decoded_data = huffman_decoding(encoded_data, tree)

    print('The data has been decoded.\n')

    print('The content of the decoded data is: {}.\n'.format(decoded_data))
    print('The size of the decoded data is: {}.\n'.format(
        sys.getsizeof(decoded_data)))

    # TEST CASE 4:
    print('TEST CASE 4:')
    a_great_sentence = 123456123987654

    print('The content of the data to encode is: {}.\n'.format(
        a_great_sentence))
    print('The size of the data to encode is: {}.\n'.format(
        sys.getsizeof(str(a_great_sentence))))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print('The data has been encoded.\n')

    print('The content of the encoded data is: {}.\n'.format(encoded_data))
    print('The size of the encoded data is: {}.\n'.format(
        sys.getsizeof(int(encoded_data, base=2))))

    decoded_data = huffman_decoding(encoded_data, tree)

    print('The data has been decoded.\n')

    print('The content of the decoded data is: {}.\n'.format(decoded_data))
    print('The size of the decoded data is: {}.\n'.format(
        sys.getsizeof(decoded_data)))

    # TEST CASE 5:
    print('TEST CASE 5:')
    a_great_sentence = None

    print('The content of the data to encode is: {}.\n'.format(
        a_great_sentence))
    print('The size of the data to encode is: {}.\n'.format(
        sys.getsizeof(str(a_great_sentence))))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print('The data has been encoded.\n')

    print('The content of the encoded data is: {}.\n'.format(encoded_data))
    print('The size of the encoded data is: {}.\n'.format(
        sys.getsizeof(int(encoded_data, base=2))))

    decoded_data = huffman_decoding(encoded_data, tree)

    print('The data has been decoded.\n')

    print('The content of the decoded data is: {}.\n'.format(decoded_data))
    print('The size of the decoded data is: {}.\n'.format(
        sys.getsizeof(decoded_data)))


    # TEST CASE 6:
    print('TEST CASE 6:')
    a_great_sentence = 'AAAAAAAAAA'

    print('The content of the data to encode is: {}.\n'.format(
        a_great_sentence))
    print('The size of the data to encode is: {}.\n'.format(
        sys.getsizeof(a_great_sentence)))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print('The data has been encoded.\n')

    print('The content of the encoded data is: {}.\n'.format(encoded_data))
    print('The size of the encoded data is: {}.\n'.format(
        sys.getsizeof(int(encoded_data, base=2))))

    decoded_data = huffman_decoding(encoded_data, tree)

    print('The data has been decoded.\n')

    print('The content of the decoded data is: {}.\n'.format(decoded_data))
    print('The size of the decoded data is: {}.\n'.format(
        sys.getsizeof(decoded_data)))

    # TEST CASE 7:
    print('TEST CASE 7:')
    a_great_sentence = 'AB'

    print('The content of the data to encode is: {}.\n'.format(
        a_great_sentence))
    print('The size of the data to encode is: {}.\n'.format(
        sys.getsizeof(a_great_sentence)))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print('The data has been encoded.\n')

    print('The content of the encoded data is: {}.\n'.format(encoded_data))
    print('The size of the encoded data is: {}.\n'.format(
        sys.getsizeof(int(encoded_data, base=2))))

    decoded_data = huffman_decoding(encoded_data, tree)

    print('The data has been decoded.\n')

    print('The content of the decoded data is: {}.\n'.format(decoded_data))
    print('The size of the decoded data is: {}.\n'.format(
        sys.getsizeof(decoded_data)))

    # TEST CASE 8:
    print('TEST CASE 8:')
    a_great_sentence = ' '

    print('The content of the data to encode is: {}.\n'.format(
        a_great_sentence))
    print('The size of the data to encode is: {}.\n'.format(
        sys.getsizeof(a_great_sentence)))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print('The data has been encoded.\n')

    print('The content of the encoded data is: {}.\n'.format(encoded_data))
    print('The size of the encoded data is: {}.\n'.format(
        sys.getsizeof(int(encoded_data, base=2))))

    decoded_data = huffman_decoding(encoded_data, tree)

    print('The data has been decoded.\n')

    print('The content of the decoded data is: {}.\n'.format(decoded_data))
    print('The size of the decoded data is: {}.\n'.format(
        sys.getsizeof(decoded_data)))
