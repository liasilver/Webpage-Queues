import WebPageIndex
import WebpagePriorityQueue

A = WebPageIndex.AVLtree("doc1-arraylist.txt")
B = WebPageIndex.AVLtree("doc2-graph.txt")
C = WebPageIndex.AVLtree("doc3-binarysearchtree.txt")
D = WebPageIndex.AVLtree("doc4-stack.txt")
E = WebPageIndex.AVLtree("doc5-queue.txt")
F = WebPageIndex.AVLtree("doc6-AVLtree.txt")
G = WebPageIndex.AVLtree("doc7-redblacktree.txt")
H = WebPageIndex.AVLtree("doc8-heap.txt")
I = WebPageIndex.AVLtree("doc9-hashtable.txt")


W = WebpagePriorityQueue.init_("data structures", [A, B, C, D, E ,F, G, H, I])

(WebpagePriorityQueue.peek(W))
