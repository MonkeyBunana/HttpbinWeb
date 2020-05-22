import requests
from Common.read_log import LogPage

def get_request(url, data=None, headers=None):
    res = requests.get(url, data, headers)
    return res

def post_request(url, data, headers=None):
    res = requests.get(url, data, headers)
    return res

def delete_request(url, data=None, headers=None):
    res = requests.get(url, data)
    return res

def put_request(url, data, headers=None):
    pass

def send_request(method, url, data=None, headers=None):
    log = LogPage('request')
    try:
        log.info(headers)
        if method == 'GET':
            return get_request(url, data, headers)
        elif method == 'POST':
            return post_request(url, data, headers)
        elif method == 'DELETE':
            return delete_request(url, data, headers)
        elif method == 'PUT':
            return put_request(url, data, headers)
        else:
            log.info(method + ' not found')
    except Exception as e:
        log.info(e)