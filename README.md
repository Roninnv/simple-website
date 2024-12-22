# 项目名称

这是一个简单的网站示例项目，包含前端和后端部分。以下是如何初始化和运行该项目的步骤。

## 后端

### 1. 安装依赖

在后端目录中，首先运行以下命令来安装依赖：

```bash
cd backend
pip3 install -r requirements.txt
```

### 2. 初始化数据

然后，进入后端目录并初始化数据：

```bash
python3 create_markdown.py
```

### 3. 启动后端

接下来，启动后端应用：

```bash
python3 main.py
```

## 前端

### 1. 安装依赖

在前端目录中，首先运行以下命令来安装依赖：

```bash
cd frontend
npm install
```

### 2. 生成 CSS

安装依赖后，运行以下命令来生成 CSS 文件（需要先安装 TailwindCSS）：

```bash
npx tailwindcss -i ./src/input.css -o ./src/output.css --watch
```

### 3. 启动前端开发环境

为了启动前端开发服务器，使用以下命令：

```bash
npm run dev
```

### 4. 打包前端

当准备好打包生产环境代码时，使用以下命令：

```bash
npm run build
```

## 环境要求

- Python 3.x
- Node.js 和 npm
