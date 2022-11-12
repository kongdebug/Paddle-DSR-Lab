# DRN(CVPR 2020)
A paddle implementation of the paper DRN: Closed-loop Matters: Dual Regression Networks for
Single Image Super-Resolution, 
[\[CVPR 2020\]](https://arxiv.org/pdf/2003.07018.pdf)


## 摘要

深度神经网络通过学习从低分辨率（LR）图像到高分辨率（HR）图像的非线性映射函数，在图像超分辨率（SR）方面表现出良好的性能。然而，现有的SR方法有两个基本限制。首先，学习从LR图像到HR图像的映射函数通常是一个不理想的问题，因为存在着无限的HR图像可以被下采样到相同的LR图像。因此，可能的函数空间可能非常大，这使得它很难找到一个好的解决方案。其次，在现实世界的应用中，配对的LR-HR数据可能是不可用的，而且基本的降级方法往往是未知的。对于这样一个更普遍的情况，现有的SR模型往往会产生适应问题，并产生较差的性能。为了解决上述问题，我们提出了一个双重回归方案，在LR数据上引入一个额外的约束条件，以减少可能的函数空间。具体来说，除了从LR图像到HR图像的映射，我们还学习一个额外的双重回归映射，估计下采样核并重建LR图像，这形成了一个闭环以提供额外的监督。更关键的是，由于双重回归过程不依赖于HR图像，我们可以直接从LR图像中学习。在这个意义上，我们可以很容易地使SR模型适应现实世界的数据，例如，来自YouTube的原始视频帧。用配对的训练数据和未配对的真实世界数据进行的大量实验证明了我们比现有方法更有优势


## 训练

由于DRN网络是为图像超分任务设计，保留网络的输入通道为3。执行以下命令，使用`PMBA`数据集训练DRN

```shell
python -u tools/main.py --config-file configs/drn_dsr_x4.yaml
```

## 测试

**DSR-TestData**
执行以下命令，对`DSR-TestData`数据集进行测试
```shell
python -u tools/main.py --config-file configs/drn_dsr_x4.yaml --evaluate-only --load drn_x4_best.pdparams
```

## 模型

[Pretraining Model](https://aistudio.baidu.com/aistudio/datasetdetail/176907)
你可以使用这个训练好的权重来重现[README_cn.md](README_cn.md)中报告的结果


## 引用

如果你觉得代码对你的研究有帮助，请引用
```
@INPROCEEDINGS{9157622,
  author={Guo, Yong and Chen, Jian and Wang, Jingdong and Chen, Qi and Cao, Jiezhang and Deng, Zeshuai and Xu, Yanwu and Tan, Mingkui},
  booktitle={2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)}, 
  title={Closed-Loop Matters: Dual Regression Networks for Single Image Super-Resolution}, 
  year={2020},
  pages={5406-5415},
  doi={10.1109/CVPR42600.2020.00545}}
```