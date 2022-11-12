# PMBANet(IEEE Transactions on Image Processing 2020)
A paddle implementation of the paper PMBANet: Progressive Multi-Branch Aggregation Network for Scene Depth Super-Resolution,
[\[IEEE Transactions on Image Processing 2020\]](https://ieeexplore.ieee.org/document/9127098)

## 摘要

深度图的超分辨率是一个有许多挑战的逆向问题。首先，深度边界通常很难重建，特别是在大的放大系数下。其次，场景中的精细结构和微小物体上的深度区域会被下采样退化所严重破坏。为了解决这些困难，我们提出了一个渐进式多分支聚合网络（PMBANet），它由堆叠的MBA块组成，以充分解决上述问题并逐步恢复退化的深度图。具体来说，每个MBA块有多个平行分支。1）重建分支是基于设计的基于注意力的误差前馈/后退模块提出的，它通过对模块施加注意力机制，逐步突出深度边界的信息特征，迭代地利用和补偿降采样误差来完善深度图。2）我们制定了一个单独的指导分支作为先验知识来帮助恢复深度细节，其中多尺度分支是学习一个多尺度表示，密切关注不同尺度的物体，而颜色分支通过使用辅助颜色信息来规范深度图。然后，引入一个融合块来自适应地融合和选择来自所有分支的鉴别性特征。我们整个网络的设计方法是有根有据的，在基准数据集上进行的大量实验表明，与最先进的方法相比，我们的方法取得了卓越的性能


## 训练

执行以下命令，使用`PMBA`数据集训练PMBANet

```shell
python -u tools/main.py --config-file configs/pmba_x4.yaml
```

## 测试

**DSR-TestData**
执行以下命令，对`DSR-TestData`数据集进行测试
```shell
python -u tools/main.py --config-file configs/pmba_x4.yaml --evaluate-only --load pmba_x4_best.pdparams
```

## 模型

[Pretraining Model](https://aistudio.baidu.com/aistudio/datasetdetail/176907)
你可以使用这个训练好的权重来重现[README_cn.md](README_cn.md)中报告的结果


## 引用

如果你觉得代码对你的研究有帮助，请引用
```
@ARTICLE{9127098,
  author={Ye, Xinchen and Sun, Baoli and Wang, Zhihui and Yang, Jingyu and Xu, Rui and Li, Haojie and Li, Baopu},
  journal={IEEE Transactions on Image Processing}, 
  title={PMBANet: Progressive Multi-Branch Aggregation Network for Scene Depth Super-Resolution}, 
  year={2020},
  volume={29},
  pages={7427-7442},
  doi={10.1109/TIP.2020.3002664}}
```