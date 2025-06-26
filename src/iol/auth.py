import datetime as dt
import requests as req
from .constants import DATE_FORMAT, API_URL


AUTH_AP = API_URL + 'token'


def _local_to_gmt(d):
    return d + dt.timedelta(hours=3)


def _gmt_to_local(d):
    return d - dt.timedelta(hour=3)


def date_from_str(s):
    return dt.datetime.strptime(s, DATE_FORMAT)


def date_to_str(d):
    return d.strftime(DATE_FORMAT) + 'GMT'


class Auth:
    """The authorisation we receive from IOL."""

    def __init__(self, js):
        """Builds an Auth from a json."""
        self.access_token = js['access_token']
        self.token_type = js['token_type']
        self.expires_in = js['expires_in']
        self.refresh_token = js['refresh_token']
        self.issued = date_from_str(js['.issued'])
        self.expires = date_from_str(js['.expires'])
        self.refresh_expires = date_from_str(js['.refreshexpires'])

    def is_access_valid(self):
        return _local_to_gmt(dt.datetime.today()) < self.expires

    def is_refresh_valid(self):
        return _local_to_gmt(dt.datetime.today()) < self.refresh_expires

    def to_json(self):
        return {'access_token': self.access_token,
                'token_type': self.token_type,
                'expires_in': self.expires_in,
                'refresh_token': self.refresh_token,
                '.issued': date_to_str(self.issued),
                '.expires': date_to_str(self.expires),
                '.refreshexpires': date_to_str(self.refresh_expires)}


def request_new_auth(username, password):
    """Request authorisation for given username and password."""

    params_ = {'username': username,
               'password': password,
               'grant_type': 'password'}
    header_ = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = req.post(AUTH_AP, data=params_, headers=header_)
    if r.status_code != 200:
        print(r.text)
        r.raise_for_status()
    return Auth(r.json())


def request_refresh_auth(auth):
    """Request a refresh of the authorisation."""

    data_ = {'refresh_token': auth.refresh_token,
             'grant_type': 'refresh_token'}
    r = req.post(AUTH_AP, data=data_)
    if r.status_code != 200:
        print(r.text)
        r.raise_for_status()
    return Auth(r.json())
