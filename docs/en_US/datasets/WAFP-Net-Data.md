# WAFP-Net Dataset Preparation Instructions

## Brief Introduction

The data used combines the `Middlebury dataset` / `MPI Sintel dataset` and the `synthetic New Tsukuba dataset`.

## Processing flow

Execute the following command, go to this project folder, download the 2 dataset zip packages: `WAFP_data.zip`, `WAFP_test_data.zip` Unzip and place the `data_all` folder (containing 133 depth maps) and the `test_data` folder (containing 4 test data) into the following locations.

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

The depth map in `data_all` needs to be downsampled and then the depth-dependent Gaussian noise is added to the low-resolution training data as θ(d) = N(0, δ/d), where δ = 651 and d denotes the depth value of each pixel in the DL. Using the `matlab` software, execute the `data/process_wafp/generate_train_noise.m` script to generate the training data `train_depth_x4_noise.h5`, taking care to modify the `data_all` folder path in the script when using.


## Downloads

The processed training set `train_depth_x4_noise.h5` has been uploaded to the AI Studio platform at the following link: https://aistudio.baidu.com/aistudio/datasetdetail/154330