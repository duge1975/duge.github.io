# config.py
# 核心配置（仅需修改这里的内容，其他文件无需动）
CONFIG = {
    # 个人信息
    "site_name": "duge1975",          # 网页名称（浏览器标签显示）
    "site_title": "Blog of duge1975", # 首页大标题
    "author": "duge1975",             # 作者名
    "copyright_year": "2026",         # 版权年份
    "footer_text": f"© {2026} duge1975 · 基于Python + Markdown + GitHub Pages构建", # 页脚文案
    
    # 路径配置（无需修改）
    "posts_dir": "src/posts/",        # Markdown文章目录
    "templates_dir": "src/templates/",# HTML模板目录
    "static_dir": "src/static/",      # 静态资源目录
    "output_dir": "docs/"             # 生成的静态页面输出目录
}