import Huffman

text = input("Enter some text:")
huffman = Huffman.Huffman()
output = huffman.compress(text)
print(output)
output = huffman.decompress(output)
print(output)
