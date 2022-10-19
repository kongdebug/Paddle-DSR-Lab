
简体中文 | [English](./README.md)
# Paddle-DSR-Lab


```shell
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
