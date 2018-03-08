import asyncio

from sanic import Sanic, response

from clients import run_requests


app = Sanic()


@app.route('/')
def test(request):
    asyncio.ensure_future(run_requests())
    return response.json({
        'hello': 'world',
        'args': request.args,
        'raw_args': request.raw_args,
        'query_string': request.query_string
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
