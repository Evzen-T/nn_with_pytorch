import torch
import numpy as np

# # scalar/vector/Matrix
# x1 = torch.empty(1)
# print(x1)
# x2 = torch.empty(3)
# print(x2)
# x3 = torch.empty(2,3)
# print(x3)
# x4 = torch.empty(3, 2,3)
# print(x4)

# # torch.rand - randomizes value
# x5 = torch.rand(2,2)
# print(x5)

# # torch.zeros - gives only 0's
# x6 = torch.zeros(2,2)
# print(x6)

# # torch.ones -  gives only 1's
# x7 = torch.ones(2,2)
# print(x7)

# # torch dtype - int/doubles/float
# x8 = torch.empty(2,2, dtype=torch.int)
# print(x8)
# print(x8.dtype)
# print(x8.size())

# tensors
# x9 = torch.tensor([2.5,0.1])
# print(x9)

# # tensor math
# y1 = torch.rand(2,2)
# y2 = torch.rand(2,2)
# print(y1)
# print(y2)
# # Addition / subtraction
# z = y1 + y2
# z = torch.add(y1, y2)
# print(z)
# #OR
# y1.add_(y2) #underscore @ the end means that y1 will change according to the math done
# print(y1)

# # Multiplication / division
# z = y1 * y2
# z = torch.mul(y1,y2)
# print(z)
# #OR
# y1.mul_(y2) #underscore @ the end means that it allows to modify the variable in place
# print(z)

# # tensor slicing / manipulation
# x10 = torch.rand(4,4)
# print(x10)
# print(x10[:,0]) #slice the tensor & gives only first column of all rows
# print(x10[1,1].item()) #gets a specific value in the tensor
# z1 = x10.view(16) #resized tensor into a scalar/1D list
# print(z1)
# z1 = x10.view(-1,8) #resize tensor
# print(z1)

# Numpy & Torch tensors
# a = torch.ones(5)
# print(a)
# b = a.numpy()
# print(type(b))

# a.add_(1) #Becareful when manipulating variables with that are linked to each other
# print(a)
# print(b)

#OR

# a = np.ones(5)
# print(a)
# b = torch.from_numpy(a)
# print(b)

# a+=1 #Becareful when manipulating variables with that are linked to each other
# print(a)
# print(b)

# # torch.cuda.is_available():
# if torch.cuda.is_available():
#     device = torch.device('cuda')
#     y3 = torch.ones(5, device=device) #runs this operation on gpu mem
#     y4 = torch.ones(5)
#     y4 = y4.to(device)
#     z2 = y3 + y4
#     print(z2)
#     z2 = z2.to('cpu') #runs operation on cpu mem
#     print(z2)

# # Requires grad - Tells pytorch to calculate the gradient for this tensor later in the optimization steps
# x11 = torch.ones(5, requires_grad=True)
# print(x11)