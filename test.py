from Common.request_template import send_request

def test_send_request():
    url = 'http://127.0.0.1:6001/get'
    headers = {
        "X-Token": "0a6db4e59c7fff2b2b94a297e2e5632e"
    }
    res = send_request("GET", url, headers=headers)
    print(res.json())

if __name__ == "__main__":
    test_send_request()