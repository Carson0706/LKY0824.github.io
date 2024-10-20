import feedparser
import os
import re
from datetime import datetime

def get_news(feed_url, num):
    result = ""
    feed = feedparser.parse(feed_url)
    entries = feed["entries"][:num]
    
    for entry in entries:
        title = entry["title"]
        link = entry["link"]
        result += f"\n- [{title}]({link})\n"
    
    return result

def main():
    news_info = get_news("https://example.com/rss", 5)  # 替换为实际新闻源的RSS链接
    update_content = f"---start---\n\n## 今日新闻更新 ({datetime.now().strftime('%Y-%m-%d')})\n" + news_info + "\n---end---"

    with open("README.md", 'r', encoding='utf-8') as f:
        readme_content = f.read()

    new_readme_content = re.sub(r'---start---(.|\n)*---end---', update_content, readme_content)

    with open("README.md", 'w', encoding='utf-8') as f:
        f.write(new_readme_content)

if __name__ == "__main__":
    main()
