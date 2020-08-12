# GhostNet-Pytorch-Implementation-cifar10

I would like to implement the Ghost-ResNet56[1]. 

The implementation of Ghost-ResNet56 was inclueded in testmodel\resnet.py. The basic ResNet structure was copied from [2]. 

(1) Firstly, I tested the model complexity of ResNet56 and ResNet56-ghost. The testing file is testmodel\getmodel.py. The result is as below:


![](https://github.com/U-C-J/GhostNet-Pytorch-Implementation-cifar10/blob/master/Screenshot%20from%202020-08-04%2014-58-08.png)

The author said they fuse BN layer to previous convolution layer. So I fused BN layer, and then I got 0.44M parameter and 65M FLOPs. For the accuracy, my running accuracy is 91.4%, which is lower than 92.7% in the paper. 



[1] https://github.com/huawei-noah/ghostnet
[2] https://github.com/akamaster/pytorch_resnet_cifar10
[3] https://github.com/TingsongYu/ghostnet_cifar10
