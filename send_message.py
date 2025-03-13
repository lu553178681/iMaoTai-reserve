import logging

import requests


def send_server_chan(sckey, title, desp):
    """
    server酱推送
    :param sckey: server酱推送的key
    :param title: 标题
    :param desp: 内容
    :return:
    """
    if sckey:
        url = f"https://sctapi.ftqq.com/{sckey}.send"
        data = {"title": title, "desp": desp}
        response = requests.post(url, data=data)
        if response.json()['data']['error'] == 'SUCCESS':
            logging.info('Server酱 Turbo版推送成功')
        else:
            logging.info('Server酱 Turbo版推送失败')
    else:
        logging.warning("server酱 KEY 没有配置,不推送消息")


def send_pushplus(token, title, content):
    if token is None:
        logging.warning("pushplus TOKEN 没有配置,不推送消息")
        return
    
    url = 'http://www.pushplus.plus/send'
    data = {
        "token": token,
        "title": title,
        "content": content
    }
    
    try:
        # 添加超时参数，设置连接超时和读取超时均为5秒
        response = requests.post(url, data=data, timeout=(5, 5))
        logging.info(f'pushplus 通知推送结果：{response.status_code, response.text}')
    except requests.exceptions.Timeout:
        logging.error("pushplus 推送服务请求超时")
    except Exception as e:
        logging.error(f"pushplus 推送失败: {e}")
