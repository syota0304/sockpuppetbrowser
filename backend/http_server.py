import psutil
from aiohttp import web
from loguru import logger

async def handle_http_request(request, stats):
    svmem = psutil.virtual_memory()
    data = {
        'active_connections': stats['connection_count'],
        'connection_count_total': stats['connection_count_total'],
        'mem_use_percent': svmem.percent,
        'special_counter_len': len(stats['special_counter'])
    }

    return web.json_response(data, content_type='application/json')


async def start_http_server(host, port, stats):
    app = web.Application()
    app.router.add_get('/stats', lambda req: handle_http_request(req, stats))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host, port)
    await site.start()
    logger.success(f"HTTP stats info server running at http://{host}:{port}/stats")

