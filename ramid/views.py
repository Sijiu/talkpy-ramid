from pyramid.view import view_config

from ramid.fake_data import get_orders, get_greetings


@view_config(route_name='home', renderer="templates/mytemplate.pt")
def my_view(_):
    return {'project': 'ramid', "orders": get_orders(), "greetings": get_greetings()}
