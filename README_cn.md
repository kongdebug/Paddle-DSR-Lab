# Paddle-DSR-Lab：深度图超分辨率的工具箱
</div>

<div align="center">

[English](README.md)| [简体中文](README_cn.md)

</div>

Paddle-DSR-Lab 是一款基于 PaddlePaddle 的深度图超分辨率的工具箱，是 PaddleDepth项目的成员之一。 它具有可扩展性，容易上手的特点，此外它在相同的训练策略和环境下公平比较了深度图超分辨率领域以及图像超分辨率里SOTA(state-of-the-art)的算法

## 基准测试和模型库

作为初始版本，Paddle-DSR-Lab目前支持以下算法。
1. [WAFP-Net (IEEE Transactions on Multimedia 2021)[1]](docs/zh_CN/models/WAFP-Net.md)
2. [PMBANet (IEEE Transactions on Image Processing 2019)[2]](docs/zh_CN/models/PMBANet.md)


## 安装

你可以通过如下命令下载Paddle-DSR-Lab工具箱

```
git clone https://github.com/kongdebug/Paddle-DSR-Lab.git
cd Paddle-DSR-Lab
pip install -r requirements.txt
```

## 数据集准备

你可以参照[数据集准备](docs/zh_CN/datasets)文件夹下对应文档来进行相关模型的数据集的准备

## 如何使用

### 训练模型

```shell
python -u tools/main.py --config-file configs/wafp_x4.yaml
```

- `config-file`参数为训练模型的配置文件路径
- 若有预训练权重进行finetune，则运行以下命令启动训练，`load`参数为预训练权重的路径

```shell
python -u tools/main.py --config-file $file_path$ --load $weight_path$
```

- 若训练中断，需要恢复训练，则运行以下命令，`resume`参数为checkpoint路径

```shell
python -u tools/main.py --config-file $file_path$ --resume $checkpoint_path$
```


### 测试模型

```shell
python -u tools/main.py --config-file $file_path$ --evaluate-only --load $weight_path$
```

## 定制化算法

Paddle-DSR-Lab的文件结构如下所示

```shell
Paddle-DSR-Lab
    │  README.md                # 英文说明文档
    │  README_cn.md             # 中文说明文档
    │  requirements.txt         # 安装依赖文件
    ├─configs                   # 配置文件
    ├─data                      # 数据处理
    │  ├─process_DocumentIMG    # 处理百度网盘超分比赛数据
    │  └─process_wafp           # 处理WAFP所用数据
    ├─docs                      # 模型以及数据集的介绍文档
    ├─ppdsr 
    │  ├─datasets               # 数据类定义、加载相关
    │  │  └─preprocess          # 数据增强相关
    │  ├─engine                 # 训练、测试总体代码
    │  ├─metrics                # 评估指标相关
    │  ├─models                 # 模型相关
    │  │  ├─backbones           # 可共用的模型backbone
    │  │  ├─criterions          # 损失函数
    │  │  └─generators          # 模型组网文件
    │  ├─modules                # 组网辅助文件，如参数初始化等
    │  ├─solver                 # 优化器相关
    │  └─utils                  # 数据读取、日志显示等辅助工具
    └─tools                     # 训练、测试启动工具
```


