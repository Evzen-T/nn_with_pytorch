import torch

# # Calculate gradient by specifying requires_grad
# x = torch.randn(3, requires_grad=True)
# print(x)

# y = x + 2 # input nodes = x & 2, output nodes = y
# print(y) #back propagates after operation ^

# z = y*y*2 # Scalar value
# z = z.mean()
# print(z)
# # Since there is z is mean & values are scalar, therefore no need for value in backward
# z.backward() #dz/dx
# print(x.grad)

# z = y*y*2
# v = torch.tensor([0.1,1.0,0.001],dtype=torch.float32) # Add
# z.backward(v) #dz/dx
# print(x.grad)

# # Prevent tracking history
# x = torch.randn(3,requires_grad=True)
# print(x)
# x.requires_grad_(False)
# print(x)
# y = x.detach()
# print(y)
# with torch.no_grad():
#     y = x + 2
#     print(y)

# # summation over epochs with require_grad
# weights = torch.ones(4, requires_grad=True)
# for epoch in range(3):
#     model_output = (weights*3).sum()

#     model_output.backward()
#     print(weights.grad)

# # without summation over epochs
# weights = torch.ones(4, requires_grad=True)
# for epoch in range(3):
#     model_output = (weights*3).sum()

#     model_output.backward()
#     print(weights.grad)
    
#     weights.grad.zero_()

# optimizer = torch.optim.SGD(weights, lr=0.01)
# optimizer.step() #optimization step
# optimizer.zero_grad()