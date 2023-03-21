# [Web Development with Python Tutorial – Flask & Dynamic Database-Driven Web Apps](https://www.youtube.com/watch?v=yBDHkveJUf4&t=2217s)

## Step1
下载安装[Flask](https://flask.palletsprojects.com/en/2.2.x/installation/)
1. 创建环境
    ```
    > mkdir myproject
    > cd myproject
    > py -3 -m venv venv
    ```
2. 激活环境
   ```
   > venv\Scripts\activate
   ```
3. 安装Flask
   ```
   $ pip install Flask
   ```

## 数据库
在线数据库网站：https://planetscale.com/
下载MySQL Workbench：https://dev.mysql.com/downloads/workbench/
1. 通过在线数据库中新建数据库，再将MySQL Workbench与在线数据库建立连接
2. MySQL Workbench中，可以通过SQL语句进行数据插入等操作，也可以直接向表中输入数据
3. 新建文件database.py
   - 安装 sqlalchemy 
     ```
     pip install sqlalchemy 
     pip install sqlalchemy -i https://pypi.tuna.tsinghua.edu.cn/simple #建议使用清华源镜像
     ```
   - py文件连接数据库
     ```
      from sqlalchemy import create_engine
      engine = create_engine("mysql+pymysql://username:password@host/database?charset=utf8mb4")
     ```
