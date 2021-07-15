import Node


class Huffman:
    def __init__(self):
        self.codes = {}
        self.tree = None

    def compress(self, text):
        # this dict will store chars as tree and their frequencies as values
        frequency = {}
        # iterate over the user input text and calculate their frequencies
        for c in text:
            frequency.setdefault(c, 0)
            frequency[c] += 1
        self.tree = [Node.Node(k, f) for k, f in frequency.items()]

        def bubblesort(arr):
            for i in range(len(arr) - 1):
                for j in range(len(arr) - 1):
                    if arr[j].freq > arr[j + 1].freq:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]

        bubblesort(self.tree)

        while len(self.tree) > 1:
            left = self.tree.pop(0)
            right = self.tree.pop(0)
            self.tree.append(Node.Node(None, left.freq + right.freq, left, right))
            bubblesort(self.tree)

        self.tree = self.tree[0]

        def traverse(tree, code=""):
            if tree.left is None:
                self.codes[tree.char] = code
                return
            if self.tree.right is None:
                self.codes[tree.char] = code
                return
            traverse(tree.left, code + "0")
            traverse(tree.right, code + "1")

        traverse(self.tree)
        print(self.codes)

        for k, v in self.codes.items():
            text = text.replace(k, v)
        return text

    def decompress(self, code):
        decrypted = ""
        current = self.tree
        for c in code:
            if c == "0":
                current = current.left
                if (current.left is None) and (current.right is None):
                    decrypted += current.char
                    current = self.tree
            elif c == "1":
                current = current.right
                if (current.left is None) and (current.right is None):
                    decrypted += current.char
                    current = self.tree

        return decrypted
