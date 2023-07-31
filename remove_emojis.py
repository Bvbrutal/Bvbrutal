import re

def remove_special_emojis(markdown_text):
    # 定义表情包的正则表达式模式
    emoji_pattern = r':[a-zA-Z0-9_\-]+:'

    # 使用re.sub()函数删除所有匹配的表情包
    cleaned_text = re.sub(emoji_pattern, '', markdown_text)

    return cleaned_text

if __name__ == '__main__':
    import sys

    # 从标准输入中读取README.md的内容
    readme_content = sys.stdin.read()

    # 删除特殊表情包
    cleaned_content = remove_special_emojis(readme_content)

    # 输出删除表情包后的文本
    print(cleaned_content)
