# Markdown本地Web服务搭建方法

[**MarkDown中插入数学公式**](https://weilai5432.github.io/2017/01/11/MathJax-%E5%9C%A8MarkDown%E4%B8%AD%E6%8F%92%E5%85%A5%E6%95%B0%E5%AD%A6%E5%85%AC%E5%BC%8F/)

$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$

## 这里展示一下起步的 HTML

创建一个文件 `index.html`，并用编辑器将下边的文字填入这个文件。

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>HELLO</title>
    <link href="//cdn.bootcss.com/skeleton/2.0.4/skeleton.min.css" rel="stylesheet">
    <script src="//cdn.bootcss.com/jquery/1.11.3/jquery.min.js"></script>
  </head>
  <body>
    <h1>你好，世界！</h1>
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
