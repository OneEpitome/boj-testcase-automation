from requests_html import HTMLSession
import subprocess
from lxml import html
import sys

if (len(sys.argv) < 2):
    problemNo = input("BOJ 문제 번호를 입력하세요 : ")

else:
    problemNo = sys.argv[1]

# 웹 페이지에 요청을 보냅니다.
session = HTMLSession()
response = session.get(f'https://www.acmicpc.net/problem/{problemNo}')
response.encoding = 'utf-8'

tree = html.fromstring(response.content)

# # 컴포넌트 선택자를 지정합니다.
inputSelector = "[id^='sample-input']"
outputSelector = "[id^='sample-output']"

# # 선택한 컴포넌트의 textContent를 수집합니다.
inputs = [''.join(element.itertext()) for element in tree.cssselect(inputSelector)]
outputs = [''.join(element.itertext()) for element in tree.cssselect(outputSelector)]

N = len(inputs) # a number of test cases
count = 0

print(f'There are {N} test cases ...')

for i in range(N):
    result = subprocess.run(["python3", "code.py"], input=inputs[i], capture_output=True, text=True)  # 스크립트 실행 및 인수 전달
    if (result.stdout.rstrip() == outputs[i].rstrip()):
        print("PASS")
        count += 1

    else:
        print(f'Wrong : {result.stdout}, Answer : {outputs[0]}')
        print("Fail")

if count == N:
    print("All Test cases are passed")
