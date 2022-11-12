# WAFP-Net(IEEE Transactions on Multimedia 2021)
A paddle implementation of the paper WAFP-Net: Weighted Attention Fusion Based Progressive Residual Learning for Depth Map Super-Resolution,
[\[IEEE Transactions on Multimedia 2021\]](https://ieeexplore.ieee.org/document/9563214)


## Abstract
Despite the remarkable progresses achieved in depth map super-resolution (DSR), it remains a major challenge to tackle with real-world degradation of low-resolution (LR) depth maps. Synthetic datasets are mainly used in existing DSR approaches, which is quite different from what would get from a real depth sensor. Besides, the enhancements of features in existing DSR approaches are not sufficiently enough, which also limit the performance. To alleviate these problems, we first propose two types of degradation models to describe the generation of LR depth maps, including bi-cubic down-sampling with noise and interval down-sampling, and different DSR models are learned correspondingly. Then, we propose a weighted attention fusion strategy that is embedded into a progressive residual learning framework, which guarantees that the high-resolution (HR) depth maps can be well recovered in a coarse-to-fine manner. The weighted attention fusion strategy can enhance the features with abundant high-frequency components in both global and local manners, thus better HR depth maps can be expected. Besides, to re-use the effective information in the progressive process sufficiently, a multi-stage fusion module is combined into the proposed framework, and the Total Generalized Variation (TGV) regularization and input loss are exploited to further improve the performance of our method. Extensive experiments of different benchmarks demonstrate the superiority of our approach over the state-of-the-art (SOTA) approaches.


## Training

```shell
python -u tools/main.py --config-file configs/wafp_x4.yaml
```


## Evaluation
**DSR-TestData**

Execute the following command to test the `DSR-TestData` dataset
```shell
python -u tools/main.py --config-file configs/wafp_x4.yaml --evaluate-only --load wafp_x4_best.pdparams
```


## Models

[Pretraining Model](https://aistudio.baidu.com/aistudio/datasetdetail/176907)
You can use this trained weight to reproduce the results reported in [README.md](README.md)

## Citation
If you find this code useful in your research, please cite:
```
@ARTICLE{9563214,
  author={Song, Xibin and Zhou, Dingfu and Li, Wei and Dai, Yuchao and Liu, Liu and Li, Hongdong and Yang, Ruigang and Zhang, Liangjun},
  journal={IEEE Transactions on Multimedia}, 
  title={WAFP-Net: Weighted Attention Fusion Based Progressive Residual Learning for Depth Map Super-Resolution}, 
  year={2022},
  volume={24},
  pages={4113-4127},
  doi={10.1109/TMM.2021.3118282}}
```