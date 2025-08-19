"""
DSA Concepts Demonstration for Text Encrypter
Educational examples showing data structures and algorithms in action
"""

from collections import deque
import time
import hashlib
import random

class DSADemo:
    def __init__(self):
        # Data Structures
        self.encryption_stack = []          # Stack - LIFO
        self.request_queue = deque()        # Queue - FIFO  
        self.algorithm_map = {              # Hash Table - O(1) lookup
            'caesar': self.caesar_cipher,
            'hash': self.hash_function,
            'reverse': self.reverse_string
        }
    
    def demonstrate_stack(self):
        """Stack Operations - Last In, First Out (LIFO)"""
        print("📚 STACK Operations (LIFO):")
        print("-" * 40)
        
        # Push operations
        operations = ["Encrypt 'hello'", "Encrypt 'world'", "Encrypt 'python'"]
        
        for op in operations:
            self.encryption_stack.append(op)
            print(f"  PUSH: {op}")
            print(f"  Stack: {self.encryption_stack}")
        
        print("\n  Processing stack (LIFO order):")
        
        # Pop operations
        while self.encryption_stack:
            processed = self.encryption_stack.pop()
            print(f"  POP: {processed}")
        
        print("  ✅ Stack is now empty\n")
    
    def demonstrate_queue(self):
        """Queue Operations - First In, First Out (FIFO)"""
        print("🚗 QUEUE Operations (FIFO):")
        print("-" * 40)
        
        # Enqueue operations
        requests = ["User A request", "User B request", "User C request"]
        
        for req in requests:
            self.request_queue.append(req)
            print(f"  ENQUEUE: {req}")
            print(f"  Queue: {list(self.request_queue)}")
        
        print("\n  Processing queue (FIFO order):")
        
        # Dequeue operations
        while self.request_queue:
            processed = self.request_queue.popleft()
            print(f"  DEQUEUE: {processed}")
        
        print("  ✅ Queue is now empty\n")
    
    def demonstrate_hash_table(self):
        """Hash Table - Constant time O(1) lookup"""
        print("🗂️ HASH TABLE Lookup (O(1)):")
        print("-" * 40)
        
        algorithms = ['caesar', 'hash', 'reverse']
        
        for algo in algorithms:
            start_time = time.time()
            
            # O(1) lookup regardless of table size
            if algo in self.algorithm_map:
                func = self.algorithm_map[algo]
                result = func("demo")
                lookup_time = time.time() - start_time
                
                print(f"  {algo.capitalize()}: {result} (Time: {lookup_time:.6f}s)")
        
        print("  ✅ Hash table provides constant-time access\n")
    
    def time_complexity_demo(self):
        """Compare algorithm time complexities"""
        print("⏱️ TIME COMPLEXITY Analysis:")
        print("-" * 40)
        
        test_sizes = [100, 1000, 5000]
        
        for size in test_sizes:
            test_data = "a" * size
            
            # O(n) - Linear time algorithms
            start = time.time()
            self.caesar_cipher(test_data)
            caesar_time = time.time() - start
            
            start = time.time()
            self.hash_function(test_data)
            hash_time = time.time() - start
            
            # O(1) - Constant time lookup
            start = time.time()
            self.algorithm_map.get('caesar')
            lookup_time = time.time() - start
            
            print(f"  Input size {size:,} characters:")
            print(f"    Caesar O(n):    {caesar_time:.6f}s")
            print(f"    Hash O(n):      {hash_time:.6f}s")
            print(f"    Lookup O(1):    {lookup_time:.6f}s")
        print()
    
    def sorting_comparison(self):
        """Compare sorting algorithm performance"""
        print("🔄 SORTING Algorithm Comparison:")
        print("-" * 40)
        
        # Generate random data
        data = [random.randint(1, 100) for _ in range(20)]
        print(f"  Original data: {data[:10]}... (showing first 10)")
        
        # Bubble Sort - O(n²)
        bubble_data = data.copy()
        start = time.time()
        self.bubble_sort(bubble_data)
        bubble_time = time.time() - start
        
        # Built-in Sort - O(n log n)
        builtin_data = data.copy()
        start = time.time()
        builtin_data.sort()
        builtin_time = time.time() - start
        
        print(f"  Bubble Sort O(n²):      {bubble_time:.6f}s")
        print(f"  Built-in Sort O(n log n): {builtin_time:.6f}s")
        print(f"  Speedup factor: {bubble_time/builtin_time:.1f}x faster\n")
    
    def search_comparison(self):
        """Compare search algorithm performance"""
        print("🔍 SEARCH Algorithm Comparison:")
        print("-" * 40)
        
        # Create sorted data for binary search
        data = list(range(1, 1001))  # 1 to 1000
        target = 750
        
        # Linear Search - O(n)
        start = time.time()
        linear_result = self.linear_search(data, target)
        linear_time = time.time() - start
        
        # Binary Search - O(log n)
        start = time.time()
        binary_result = self.binary_search(data, target)
        binary_time = time.time() - start
        
        print(f"  Searching for {target} in {len(data):,} items:")
        print(f"  Linear Search O(n):     Index {linear_result}, {linear_time:.6f}s")
        print(f"  Binary Search O(log n): Index {binary_result}, {binary_time:.6f}s")
        
        if linear_time > 0 and binary_time > 0:
            speedup = linear_time / binary_time
            print(f"  Binary search is {speedup:.1f}x faster\n")
        else:
            print("  Both algorithms executed too quickly to measure\n")
    
    # Helper algorithms with different complexities
    def caesar_cipher(self, text, shift=3):
        """Caesar cipher - O(n) time complexity"""
        result = ""
        for char in text:  # O(n) - visit each character once
            if char.isalpha():
                base = 65 if char.isupper() else 97
                shifted = (ord(char) - base + shift) % 26 + base
                result += chr(shifted)
            else:
                result += char
        return result
    
    def hash_function(self, text):
        """SHA-256 hash - O(n) time complexity"""
        return hashlib.sha256(text.encode()).hexdigest()[:16]  # First 16 chars
    
    def reverse_string(self, text):
        """String reversal - O(n) time complexity"""
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
        for i, value in enumerate(arr):
            if value == target:
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
    """Run comprehensive DSA demonstrations"""
    print("🐍 DATA STRUCTURES & ALGORITHMS")
    print("Educational Demo for Text Encrypter Project")
    print("=" * 60)
    
    dsa = DSADemo()
    
    # Run all demonstrations
    dsa.demonstrate_stack()
    dsa.demonstrate_queue() 
    dsa.demonstrate_hash_table()
    dsa.time_complexity_demo()
    dsa.sorting_comparison()
    dsa.search_comparison()
    
    # Summary
    print("🎓 DSA CONCEPTS in Text Encrypter:")
    print("-" * 40)
    print("  • Stack: Encryption operation history (LIFO)")
    print("  • Queue: User request processing (FIFO)")
    print("  • Hash Table: Fast algorithm selection (O(1))")
    print("  • Linear Algorithms: Text processing (O(n))")
    print("  • Time Analysis: Performance measurement")
    print("  • Search/Sort: Data organization and retrieval")
    print("\n✨ Understanding these concepts helps build efficient software!")

if __name__ == "__main__":
    main()