# 运行Easyweb节点
您可以在您自己的服务器上通过 Easyweb节点 运行您的 Easyweb应用。

#步骤
1. 在 http://easyweb.fun 上创建的你应用
2. 在 http://easyweb.fun/me 的 应用设置 中把 网站部署在外 设为True
3. 下载该repo中的servo文件夹, 并运行 python3 -m servo.update
    输入您的应用名和密码后,将开始下载,下载完后应该看到除了servo文件夹还有web和user_db两个文件夹
4. 运行 python3 -m servo 
   输入本地端口后 Easyweb节点 将开始运行
   当别人访问 http://easyweb.fun/<your_app> 时，请求和数据的处理将会在您的 Easyweb节点 上运行
