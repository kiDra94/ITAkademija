import numpy as np

x = np.random.rand(4, 3)
print(x)
print("---------------")
print(np.sum(x, axis=0))
print("---------------")
print(np.sum(x, axis=0, keepdims=True))
print("---------------")
# Output for below statement: (3,)
print((np.sum(x, axis=0)).shape)
print("---------------")
# Output for below statement: (1, 3)
print((np.sum(x, axis=0, keepdims=True)).shape)