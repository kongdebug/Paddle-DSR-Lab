# PMBANet Dataset Preparation Instructions

## Brief Introduction

As the PMBA repo does not provide the relevant data, and emails to the authors were not answered, the three datasets `Middlebury dataset` / `MPI Sintel dataset` and `synthetic New Tsukuba dataset`, which are consistent with WAFP-Net, were used.

## Processing flow

Consistent with the raw data used in [WAFP-Net data processing](docs/en_US/datasets/WAFP-Net-Data.md), go to this project folder and download the 2 dataset zip files: `WAFP_data.zip`, `WAFP_test_data.zip` Unzip and place the `data_ all` folder (containing 133 depth maps) and the `test_data` folder (containing 4 test data) into the following locations.

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

**NOTE**: WAFP-Net downsamples and adds noise to the high-resolution depth map before upsampling to the size of the high-resolution depth map and generating an .h5 file as the training set. This process is not consistent with the data processing required for networks such as PMBANet, RCAN, DRN, etc., so only the operation of downsampling and adding noise is retained to generate the corresponding low-resolution depth map.

Using the `matlab` software, execute the `data/process_pmba/generate_train_LR.m` script to generate the high-resolution and low-resolution depth map pairs of the training data, note that when using it, modify the path of the `data_all` folder in the script, and after running, name the high-resolution depth map folder as `data_ all_HR_x4` and the low-resolution depth map folder as `data_all_LR_x4`, and create a new `PMBA` folder under the `data` folder, and put the above folders into this folder.

In the test data set, the image files are stored in mat file format, execute the `data/process_pmba/generate_test_data.py` script to generate the test set in `.png` format.

For PMBANet, as the required image blocks are relatively small, the `data/process_pmba/process_pmba_data.py` script is executed to slice the resulting depth map image pairs according to `crop_size = 128` with `step = 64`


## Downloads

The processed dataset has been uploaded to the AI Studio platform at the following link: https://aistudio.baidu.com/aistudio/datasetdetail/173618
