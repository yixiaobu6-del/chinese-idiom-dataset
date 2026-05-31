# Chinese Idiom Dataset - 中文成语歇后语数据集

> 结构化的中文成语和歇后语数据集，适用NLP、教育应用、文化研究

---

## Features / 功能特点

| 功能 | 说明 |
|------|------|
| 格式规范 | 统一的 JSON 结构，字段完整 |
| 数据丰富 | 成语含拼音、释义、出处、例句 |
| 歇后语数据 | 谜面、谜底、解析说明、分类标签 |
| 搜索标签 | 支持按分类标签（动物、数字等）搜索 |
| 命令行检索 | 开箱即用的 CLI 搜索工具 |
| Python 模块 | 可直接 import 使用 |
| UTF-8编码 | 全中文数据，兼容各类编程环境 |

## Installation / 安装

```bash
# 克隆仓库
git clone https://github.com/yourusername/chinese-idiom-dataset.git

cd chinese-idiom-dataset

# Python 3.6+ 即可运行
python scripts/search.py --help
```

## Usage / 使用方法

### 命令行检索

```bash
# 搜索成语
python scripts/search.py "成语"

# 搜索歇后语
python scripts/search.py "歇后语"

# 仅搜索成语
python scripts/search.py --type idiom

# 仅搜索歇后语
python scripts/search.py --type xiehouyu

# 按标签搜索
python scripts/search.py --tag "动物"
```

### 数据结构

#### 成语数据 (idioms_sample.json)

| 字段 | 类型 | 说明 | 示例 |
|------|------|------|------|
| id | string | 唯一标识符 | "iy_001" |
| idiom | string | 成语 | "画蛇添足" |
| pinyin | string | 拼音 | "huà shé tiān zú" |
| meaning | string | 释义 | "比喻做了多余的事，反而不好" |
| source | string | 出处/典故 | "《战国策·齐策》" |
| example | string | 例句 | "这篇文章已经写得很完整了，再加内容就是画蛇添足。" |
| tags | array[string] | 分类标签 | `["动物", "贬义"]` |

#### 歇后语数据 (xiehouyu_sample.json)

| 字段 | 类型 | 说明 | 示例 |
|------|------|------|------|
| id | string | 唯一标识符 | "ix_001" |
| riddle | string | 谜面（前半句） | "外甥打灯笼" |
| answer | string | 谜底（后半句） | "照旧（舅）" |
| explanation | string | 解析说明 | "利用谐音双关" |
| category | string | 分类 | "谐音" |

### Python 模块使用示例

```python
import json

# 加载成语数据
with open('data/idioms_sample.json', 'r', encoding='utf-8') as f:
    idioms = json.load(f)

# 加载歇后语数据
with open('data/xiehouyu_sample.json', 'r', encoding='utf-8') as f:
    xiehouyu = json.load(f)

# 搜索含"马"字的成语
horse_idioms = [i for i in idioms if '马' in i['idiom']]
print(f"含\"马\"字的成语有 {len(horse_idioms)} 条")

# 按标签过滤动物相关成语
animal_idioms = [i for i in idioms if '动物' in i.get('tags', [])]
print(f"动物类成语有 {len(animal_idioms)} 条")
```

## Contributing / 贡献

参见 [CONTRIBUTING.md](CONTRIBUTING.md)

欢迎贡献：
- 补充成语和歇后语数据
- 改进搜索脚本
- 添加更多分类标签
- 报告数据错误

## License / 许可证

MIT License - 参见 [LICENSE](LICENSE)

---

> 版本：1.0.0 | 更新日期：2026-05-30