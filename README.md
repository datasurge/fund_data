# Fund data crawler project

获取新浪基金数据，包含历史数据、实时数据两个脚本文件。

## 脚本说明

爬取历史数据和实时数据采用不同抓取方式，采取独立抓取程序。

### sina_qdll.py

抓取实时数据脚本，目前只针对一只基金数据，使用Python运行即可。

依赖库为 `Xpath`、`requests` 。

### sina_qdll_history.py

抓取历史数据脚本，目前针对一只基金数据。由于历史数据采用JS 代码异步加载，所有采用自动化测试方式抓取。

#### 依赖

Selenium 是Python自动化工具，安装方式：

```
pip install selenium
```

同时浏览器需要安装插件，为selenium 提供支撑，开发环境使用 chrome 浏览器，插件为 ChromeDriver，[下载地址](https://chromedriver.chromium.org/downloads)。安装方式[参见](https://www.jianshu.com/p/dd848e40c7ad)。