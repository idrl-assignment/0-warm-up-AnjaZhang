# warm-up

本次作业为热身题，目的是帮助大家熟悉 github classroom 的操作流程。

## 要求

- 符合 PEP 8 代码规范
- 将所需第三方 package 放到 `requirements.txt` 中
- 编写 `plot_matrix.py` 中 `TODO` 部分，使程序满足以下功能：
  1. `generate_matrix(m, n)` 生成 m 行 n 列的二值**随机矩阵**（每个元素随机为 0 或 1）
  2. `save_matrix(matrix, file_name)` 将 `matirx` 保存成图片形式
- 通过单元测试，系统会赋予相应分值；可本地执行 `pytest` 查看测试结果
- 个人作业仓库在每次 push 后会执行自动评分，并自动生成带反馈结果的 pull request，其中包含生成的图片结果（待执行结束后）

## 评分标准

|要点|分值|
|:---:|:---:|
|代码规范|2|
|generate_matrix()|4|
|save_matrix()|2|
|总分|8|