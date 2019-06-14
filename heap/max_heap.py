class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    swapped_value = self.storage[0]
    self.storage[0] = self.storage[-1]
    self.storage[-1] = swapped_value
    self.storage.pop(-1)
    self._sift_down(0)
    return swapped_value

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    # in worst case elem will need to make its way to the top of the heap
    while index > 0:
      # get parent elem of this index
      parent = (index - 1) // 2
      # check if elem at index is higjer priority then parent elem
      if self.storage[index] > self.storage[parent]:
        # if it is, swap them
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]

        # update index to be new spot that swapped elem now resides at
        index = parent
      else:
        # otherwise, our element is at a valid spot in the heap
        # we no longer need to buble up -> break
        break

  def _sift_down(self, index):
    my_index = index
    if len(self.storage) < 2:
        return
    while (2 * index) + 1 < len(self.storage):
        left_child = (2 * index) + 1
        right_child = (2 * index) + 2
        if right_child > len(self.storage) - 1:
            if self.storage[left_child] > self.storage[index]:
                swapped_value = self.storage[left_child]
                self.storage[left_child] = self.storage[index]
                self.storage[index] = swapped_value
                index = left_child
        elif self.storage[left_child] > self.storage[right_child]:
            if self.storage[left_child] > self.storage[index]:
                swapped_value = self.storage[left_child]
                self.storage[left_child] = self.storage[index]
                self.storage[index] = swapped_value
                index = left_child
            else:
                break
        elif self.storage[right_child] > self.storage[index]:
            swapped_value = self.storage[right_child]
            self.storage[right_child] = self.storage[index]
            self.storage[index] = swapped_value
            index = right_child
        else:
            break
