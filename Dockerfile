# 使用官方 Python 3.12 镜像
FROM python:3.12

COPY README.md /app/README.md

# 设置工作目录
WORKDIR /app

# 安装 Poetry（如果已安装，可以省略）
RUN pip install poetry

# 复制 Poetry 配置文件
COPY pyproject.toml poetry.lock ./

# 安装依赖
RUN poetry config virtualenvs.create false && poetry install  --no-root --no-interaction --no-ansi

# 复制 Django 项目代码
COPY . .


# 运行 Django 服务器（可根据需要修改）
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

COPY startup.sh /app/
RUN chmod +x /app/startup.sh

# 使用脚本启动容器
CMD ["/app/startup.sh"]
