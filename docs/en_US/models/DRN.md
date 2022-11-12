# DRN(CVPR 2020)
A paddle implementation of the paper DRN: Closed-loop Matters: Dual Regression Networks for
Single Image Super-Resolution, 
[\[CVPR 2020\]](https://arxiv.org/pdf/2003.07018.pdf)


## Abstract
Deep neural networks have exhibited promising performance in image super-resolution (SR) by learning a non-linear mapping function from low-resolution (LR) images to high-resolution (HR) images. However, there are two underlying limitations to existing SR methods. First, learning the mapping function from LR to HR images is typically an ill-posed problem, because there exist infinite HR images that can be downsampled to the same LR image. As a result, the space of the possible functions can be extremely large, which makes it hard to find a good solution. Second, the paired LR-HR data may be unavailable in real-world applications and the underlying degradation method is often unknown. For such a more general case, existing SR models often incur the adaptation problem and yield poor per-formance. To address the above issues, we propose a dual regression scheme by introducing an additional constraint on LR data to reduce the space of the possible functions. Specifically, besides the mapping from LR to HR images, we learn an additional dual regression mapping estimates the down-sampling kernel and reconstruct LR images, which forms a closed-loop to provide additional supervision. More critically, since the dual regression process does not depend on HR images, we can directly learn from LR images. In
this sense, we can easily adapt SR models to real-world data, e.g., raw video frames from YouTube. Extensive experiments with paired training data and unpaired real-world data demonstrate our superiority over existing methods.


## Training

As the DRN network is designed for the image super-segmentation task, the input channels to the network are reserved for 3. The following command is executed to train the DRN using the `PMBA` dataset

```shell
python -u tools/main.py --config-file configs/drn_dsr_x4.yaml
```

## Evaluation
**DSR-TestData**

Execute the following command to test the `DSR-TestData` dataset
```shell
python -u tools/main.py --config-file configs/drn_dsr_x4.yaml --evaluate-only --load drn_x4_best.pdparams
```


## Models

[Pretraining Model](https://aistudio.baidu.com/aistudio/datasetdetail/176907)
You can use this trained weight to reproduce the results reported in [README.md](README.md)


## Citation
If you find this code useful in your research, please cite:
```
@INPROCEEDINGS{9157622,
  author={Guo, Yong and Chen, Jian and Wang, Jingdong and Chen, Qi and Cao, Jiezhang and Deng, Zeshuai and Xu, Yanwu and Tan, Mingkui},
  booktitle={2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)}, 
  title={Closed-Loop Matters: Dual Regression Networks for Single Image Super-Resolution}, 
  year={2020},
  pages={5406-5415},
  doi={10.1109/CVPR42600.2020.00545}}
```