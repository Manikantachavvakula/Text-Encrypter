"""
DSA Concepts Demonstrated in Text Encrypter
Educational examples showing how data structures and algorithms work
"""

from collections import deque
import time
import hashlib

class DSADemo:
    def __init__(self):
        # Stack - LIFO (Last In, First Out)
        self.encryption_stack = []
        
        # Queue - FIFO (First In, First Out)
        self.encryption_queue = deque()
        
        # Hash Table - O(1) lookup time
        self.algorithm_lookup = {
            'caesar': self.caesar_cipher,
            'hash': self.hash_function,
            'reverse': self.reverse_string
        }
    
    def demonstrate_stack(self):
        """Stack Operations - LIFO principle"""
        print("📚 STACK Operations (LIFO):")
        
        # Push operations - O(1)
        operations = ["Encrypt 'hello'", "Encrypt 'world'", "Encrypt 'python'"]
        
        for op in operations:
            self.encryption_stack.append(op)
            print(f"  PUSH: {op}")
        
        print(f"  Stack: {self.encryption_stack}")
        
        # Pop operations - O(1)
        while self.encryption_stack:
            popped = self.encryption_stack.pop()
            print(f"  POP: {popped}")
        
        print("  Stack is now empty\n")
    
    def demonstrate_queue(self):
        """Queue Operations - FIFO principle"""
        print("🚗 QUEUE Operations (FIFO):")
        
        # Enqueue operations - O(1)
        requests = ["Request 1", "Request 2", "Request 3"]
        
        for req in requests:
            self.encryption_queue.append(req)
            print(f"  ENQUEUE: {req}")
        
        print(f"  Queue: {list(self.encryption_queue)}")
        
        # Dequeue operations - O(1)
        while self.encryption_queue:
            processed = self.encryption_queue.popleft()
            print(f"  DEQUEUE: {processed}")
        
        print("  Queue is now empty\n")
    
    def demonstrate_hash_table(self):
        """Hash Table - O(1) lookup demonstration"""
        print("🗂️ HASH TABLE Lookup (O(1)):")
        
        algorithms = ['caesar', 'hash', 'reverse']
        
        for algo in algorithms:
            start_time = time.time()
            
            # O(1) lookup time regardless of table size
            if algo in self.algorithm_lookup:
                func = self.algorithm_lookup[algo]
                result = func("test")
                lookup_time = time.time() - start_time
                
                print(f"  {algo}: {result} (lookup: {lookup_time:.6f}s)")
        print()
    
    def time_complexity_analysis(self):
        """Analyze time complexities of different operations"""
        print("⏱️ TIME COMPLEXITY Analysis:")
        
        test_sizes = [10, 100, 1000]
        
        for size in test_sizes:
            test_string = "a" * size
            
            # O(n) - Linear time
            start = time.time()
            self.caesar_cipher(test_string)
            linear_time = time.time() - start
            
            # O(n) - Hash function
            start = time.time()
            self.hash_function(test_string)
            hash_time = time.time() - start
            
            # O(1) - Hash table lookup
            start = time.time()
            self.algorithm_lookup.get('caesar')
            lookup_time = time.time() - start
            
            print(f"  Size {size}:")
            print(f"    Caesar O(n): {linear_time:.6f}s")
            print(f"    Hash O(n): {hash_time:.6f}s")
            print(f"    Lookup O(1): {lookup_time:.6f}s")
        print()
    
    def sorting_demo(self):
        """Demonstrate different sorting algorithms"""
        print("🔄 SORTING Algorithms:")
        
        import random
        data = [random.randint(1, 100) for _ in range(10)]
        print(f"  Original: {data}")
        
        # Bubble Sort - O(n²)
        bubble_data = data.copy()
        start = time.time()
        self.bubble_sort(bubble_data)
        bubble_time = time.time() - start
        print(f"  Bubble Sort O(n²): {bubble_data} ({bubble_time:.6f}s)")
        
        # Built-in Sort - O(n log n)
        builtin_data = data.copy()
        start = time.time()
        builtin_data.sort()
        builtin_time = time.time() - start
        print(f"  Built-in Sort O(n log n): {builtin_data} ({builtin_time:.6f}s)")
        print()
    
    def search_algorithms(self):
        """Demonstrate search algorithms"""
        print("🔍 SEARCH Algorithms:")
        
        # Linear Search - O(n)
        data = list(range(1, 101))  # 1 to 100
        target = 75
        
        start = time.time()
        linear_result = self.linear_search(data, target)
        linear_time = time.time() - start
        
        # Binary Search - O(log n)
        start = time.time()
        binary_result = self.binary_search(data, target)
        binary_time = time.time() - start
        
        print(f"  Linear Search O(n): Found {target} at index {linear_result} ({linear_time:.6f}s)")
        print(f"  Binary Search O(log n): Found {target} at index {binary_result} ({binary_time:.6f}s)")
        print()
    
    # Helper algorithms
    def caesar_cipher(self, text, shift=3):
        """Caesar cipher - O(n) time complexity"""
        result = ""
        for char in text:  # O(n) - process each character once
            if char.isalpha():
                base = 65 if char.isupper() else 97
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += char
        return result
    
    def hash_function(self, text):
        """Hash function - O(n) time complexity"""
        return hashlib.md5(text.encode()).hexdigest()
    
    def reverse_string(self, text):
        """Reverse string - O(n) time complexity"""
        return text[::-1]
    
    def bubble_sort(self, arr):
        """Bubble sort - O(n²) time complexity"""
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    
    def linear_search(self, arr, target):
        """Linear search - O(n) time complexity"""
        for i, val in enumerate(arr):
            if val == target:
                return i
        return -1
    
    def binary_search(self, arr, target):
        """Binary search - O(log n) time complexity"""
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

def main():
    """Run all DSA demonstrations"""
    print("🐍 DATA STRUCTURES & ALGORITHMS in Text Encrypter\n")
    print("=" * 60)
    
    dsa = DSADemo()
    
    # Demonstrate each concept
    dsa.demonstrate_stack()
    dsa.demonstrate_queue()
    dsa.demonstrate_hash_table()
    dsa.time_complexity_analysis()
    dsa.sorting_demo()
    dsa.search_algorithms()
    
    print("🎓 DSA concepts used in our encryption project:")
    print("  • Stack: Storing encryption history (LIFO)")
    print("  • Queue: Processing encryption requests (FIFO)")
    print("  • Hash Table: Fast algorithm lookup (O(1))")
    print("  • String Algorithms: Caesar cipher implementation")
    print("  • Time Complexity: Algorithm performance analysis")

if __name__ == "__main__":
    main()