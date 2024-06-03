class Node:
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.frequency = int(frequency)
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency > other.frequency

    def __str__(self):
        return f"{self.symbol} -> {self.frequency}"


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def isGreaterThanOne(self):
        return len(self.queue) > 1
    def insert(self, data):
        self.queue.append(data)

    def pop(self):
        try:
            max_val = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max_val]:
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item
        except IndexError:
            print()
            exit()




class HuffmanCode(object):

    def __init__(self,fileName):
        self.queue = PriorityQueue()
        quantity_of_letters=0
        with open (fileName,"r") as f:
            for line in f:
                tmp = line.split(" ")
                if len(tmp) == 2:
                    self.queue.insert(Node(tmp[0], tmp[1]))
                else:
                     self.quantity_of_letters=tmp


    def mergedNode(self,LeftNode: Node,RightNode: Node):
        return Node(symbol=LeftNode.symbol+RightNode.symbol,frequency=LeftNode.frequency+RightNode.frequency)

    def createHuffmanTree(self):

        while(self.queue.isGreaterThanOne()):
            ##getting nodes here
            left_node = self.queue.pop()
            right_node = self.queue.pop()
            ##creating new node here
            merged_node = self.mergedNode(left_node,right_node)
            merged_node.right = right_node
            merged_node.left = left_node
            ##adding this new node to our priority queue
            self.queue.insert(merged_node)
            print(merged_node)

    def generate_huffman_codes(self,node, code="", huffman_codes={}):
        if node is not None:
            if node.symbol is not None:
                huffman_codes[node.symbol] = code
            self.generate_huffman_codes(node.left, code + "0", huffman_codes)
            self.generate_huffman_codes(node.right, code + "1", huffman_codes)

        return huffman_codes

test = HuffmanCode("huffman.txt")

test.createHuffmanTree()

generated = test.generate_huffman_codes(test.queue.queue[0])

print(generated)
