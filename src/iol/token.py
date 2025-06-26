import datetime as dt
import requests as req

# IOL access points.
API_URL = 'https://api.invertironline.com/api/v2/'
TOKEN_AP = API_URL + 'token'
ACCOUNT_AP = API_URL + 'estadocuenta'
CAN_OPERATE_AP = API_URL + 'operar/CPD/PuedeOperar'
PORTFOLIO_ARG_AP = API_URL + 'portafolio/argentina'
PORTFOLIO_EEUU_AP = API_URL + 'portafolio/estados_Unidos'

# Date formats from IOL.
DATE_FORMAT = '%a, %d %b %Y %H:%M:%S %Z'


def _local_to_gmt(d):
    return d + dt.timedelta(hours=3)


def _gmt_to_local(d):
    return d - dt.timedelta(hour=3)


def _date_from_str(s):
    return dt.datetime.strptime(s, DATE_FORMAT)


def _date_to_str(d):
    return d.strftime(DATE_FORMAT) + 'GMT'


def _create_headers(token):
    return {'Accept': 'application/json',
            'Authorization': 'Bearer ' + token}


class Token:
    """The authorisation we receive from IOL.
    """

    def __init__(self, js):
        """Builds an Auth from a json."""
        self.access_token = js['access_token']
        self.token_type = js['token_type']
        self.expires_in = js['expires_in']
        self.refresh_token = js['refresh_token']
        self.issued = _date_from_str(js['.issued'])
        self.expires = _date_from_str(js['.expires'])
        self.refresh_expires = _date_from_str(js['.refreshexpires'])

    def is_access_valid(self):
        return _local_to_gmt(dt.datetime.today()) < self.expires

    def is_refresh_valid(self):
        return _local_to_gmt(dt.datetime.today()) < self.refresh_expires

    def to_json(self):
        return {'access_token': self.access_token,
                'token_type': self.token_type,
                'expires_in': self.expires_in,
                'refresh_token': self.refresh_token,
                '.issued': _date_to_str(self.issued),
                '.expires': _date_to_str(self.expires),
                '.refreshexpires': _date_to_str(self.refresh_expires)}


def request_new_token(username, password):
    """Request Auth for 'username' and 'password'."""
    rdata = 'username=' + username + '&password=' + password + '&grant_type=password'
    rhead = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = req.request('POST', TOKEN_AP, data=rdata, headers=rhead)
    return Token(r.json())
