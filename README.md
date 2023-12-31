# iOS Pendo笔记转CSV工具

这个工具的主要目的是转换由iOS Pendo软件导出的笔记文本到CSV文件格式，从而方便用户备份和导入到其他软件。

## 背景

iOS Pendo是一个非常受欢迎的笔记应用，但其导出功能产生的文本格式可能不适用于所有场景。为了解决这个问题，我们创建了这个工具，能够将Pendo导出的笔记文本转换为更加通用的CSV格式。

## 使用方法

1. 将您的Pendo笔记导出为文本文件，并确保该文件名为“文本.txt”。
2. 将此文本文件放在与Python脚本相同的目录下。
3. 运行Python脚本。脚本会读取文本文件并生成一个名为“notes.csv”的CSV文件。
4. 您现在可以打开和查看CSV文件，或将其导入到其他支持CSV格式的应用中。

## 代码结构

- `is_date_type_line`: 一个辅助函数，用于判断给定的行是否表示日期和类型。
- 主脚本部分首先读取文本文件，提取每个笔记的详细信息，并将这些信息保存为CSV文件。

## 依赖

- Python 3.x

## 开发者和贡献

此工具由Jellzone开发。如果您在使用过程中遇到任何问题，或想要提供反馈和建议，请随时创建一个GitHub issue。
