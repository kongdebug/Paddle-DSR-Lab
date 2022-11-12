# WAFP-Net数据集准备说明


## 简介

使用的数据融合了`Middlebury dataset` / `MPI Sintel dataset` 和 `synthetic New Tsukuba dataset` 共三个数据集


## 处理流程

执行以下命令，进入本项目文件夹，下载2个数据集压缩包：`WAFP_data.zip`，`WAFP_test_data.zip` 解压并将`data_all`文件夹（含133张深度图）和`test_data`文件夹（含4个测试数据）放置成以下位置

```shell
cd Paddle-DSR-Lab

wget https://videotag.bj.bcebos.com/Data/WAFP_data.zip
wget https://videotag.bj.bcebos.com/Data/WAFP_test_data.zip

unzip -qo WAFP_data.zip -d ./data/
unzip -qo WAFP_test_data.zip -d ./data/
```

```shell
data/
  ├── data_all/
  │   ├── alley_1_1.png
  │   ├── ...
  │   └── ...
  ├── test_data/
  │   ├── cones_x4.mat
  │   ├── teddy_x4.mat
  │   ├── tskuba_x4.mat
  │   └── venus_x4.mat
```

`data_all`中的深度图需要进行下采样，然后将深度相关高斯噪声以θ（d）=N（0，δ/d）的形式添加到低分辨率训练数据中，其中δ=651，d表示DL中每个像素的深度值。使用`matlab`软件，执行`data/process_wafp/generate_train_noise.m`脚本，生成训练数据`train_depth_x4_noise.h5`，注意使用时修改脚本中`data_all`文件夹路径


## 下载

处理好的训练集`train_depth_x4_noise.h5`已上传至AI Studio平台，链接如下：https://aistudio.baidu.com/aistudio/datasetdetail/154330

