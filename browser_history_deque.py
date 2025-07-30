from collections import deque


browser_history = deque(maxlen=5)
forward_stack = deque()


def add_new_page(url:str):
    browser_history.append(url)

def go_back():
    item = browser_history.pop()
    forward_stack.append(item)

def go_forward():
    item = forward_stack.pop()
    browser_history.append(item)




print(0,browser_history,forward_stack)
add_new_page("www.google.com")
print(1,browser_history,forward_stack)
add_new_page("www.misogiai.com")
print(2,browser_history,forward_stack)
add_new_page("www.linkedin.com")
print(3,browser_history,forward_stack)
go_back()
print(4,browser_history,forward_stack)
go_forward()
print(5,browser_history,forward_stack)
