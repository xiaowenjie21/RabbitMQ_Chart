import aiohttp_jinja2, aiohttp
from aiohttp import web
import asyncio
from aiohttp.abc import AbstractView
from functools import wraps
import time
from aiohttp_session import get_session

def expires(func):
    @asyncio.coroutine
    @wraps(func)
    async def expires(*args):
        if asyncio.iscoroutinefunction(func):
            coro = func
        else:
            coro = asyncio.coroutine(func)

        if isinstance(args[0], AbstractView):
            request = args[0].request
        else:
            request = args[-1]

        # session过期控制
        session = await get_session(request)
        if session.get('last_visit'):
            last_time = session.get('last_visit')
            if time.time() - last_time > 600:
                session.invalidate()
                return web.Response(text = '会话过期，请重新登录')

        context = await coro(*args)
        if isinstance(context, web.StreamResponse):
            return context

    return expires


class WebRoute:
    #首页与退出的路由
    def __init__(self, loop):
        self.loop = loop


    def base(self, app):
        '''安装路由'''
        app.router.add_get('/', self.index)
        app.router.add_get('/line', self.line)
        app.router.add_get('/bar', self.bar)

    async def bar(self, request):
        session = await get_session(request)
        return aiohttp_jinja2.render_template('bar.html', request, {'title': '条形chart', 'session': session})

    async def line(self, request):
        session = await get_session(request)
        return aiohttp_jinja2.render_template('line.html', request, {'title': '线性chart', 'session': session})


    async def index(self, request):
        session = await get_session(request)
        return aiohttp_jinja2.render_template('index.html', request, {'title': 'dc.js结合RabbitMq的动态及实时图表', 'session': session})


    async def delete(self, request):
        session = await get_session(request)
        session.clear()
        return web.Response(text = 'success')