# encoding:utf-8
import urllib

def test_1():
    config = {"company_id": "nsfocus", "user": "test_user", "passwd": 'test_user',
              "mobile": "13512341234", "code": "【绿盟科技】验证码5769"}
    send_content = urllib.urlencode(config)

    print send_content

if __name__ == '__main__':
    test_1()