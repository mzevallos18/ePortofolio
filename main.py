import csv
from typing import Optional, List, Dict

# Class to represent a course with number, title, and prerequisites
class Course:
    def __init__(self, num: str, title: str, prereqs: List[str]):
        self.courseNum = num.strip().upper()
        self.courseTitle = title.strip()
        self.prerequisites = [p.strip().upper() for p in prereqs if p.strip()]

    # Print course details
    def print(self) -> None:
        prereq_str = "None" if not self.prerequisites else " ".join(self.prerequisites)
        print(f"{self.courseNum}, {self.courseTitle}, Prerequisites: {prereq_str}")


# Node used in the AVL tree
class AVLNode:
    def __init__(self, course: Course):
        self.course = course
        self.left: Optional["AVLNode"] = None
        self.right: Optional["AVLNode"] = None
        self.height: int = 1

# Utility functions for AVL balancing
def _height(n: Optional[AVLNode]) -> int:
    return n.height if n else 0

def _balance_factor(n: AVLNode) -> int:
    return _height(n.left) - _height(n.right)

def _update_height(n: AVLNode) -> None:
    n.height = 1 + max(_height(n.left), _height(n.right))

# Right rotation
def _rotate_right(y: AVLNode) -> AVLNode:
    x = y.left
    T2 = x.right if x else None
    x.right = y
    y.left = T2
    _update_height(y)
    _update_height(x)
    return x

# Left rotation
def _rotate_left(x: AVLNode) -> AVLNode:
    y = x.right
    T2 = y.left if y else None
    y.left = x
    x.right = T2
    _update_height(x)
    _update_height(y)
    return y

# Rebalance a node if needed
def _rebalance(node: AVLNode) -> AVLNode:
    _update_height(node)
    bf = _balance_factor(node)

    # Left heavy
    if bf > 1:
        if _balance_factor(node.left) < 0:
            node.left = _rotate_left(node.left)
        return _rotate_right(node)

    # Right heavy
    if bf < -1:
        if _balance_factor(node.right) > 0:
            node.right = _rotate_right(node.right)
        return _rotate_left(node)

    return node


# AVL Tree to store courses in sorted order
class AVLTree:
    def __init__(self):
        self.root: Optional[AVLNode] = None

    # Insert course into tree
    def insert(self, course: Course) -> None:
        def _insert(n: Optional[AVLNode], c: Course) -> AVLNode:
            if n is None:
                return AVLNode(c)
            if c.courseNum < n.course.courseNum:
                n.left = _insert(n.left, c)
            elif c.courseNum > n.course.courseNum:
                n.right = _insert(n.right, c)
            else:
                # Replace if duplicate
                n.course = c
                return n
            return _rebalance(n)
        self.root = _insert(self.root, course)

    # Find a course by ID
    def find(self, courseID: str) -> Optional[Course]:
        key = courseID.strip().upper()
        n = self.root
        while n:
            if key == n.course.courseNum:
                return n.course
            n = n.left if key < n.course.courseNum else n.right
        return None

    # Return courses in sorted order
    def inorder(self) -> List[Course]:
        out: List[Course] = []
        def _dfs(n: Optional[AVLNode]):
            if not n:
                return
            _dfs(n.left)
            out.append(n.course)
            _dfs(n.right)
        _dfs(self.root)
        return out

    # Return height of tree
    def height(self) -> int:
        return _height(self.root)


# CourseStore holds multiple structures for efficiency
class CourseStore:
    def __init__(self):
        self.array: List[Course] = []          # List of courses
        self.index: Dict[str, Course] = {}     # Fast lookup by course number
        self.avl = AVLTree()                   # AVL tree for sorted order

    # Clear all stored data
    def clear(self) -> None:
        self.array.clear()
        self.index.clear()
        self.avl = AVLTree()

    # Add or update a course
    def add(self, course: Course) -> None:
        if course.courseNum in self.index:
            old = self.index[course.courseNum]
            for i, c in enumerate(self.array):
                if c.courseNum == old.courseNum:
                    self.array[i] = course
                    break
        else:
            self.array.append(course)

        self.index[course.courseNum] = course
        self.avl.insert(course)

    # Print all courses in sorted order
    def list_all_sorted(self) -> None:
        for c in self.avl.inorder():
            c.print()

    # Lookup a course quickly using dictionary
    def lookup_fast(self, courseID: str) -> None:
        c = self.index.get(courseID.strip().upper())
        if c:
            c.print()
        else:
            print("Course not found")

    # Print stats about stored data
    def stats(self) -> None:
        print(f"Total courses: {len(self.array)}")
        print(f"AVL height: {self.avl.height()}")


# Load data from a CSV file
def load_store_from_csv(path: str, store: CourseStore, replace: bool = False) -> None:
    try:
        if replace:
            store.clear()
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            count = 0
            for row in reader:
                if len(row) < 2:
                    print("Error parsing row, expected at least 2 columns")
                    continue
                num = row[0].strip()
                title = row[1].strip()
                prereqs = [p.strip() for p in row[2:]] if len(row) > 2 else []
                if not num or not title:
                    print("Error parsing row, missing course number or title")
                    continue
                store.add(Course(num, title, prereqs))
                count += 1
        print(f"Loaded {count} courses from {path}")
    except FileNotFoundError:
        print("Error: Try a different file")

# Seed with example data
def seed_sample_data(store: CourseStore) -> None:
    rows = [
        ["CSCI100", "Introduction to Computer Science"],
        ["CSCI101", "Introduction to Programming in C++", "CSCI100"],
        ["CSCI200", "Data Structures", "CSCI101"],
        ["MATH201", "Discrete Mathematics"],
        ["CSCI300", "Introduction to Algorithms", "CSCI200", "MATH201"],
        ["CSCI301", "Advanced Programming", "CSCI101"],
        ["CSCI350", "Operating Systems", "CSCI300"],
        ["CSCI400", "Large Software Development", "CSCI301", "CSCI350"],
    ]
    for r in rows:
        store.add(Course(r[0], r[1], r[2:]))
    print("Seeded sample data")


# Main program with menu options
def main():
    store = CourseStore()
    seed_sample_data(store)

    while True:
        print("\nMenu:")
        print("1. Load Data from CSV")
        print("2. Print Course List")
        print("3. Print Course Info")
        print("4. Stats")
        print("9. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            path = input("Enter CSV file path: ").strip()
            mode = input("Replace current data? Y or N: ").strip().upper()
            load_store_from_csv(path, store, replace=(mode == "Y"))
        elif choice == "2":
            print("Courses available:")
            store.list_all_sorted()
        elif choice == "3":
            cid = input("Enter course number: ").strip()
            print("Course Info:")
            store.lookup_fast(cid)
        elif choice == "4":
            store.stats()
        elif choice == "9":
            print("Exiting.")
            break
        else:
            print("Not a valid option.")

# Run program
if __name__ == "__main__":
    main()
