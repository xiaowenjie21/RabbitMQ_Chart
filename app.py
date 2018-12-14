import jinja2, aiohttp_jinja2
from aiohttp.web import run_app
import asyncio
from aiohttp_session import setup
import base64
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from router import WebRoute
from config import *
from aiohttp import web
from consume import *

async def start_background_tasks(app):
    """后台任务 需要改进"""
    recv_serverid = MQ_CONFIG.get("serverid")
    # threading.Thread(target = RabbitComsumer.run, args = (recv_serverid,)).start()
    threading.Thread(target = RabbitPublisher.run, args = (recv_serverid, )).start()

class WorkerPool:
    '''web工作组'''

    def __init__(self, loop):
        self.loop = asyncio.get_event_loop() or loop
        self.webRouter = WebRoute(loop=loop)

    def init(self):
        '''Web应用初始化函数
        @session中间件安装
        @static静态文件的安装
        @jinja2模板路径的安装
        @router的安装
        '''
        app = web.Application()
        fernet_key = 'yj5e_WBa1I650aaW8Wru0uKjDkAF1Trglk5ee83wGP8='
        secret_key = base64.urlsafe_b64decode(fernet_key)
        setup(app, EncryptedCookieStorage(secret_key))

        # 添加静态文件目录
        app.router.add_static('/static/', path=str(PROJECT_ROOT / 'static'), name='static')
        # 安装模板
        aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(template_dir))
        # 安装路由 .base <基本路由> _. < 其他路由>
        self.webRouter.base(app)

        return app


try:

    loop = asyncio.get_event_loop()
    wp = WorkerPool(loop=loop)
    app = wp.init()
    app.on_startup.append(start_background_tasks)
    run_app(app, host='127.0.0.1', port=80)

except KeyboardInterrupt:
    sys.stderr.flush()
