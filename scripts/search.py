#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
成语歇后语检索工具

用法:
    python search.py "关键词"           # 在成语和歇后语中搜索
    python search.py "关键词" --type idiom     # 仅搜索成语
    python search.py "关键词" --type xiehouyu  # 仅搜索歇后语
    python search.py --tag "动物"              # 按标签搜索成语
    python search.py --list-tags              # 列出所有标签
    python search.py --category "谐音"         # 按类别搜索歇后语
"""

import json
import argparse
import sys
import os
from typing import List, Dict, Any


def load_data(filename: str) -> List[Dict[str, Any]]:
    """加载数据文件"""
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', filename)
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"错误: 找不到数据文件 {data_path}")
        return []
    except json.JSONDecodeError:
        print(f"错误: 数据文件格式错误 {data_path}")
        return []


def print_idiom(idiom: Dict):
    """格式化打印成语"""
    print("-" * 50)
    print(f"  【{idiom['idiom']}】({idiom['pinyin']})")
    print(f"  释义: {idiom['meaning']}")
    print(f"  出处: {idiom['source']}")
    print(f"  例句: {idiom['example']}")
    if idiom.get('tags'):
        print(f"  标签: {', '.join(idiom['tags'])}")
    print("-" * 50)
    print()


def print_xiehouyu(xiehouyu: Dict):
    """格式化打印歇后语"""
    print("-" * 50)
    print(f"  【{xiehouyu['riddle']}】")
    print(f"  谜底: {xiehouyu['answer']}")
    print(f"  解析: {xiehouyu['explanation']}")
    print(f"  分类: {xiehouyu['category']}")
    print("-" * 50)
    print()


def search_idioms(idioms: List[Dict], keyword: str) -> List[Dict]:
    """搜索成语"""
    results = []
    kw = keyword.lower()
    for item in idioms:
        if (kw in item.get('idiom', '').lower() or
            kw in item.get('meaning', '').lower() or
            kw in item.get('source', '').lower() or
            kw in item.get('example', '').lower()):
            results.append(item)
    return results


def search_xiehouyu(xiehouyu_list: List[Dict], keyword: str) -> List[Dict]:
    """搜索歇后语"""
    results = []
    kw = keyword.lower()
    for item in xiehouyu_list:
        if (kw in item.get('riddle', '').lower() or
            kw in item.get('answer', '').lower() or
            kw in item.get('explanation', '').lower()):
            results.append(item)
    return results


def list_tags(idioms: List[Dict]):
    """列出所有成语标签"""
    tag_set = set()
    for item in idioms:
        for tag in item.get('tags', []):
            tag_set.add(tag)

    print(f"\n共有 {len(tag_set)} 个标签:")
    print(", ".join(sorted(tag_set)))
    print()


def main():
    parser = argparse.ArgumentParser(
        description='成语歇后语检索工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
    python search.py "马"                       # 搜索含"马"的成语和歇后语
    python search.py "马" --type idiom          # 仅搜索成语
    python search.py "马" --type xiehouyu       # 仅搜索歇后语
    python search.py --tag "动物"               # 按标签搜索成语
    python search.py --category "谐音"          # 按类别搜索歇后语
    python search.py --list-tags                # 列出所有标签
        """
    )

    parser.add_argument('keyword', nargs='?', help='搜索关键词')
    parser.add_argument('--type', '-t', choices=['idiom', 'xiehouyu'], help='搜索类型')
    parser.add_argument('--tag', help='按标签搜索成语')
    parser.add_argument('--category', '-c', help='按类别搜索歇后语')
    parser.add_argument('--list-tags', action='store_true', help='列出所有标签')
    parser.add_argument('--limit', '-l', type=int, default=20, help='限制结果数量')

    args = parser.parse_args()

    # 加载数据
    idioms = load_data('idioms_sample.json')
    xiehouyu_list = load_data('xiehouyu_sample.json')

    has_results = False

    # 列出标签
    if args.list_tags:
        list_tags(idioms)
        return

    # 搜索或浏览
    if not args.keyword and not args.tag and not args.category:
        print(f"\n=== 成语搜索 ===")
        print(f"数据统计: 成语 {len(idioms)} 条, 歇后语 {len(xiehouyu_list)} 条")
        print(f"使用 python search.py --help 查看帮助")
        return

    # 按标签搜索成语
    if args.tag:
        print(f"\n=== 标签搜索: {args.tag} ===\n")
        results = [i for i in idioms if args.tag in i.get('tags', [])]
        print(f"找到 {len(results)} 条结果:\n")
        for item in results:
            if len(results) <= args.limit:
                print_idiom(item)
        has_results = True

    # 按类别搜索歇后语
    if args.category:
        print(f"\n=== 类别搜索: {args.category} ===\n")
        results = [x for x in xiehouyu_list if args.category in x.get('category', '')]
        print(f"找到 {len(results)} 条结果:\n")
        for item in results:
            if len(results) <= args.limit:
                print_xiehouyu(item)
        has_results = True

    # 关键词搜索
    if args.keyword:
        search_type = args.type or 'all'

        if search_type in ('all', 'idiom'):
            print(f"\n=== 成语搜索: {args.keyword} ===\n")
            idiom_results = search_idioms(idioms, args.keyword)
            print(f"找到 {len(idiom_results)} 条结果:\n")
            for item in idiom_results[:args.limit]:
                print_idiom(item)
            has_results = True

        if search_type in ('all', 'xiehouyu'):
            print(f"\n=== 歇后语搜索: {args.keyword} ===\n")
            xh_results = search_xiehouyu(xiehouyu_list, args.keyword)
            print(f"找到 {len(xh_results)} 条结果:\n")
            for item in xh_results[:args.limit]:
                print_xiehouyu(item)
            has_results = True

    if not has_results:
        print("未找到匹配结果。")


if __name__ == '__main__':
    main()