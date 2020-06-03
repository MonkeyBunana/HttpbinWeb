import requests


def get_request(url, data=None, headers=None):
    res = requests.get(url=url, data=data, headers=headers)
    return res

def post_request(url, data, headers=None):
    res = requests.post(url=url, data=data, headers=headers)
    return res

def del_request(url, data=None, headers=None):
    res = requests.delete(url, data=data)
    return res

def put_request(url, data, headers=None):
    pass

def send_request(method, url, data=None, headers=None):
    try:
        if headers:
            if method == "GET":
                return get_request(url, data, headers=headers)
            if method == "POST":
                return post_request(url, data=data, headers=headers)
            if method == "DELETE":
                return del_request(url, data=data, headers=headers)
            if method == "PUT":
                return put_request(url, data=data, headers=headers)
        else:
            pass
    except Exception as e:
        pass