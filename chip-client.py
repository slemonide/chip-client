import click
from dotenv import load_dotenv
from os.path import expanduser
import os
import requests
from texttable import Texttable

class ChipClient(object):
    def __init__(self, api_url, api_token):
        load_dotenv(expanduser("~/.local/share/chip-proxy"), override=True)

        self.api_url = api_url or 'http://localhost:8001/api'

        proxy_api_token = api_token or os.environ['CONFIGPROXY_AUTH_TOKEN']
        self.headers = {
            'Authorization': 'token %s' % proxy_api_token,
            'Content-Type': 'application/json',
            'accept': 'application/json'
        }

@click.group()
@click.pass_context
@click.option("--api-url", help='chip-proxy address')
@click.option("--api-token", help='chip-proxy API token')
def chip_client(ctx, api_url, api_token):
    ctx.obj = ChipClient(api_url, api_token)

@chip_client.command()
@click.pass_obj
def ls(cc):
    '''List available routes'''

    r = requests.get(cc.api_url + '/routes', headers=cc.headers)
    r.raise_for_status()
    routes = r.json()

    #click.echo(str(routes))

    table_rows = []

    table_rows.append(["Path", "Port", "Last Activity"])

    for route_item in routes.items():
        route = route_item[0]
        route_data = route_item[1]
        route_target = route_data['target']
        route_last_activity = route_data['last_activity']

        table_rows.append([route, route_target, route_last_activity])

    table = Texttable()
    table.set_deco(Texttable.HEADER)
    table.set_cols_width([40,35,25])
    table.set_cols_dtype(['t', 't', 't'])
    table.add_rows(table_rows)
    
    click.echo(table.draw())
        

@chip_client.command()
@click.pass_obj
@click.argument('path')
@click.argument('port')
def add(cc, path, port):
    '''Add a new route'''

    r = requests.post(cc.api_url + '/routes/' + path, headers=cc.headers,
        json = {'target': "http://localhost:" + port})
    r.raise_for_status()

if __name__ == '__main__':
    chip_client()
