#!/usr/bin/env python3
"""
Word HTML 转 Markdown
处理 Word 另存为 HTML 产生的文件
"""

from bs4 import BeautifulSoup
import re
import sys
import os


def convert_table(table):
    """转换表格为Markdown格式，处理colspan和rowspan"""
    tbody = table.find('tbody') or table
    trs = tbody.find_all('tr')
    if not trs:
        return ""

    # 解析原始表格结构
    raw_cells = []  # 原始单元格数据

    for tr in trs:
        row_data = []
        col_idx = 0
        for td in tr.find_all(['td', 'th']):
            colspan = int(td.get('colspan', 1))
            rowspan = int(td.get('rowspan', 1))
            text = td.get_text().strip()

            while len(row_data) < col_idx:
                row_data.append(None)

            row_data.append({'text': text, 'rowspan': rowspan, 'colspan': colspan})
            col_idx += colspan

        raw_cells.append(row_data)

    # 计算最大列数
    max_cols = max(len(row) for row in raw_cells) if raw_cells else 0

    # 填充到矩形
    for row in raw_cells:
        while len(row) < max_cols:
            row.append(None)

    # 构建单元格位置映射表，处理rowspan
    # cell_at[row][col] = cell_info 或 None
    # 先填充所有单元格到临时结构
    temp_grid = [[None] * max_cols for _ in range(len(raw_cells))]

    for row_idx, row in enumerate(raw_cells):
        col_idx = 0
        for cell in row:
            if cell:
                colspan = cell.get('colspan', 1)
                rowspan = cell.get('rowspan', 1)

                # 将单元格信息填充到grid中
                for r in range(rowspan):
                    for c in range(colspan):
                        if row_idx + r < len(temp_grid) and col_idx + c < max_cols:
                            temp_grid[row_idx + r][col_idx + c] = cell

                col_idx += colspan
            else:
                col_idx += 1

    # 生成最终行
    result_rows = []
    for row_idx in range(len(raw_cells)):
        final_row = []
        col_idx = 0

        while col_idx < max_cols:
            cell = temp_grid[row_idx][col_idx] if row_idx < len(temp_grid) and col_idx < max_cols else None

            if cell:
                text = cell['text']
                colspan = cell.get('colspan', 1)
                final_row.append(text)
                # colspan > 1时，后续列留空
                for _ in range(colspan - 1):
                    final_row.append('')
                col_idx += colspan
            else:
                final_row.append('')
                col_idx += 1

        # 填充到max_cols
        while len(final_row) < max_cols:
            final_row.append('')
        result_rows.append(final_row[:max_cols])

    # 生成Markdown表格
    md = []
    md.append("| " + " | ".join([""] * max_cols) + " |")
    md.append("|" + "|".join(["---" for _ in range(max_cols)]) + "|")
    for row in result_rows:
        md.append("| " + " | ".join(row) + " |")

    return "\n".join(md) + "\n"

    # 生成 Markdown 表格
    md = []
    # 使用空表头（因为这种Word表格没有标准表头）
    md.append("| " + " | ".join([""] * max_cols) + " |")
    md.append("|" + "|".join(["---" for _ in range(max_cols)]) + "|")
    for row in final_rows:
        md.append("| " + " | ".join(row) + " |")

    return "\n".join(md) + "\n"

    # 生成 Markdown 表格
    if not rows:
        return ""

    md = []
    # 如果第一行只有1列且内容很短，可能不是数据行
    if rows and len(rows[0]) == 1 and len(rows[0][0]) < 15:
        # 第一行是表头
        headers = rows[0]
        rows = rows[1:]
        md.append("| " + " | ".join(headers) + " |")
        md.append("|" + "|".join(["---" for _ in range(len(headers))]) + "|")
    else:
        # 没有表头，使用空表头
        md.append("| " + " | ".join([""] * max_cols) + " |")
        md.append("|" + "|".join(["---" for _ in range(max_cols)]) + "|")

    # 数据行
    for row in rows:
        md.append("| " + " | ".join(row) + " |")

    return "\n".join(md) + "\n"


