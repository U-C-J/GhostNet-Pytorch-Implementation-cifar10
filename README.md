# GhostNet-Pytorch-Implementation-cifar10

I would like to modify ResNet with Ghost Module. 

The implementation was inclueded in testmodel\resnet.py. The basic ResNet structure was copied from [1]. 

(1) Firstly, I tested the model complexity of ResNet56 and ResNet56-ghost. The result is as below:


![](https://github.com/U-C-J/GhostNet-Pytorch-Implementation-cifar10/blob/master/Screenshot%20from%202020-08-04%2014-58-08.png)


I am trying to figure out why my ghost model flops and weights are different. If you have any idea, please tell me.


[1] https://github.com/akamaster/pytorch_resnet_cifar10

[2] https://github.com/TingsongYu/ghostnet_cifar10
