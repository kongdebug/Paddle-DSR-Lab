# PMBANet数据集准备说明

## 简介

由于PMBA的repo中并没有提供相关数据，发邮件咨询作者也没得到回复，因此使用与WAFP-Net一致的`Middlebury dataset` / `MPI Sintel dataset` 和 `synthetic New Tsukuba dataset`  三个数据集

## 处理流程

与[WAFP-Net数据处理](docs/zh_CN/datasets/WAFP-Net-Data.md)所用的原始数据一致，进入本项目文件夹，下载2个数据集压缩包：`WAFP_data.zip`，`WAFP_test_data.zip` 解压并将`data_all`文件夹（含133张深度图）和`test_data`文件夹（含4个测试数据）放置成以下位置


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

**注意**：WAFP-Net 将高分辨率的深度图下采样并添加噪声后再上采样至高分辨率深度图的大小，并生成.h5文件作为训练集。这流程与PMBANet、RCAN、DRN等网络所需的数据处理不一致，因此仅保留下采样与添加噪声的操作，生成对应的低分辨率深度图

使用`matlab`软件，执行`data/process_pmba/generate_train_LR.m`脚本，生成训练数据的高分辨率与低分辨率深度图对，注意使用时修改脚本中`data_all`文件夹路径，运行结束后将高分辨率深度图文件夹命名为`data_all_HR_x4`，低分辨率深度图文件夹命名为`data_all_LR_x4`，并在`data`文件夹下新建`PMBA`文件夹，将上述文件夹放入

在测试数据集中，图片文件是以mat文件格式存储的，执行`data/process_pmba/generate_test_data.py`脚本，生成`.png`格式的测试集

对于PMBANet，由于需要的图像块比较小，所以执行`data/process_pmba/process_pmba_data.py`脚本，将处理得到的深度图影像对按照`crop_size = 128`与`step = 64`进行切块


## 下载

处理好的数据集已上传至AI Studio平台，链接如下：https://aistudio.baidu.com/aistudio/datasetdetail/173618
