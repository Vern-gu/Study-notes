# coding:utf8

import re
from socket import *
from multiprocessing import Process


# 设置静态文件根目录
ROOT_DIR = "c:/users/vern/Desktop/python"


def recv_request(clSocket):
    """处理客户端请求"""
    response_headers = "Sever: My sever\r\n"
    # 浏览器传输来的数据也是byte格式
    request = clSocket.recv(1024).decode("utf-8")
    request_lines = request.splitlines()
    for lines in request_lines:
        print("request:", lines)
    request_start_line = request_lines[0]  # 解析请求报文
    file_name = re.match(r"\w+\s+(/[^ ]*)", request_start_line).group(1)
    print(file_name)
    # 提取请求的路径
    if "/" == file_name:
        file_name = "/index.html"
    try:
        htmlFile = open(ROOT_DIR + file_name,"r")
        file = htmlFile.read()
        htmlFile.close()
    except:
        response_start_line = "HTTP/1.1 404 NOT FOUND\r\n"
        response_body = "404 NOT FOUND"
    else:
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_body = file
    response = response_start_line + response_headers + "\r\n" + response_body
    clSocket.send(response.encode("utf-8"))
    # 网络传输的必须是byte类型，因此也可以是send(bytes(response,"utf-8"))
    # print("response:", response)
    clSocket.close()


def main():
    webS = socket(AF_INET, SOCK_STREAM)
    webS.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    webS.bind(("", 8000))
    webS.listen(128)
    while True:
        client, addr = webS.accept()
        print("[%s:%s] has connected"%addr)  # addr是元组，可以直接解包
        clp = Process(target=recv_request, args=(client,))
        clp.start()
        client.close()

if __name__ == "__main__":
    main()

