def merge(array, l, m, r, byfunc): 
    #l=start ind of left arr, m=mid ind, r=end ind of right ind
    #pos=ind of current position
    nleft = m - l + 1
    nright = r - m
    left_arr = array[l:m+1]
    right_arr = array[m+1:r+1]
    left = 0
    right = 0
    pos = l
    while left < nleft and right < nright:
        if byfunc == None:
            if left_arr[left] <= right_arr[right]:
                array[pos] = left_arr[left]
                left += 1
            else:
                array[pos] = right_arr[right]
                right += 1

        else:
            if byfunc(left_arr[left]) <= byfunc(right_arr[right]):
                array[pos] = left_arr[left]
                left += 1
            else:
                array[pos] = right_arr[right]
                right += 1
        pos += 1

    while left < nleft:
        array[pos] = left_arr[left]
        left += 1
        pos += 1
    while right < nright:
        array[pos] = right_arr[right]
        right += 1
        pos += 1

def mergesort_recursion(array, l, r , byfunc):
    if (r-l+1) > 1:
        m = (l+r) // 2
        mergesort_recursion(array, l, m, byfunc)
        mergesort_recursion(array, m+1, r, byfunc)
        merge(array, l, m, r, byfunc)

def mergesort(array, byfunc=None):
    mergesort_recursion(array, 0, len(array)-1, byfunc)
    print(array)

class Stack:
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if len(self.__items) >= 1:
            return self.__items.pop()

    def peek(self):
        if len(self.__items) >= 1:
            return self.__items[-1]
        else:
            return None

    @property
    def is_empty(self):
        return len(self.__items) == 0

    @property
    def size(self):
        return len(self.__items)

class EvaluateExpression:
  valid_char = '0123456789+-*/() '
  def __init__(self, string=""):
    self.expr = string
    self.valid_char = '0123456789+-*/() '
  @property
  def expression(self):
    return self.expr

  @expression.setter
  def expression(self, new_expr):
    flag = True
    for i in new_expr:
      if i not in self.valid_char:
        flag = False
        break
    if flag:
      self.expr = new_expr
    else:
      self.expr = ""

  def insert_space(self):
    new_string = ""
    for i in self.expr:
      if i in "+-*/()":
        new_string = new_string+" "+i+" "
      else:
        new_string = new_string+i
    self.expr = new_string
    return new_string

  def process_operator(self, operand_stack, operator_stack):
    op = operator_stack.pop()
    
    b = operand_stack.pop()
    print(b)
    a = operand_stack.pop()
    print(a)
    if op == "+":
      operand_stack.push(int(a)+int(b))
    elif op == "-":
      operand_stack.push(int(a)-int(b))
    elif op == "*":
      operand_stack.push(int(a)*int(b))
    elif op == "/":
      operand_stack.push(int(a)//int(b))

  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()
    for i in tokens:
      if i not in "+-*/()":
        operand_stack.push(int(i))
      else:
        if i == ")":
          while operator_stack.size != 0 and operator_stack.peek() != "(":
            self.process_operator(operand_stack,operator_stack)
          operator_stack.pop()
        elif i == "(":
          operator_stack.push(i)

        elif operator_stack.size != 0 and operator_stack.peek() in "*/":
          self.process_operator(operand_stack,operator_stack)
          operator_stack.push(i)
        else:
          operator_stack.push(i)
          
    while not operator_stack.is_empty:
      self.process_operator(operand_stack,operator_stack)
    return operand_stack.peek()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]








