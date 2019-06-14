class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # check new node val < current node val
    if value < self.value:
      # if no left child, place new node
      if not self.left:
        self.left = BinarySearchTree(value)
      # else repeat the proccess
      else:
        self.left.insert(value)

    # Check new node val >= current node val
    if value >= self.value:
      # if no right child, place new node
      if not self.right:
        self.right = BinarySearchTree(value)
      # otherwise repeat process
      else:
        self.right.insert(value)

  def contains(self, target):
    current = self
    complete = False
    while not complete:
      if not current:
        return False
      if current.value == target:
        return True
      elif current.value > target:
        current = current.left
      else:
        current = current.right

  def get_max(self):
    current = self
    max = 0
    while current:
      if current.value > max:
        max = current.value
        current = current.right
    return max

  def for_each(self, cb):
    cb(self.value)
    if self.right is None and self.left is None:
      return
    else:
      if self.left is not None:
        self.left.for_each(cb)
      if self.right is not None:
        self.right.for_each(cb)

    return