def convert_list(lst, ordered=False, level=0):
    """转换列表为Markdown格式"""
    result = []
    items = lst.find_all('li', recursive=False)

    for i, item in enumerate(items):
        indent = "  " * level
        if ordered:
            prefix = f"{indent}{i+1}. "
        else:
            prefix = f"{indent}- "

        # 处理列表项内容
        text = item.get_text().strip()
        if text:
            result.append(prefix + text)

    return "\n".join(result) + "\n"


def convert_element(elem):
    """递归转换HTML元素"""
    result = []
    for child in elem.children:
        if child.name is None:
            text = str(child).strip()
            if text:
                result.append(text)
        elif child.name == 'p':
            # 段落之间增加空行（两个换行符）
            para_text = convert_element(child).strip()
            if para_text:
                result.append(para_text + "\n\n")
        elif child.name == 'br':
            result.append("\n")
        elif child.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(child.name[1])
            text = child.get_text().strip()
            # 标题后增加空行
            result.append("#" * level + " " + text + "\n\n")
        elif child.name in ['b', 'strong']:
            text = child.get_text().strip()
            if text:
                result.append(f"**{text}**")
        elif child.name in ['i', 'em']:
            text = child.get_text().strip()
            if text:
                result.append(f"*{text}*")
        elif child.name == 'table':
            # 表格后增加空行
            result.append(convert_table(child) + "\n")
        elif child.name in ['ul', 'ol']:
            ordered = child.name == 'ol'
            # 列表后增加空行
            result.append(convert_list(child, ordered) + "\n")
        elif child.name == 'div':
            result.append(convert_element(child))
        elif child.name == 'span':
            text = convert_element(child)
            if text.strip():
                result.append(text)
        else:
            result.append(convert_element(child))
    return "".join(result)


def html_to_markdown(html_path, md_path=None):
    """
    将 Word 导出的 HTML 文件转换为 Markdown

    Args:
        html_path: HTML 文件路径
        md_path: 输出 Markdown 路径，默认为同名 .md 文件
    """
    if not os.path.exists(html_path):
        print(f"错误: 文件不存在: {html_path}")
        return False

    if md_path is None:
        md_path = html_path.replace('.html', '.md').replace('.htm', '.md')

    # 1. 读取 HTML（尝试多种编码）
    html = None
    for encoding in ['gb2312', 'gbk', 'utf-8']:
        try:
            with open(html_path, "r", encoding=encoding, errors="ignore") as f:
                html = f.read()
            print(f"使用编码: {encoding}")
            break
        except Exception as e:
            continue

    if html is None:
        print("错误: 无法读取文件，编码不支持")
        return False

    # 2. 解析并转换
    soup = BeautifulSoup(html, 'lxml')

    # 移除无用标签
    for tag in soup(["script", "style", "meta", "link"]):
        tag.decompose()

    # 3. 执行转换
    body = soup.find('body')
    content = convert_element(body) if body else convert_element(soup)

    # 4. 清理 Word 标记
    content = re.sub(r'\[if !supportLists\]', '', content)
    content = re.sub(r'\[endif\]', '', content)
    content = re.sub(r'StartFragment|EndFragment', '', content)
    # 修复标题格式（编号与加粗之间加空格）
    content = re.sub(r'^(\d+(?:\.\d+)*)(\*\*)', r'\1 \2', content, flags=re.MULTILINE)
    # 清理空的加粗标记 ****
    content = re.sub(r'\*\*\*\*', '', content)
    # 清理多余空行（保留段落间的单个空行，但清理超过两个的连续空行）
    content = re.sub(r'\n{5,}', '\n\n\n\n', content)
    # 清理行首行尾空白
    content = '\n'.join(line.rstrip() for line in content.split('\n'))

    # 5. 保存
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[OK] 转换完成: {md_path}")
    print(f"[OK] 文件大小: {len(content)} 字符")
    return True


def main():
    if len(sys.argv) < 2:
        print("用法: python html_to_markdown.py <html文件路径> [输出md文件路径]")
        print("示例: python html_to_markdown.py document.html")
        print("      python html_to_markdown.py document.html output.md")
        sys.exit(1)

    html_path = sys.argv[1]
    md_path = sys.argv[2] if len(sys.argv) > 2 else None

    success = html_to_markdown(html_path, md_path)
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
