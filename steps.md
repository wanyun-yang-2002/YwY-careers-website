# [Web Development with Python Tutorial – Flask & Dynamic Database-Driven Web Apps](https://www.youtube.com/watch?v=yBDHkveJUf4&t=2217s)

## Step1
下载安装[Flask](https://flask.palletsprojects.com/en/2.2.x/installation/)
1. 创建环境
    ```python
    > mkdir myproject
    > cd myproject
    > py -3 -m venv venv
    ```
2. 激活环境
   ```python
   > venv\Scripts\activate
   ```
3. 安装Flask
   ```python
   $ pip install Flask
   ```
## 前端页面
   1. 按照教程代码，无法把Apply的button放到最右边，仔细查看[文档](https://getbootstrap.com/docs/5.3/layout/columns/#how-they-work)后找到解决办法
      ```html
      <div class="row">
         <!-- 左边 -->
         <div class="col-auto me-auto">.col-auto .me-auto</div>
         <!-- 右边 -->
         <div class="col-auto">.col-auto</div>
      </div>
      ```
## 数据库
在线数据库网站：https://planetscale.com/
下载MySQL Workbench：https://dev.mysql.com/downloads/workbench/
1. 通过在线数据库中新建数据库，再将MySQL Workbench与在线数据库建立连接
2. MySQL Workbench中，可以通过SQL语句进行数据插入等操作，也可以直接向表中输入数据
3. 新建文件database.py
   - 安装 sqlalchemy 
     ```python
     pip install sqlalchemy 
     #建议使用清华源镜像
     pip install sqlalchemy -i https://pypi.tuna.tsinghua.edu.cn/simple 
     ```
   - py文件连接数据库
     ```python
      from sqlalchemy import create_engine
      engine = create_engine("mysql+pymysql://username:password@host/database?charset=utf8mb4")
     ```
4. 把sqlalchemy row变成python中的字典形式
   看着教程直接用的```dict()```，自己运行时却不断报错，经google搜索，在stackoverflow上看到了如下回答：
   ```python
   for row in resultproxy:
      row_as_dict = row._mapping  # SQLAlchemy 1.4 and greater
      # row_as_dict = dict(row)  # SQLAlchemy 1.3 and earlier
   ```
   原来是不同版本的SQLAlchemy对应的方法不一样，于是采用```row._mapping```，成功运行！
5. 隐私安全保护
   由于教程是在在线IDE编写代码的，所以可以直接创建一个系统环境变量（system environment variables）里的 secrets ，用于保护连接数据库时的账号密码。
   我直接用的pycharm，这一步暂时不知道怎么做，所以跳过了这一步。