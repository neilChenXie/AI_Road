
## 背景
此问题是一个python脚本的处理HTML文件的逻辑问题。表格 rowspan 导致列错位。用`minimax-m2.5`一下午都没有debug出根本问题，切换`claude opus`一次就debug好了，所以记录用于测试其他模型。

## 安装依赖

```bash
source ~/.venv/bin/activate

pip install -r requirements.txt
```

## 执行脚本

```bash
source ~/.venv/bin/activate

python html_to_markdown.py test-case-复杂表格.html
```

## prompt提示词

```bash
通过 html_to_markdown.py 转化 《test-case-复杂表格.html》，结果中的表格有些问题：

| 返回类型 | 返回值 |  |  |  |  |
| int | 0 |  |  |  |  |
| -1 |  |  |  |  | 加载套接字库失败 |

应该是：
| 返回类型 | 返回值 |  |  |  | 返回值说明 |
| int | 0 |  |  |  | 加载套接字库成功，库版本2.2 |
| int | -1 | |  |  | 加载套接字库失败 |
```