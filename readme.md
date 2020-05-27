# Markdown本地Web服务搭建方法

[**MarkDown中插入数学公式**](https://weilai5432.github.io/2017/01/11/MathJax-%E5%9C%A8MarkDown%E4%B8%AD%E6%8F%92%E5%85%A5%E6%95%B0%E5%AD%A6%E5%85%AC%E5%BC%8F/)

$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$

## 自动索引

运行 `python build.py` 自动搜索目录下所有*.md文件，并将索引写入`index.md`

## 模板HTML

创建一个文件 `index.html`，并用编辑器将下边的文字填入这个文件。

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <link href="//cdn.bootcss.com/skeleton/2.0.4/skeleton.css" rel="stylesheet">
    <script src="//cdn.bootcss.com/jquery/3.0.0-alpha1/jquery.js"></script>
    <script src="//cdn.bootcss.com/markdown-it/4.4.0/markdown-it.min.js"></script>
  </head>
  <body>
    <h1>Hello Markdown</h1>
  </body>
</html>
```

## 启动 HTTP 服务器

```shell
# python 2.*
$ python -m SimpleHTTPServer 8000
# python 3.*
$ python -m http.server 8000

Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

```
