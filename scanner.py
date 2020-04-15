import sys
import os
import requests
import json
import argparse

# create cli argument for filepath
parser = argparse.ArgumentParser(description='Scan a CFT Template')
parser.add_argument("--scan", 
                    choices=["all", "fail", "extreme", "veryhigh", "high", "medium", "low"],
                    required=True, type=str, help="Filter your Scan by Severity")
parser.add_argument(dest="cloudformationtemp", help="specify file path")
args = parser.parse_args()

cloudformationtemp = args.cloudformationtemp
scan = args.scan

# set Environment variable. 
api= os.environ.get('apiKey')
# Region in which Cloud Conformity serves your organisation
region="us-west-2"
#API connection for CC
endpoint = 'https://' + region + '-api.cloudconformity.com'
url = endpoint + '/v1/template-scanner/scan'
url2 = endpoint + '/v1/services'

headers = {
	'Content-Type': 'application/vnd.api+json',
	'Authorization': 'ApiKey ' + api
}

#open file and print contents.
try:
    contents = open(cloudformationtemp, 'r').read() 
except ValueError:
    print("Template Scanner could not process your template...")
    sys.exit()

payload =  {
	'data': {
		'attributes': {
			'type': 'cloudformation-template',
			'contents': contents
		}
	}
}
# post method
resp = requests.post(url, headers=headers, data=json.dumps(payload))
TurnResponsetoString = json.dumps(resp.json(), indent=2, sort_keys=True)
formResponse = json.loads(TurnResponsetoString)
# get method
response = requests.get(url2,headers=headers)
formatResponse = json.dumps(response.json(), indent=3, sort_keys=False)
results = json.loads(formatResponse)

# key for post call
access = formResponse['data']
# keys for get call
access2 = results['data']
access3 = results['included']
def optionA():
    for data in access:
        rules = data['relationships']
        ruledata = rules['rule']
        rulelist = ruledata['data']
        aruleid = rulelist['id']
        attributes = data['attributes']
        rulename = attributes["rule-title"]
        category = attributes['status']
        message = attributes['message']
        risk = attributes['risk-level']
        info = data["id"]
        for data in access2:
            relationship = data['relationships']
            rules = relationship['rules']
            identifier = rules['data']
            attributes = data['attributes']
            provider = attributes['provider']
            awsservice = attributes['name']
            for data in access3:
                ruleid = data['id']
                html = data['knowledge-base-html']
                for data in identifier:
                    rulenum = data['id']
                    if aruleid == rulenum:
                        if aruleid == ruleid:
                            if ruleid == rulenum:
                                    test = ( "https://www.cloudconformity.com/knowledge-base/" + provider + "/" + awsservice + "/" + html + ".html")
                                    #print(ruleid)
                                    print("\n", aruleid, "\n", rulename,"\n", category,"\n", message,"\n", risk,"\n", info, "\n", test)

def optionB():
    for data in access:
        rules = data['relationships']
        ruledata = rules['rule']
        rulelist = ruledata['data']
        aruleid = rulelist['id']
        attributes = data['attributes']
        rulename = attributes["rule-title"]
        category = attributes['status']
        message = attributes['message']
        risk = attributes['risk-level']
        info = data["id"]
        if category == "FAILURE":
            for data in access2:
                relationship = data['relationships']
                rules = relationship['rules']
                identifier = rules['data']
                attributes = data['attributes']
                provider = attributes['provider']
                awsservice = attributes['name']
                for data in access3:
                    ruleid = data['id']
                    html = data['knowledge-base-html']
                    for data in identifier:
                        rulenum = data['id']
                        if aruleid == rulenum:
                            if aruleid == ruleid:
                                if ruleid == rulenum:
                                        test = ( "https://www.cloudconformity.com/knowledge-base/" + provider + "/" + awsservice + "/" + html + ".html")
                                        #print(ruleid)
                                        print("\n", aruleid, "\n", rulename,"\n", category,"\n", message,"\n", risk,"\n", info, "\n", test)
def optionC():
    for data in access:
        rules = data['relationships']
        ruledata = rules['rule']
        rulelist = ruledata['data']
        aruleid = rulelist['id']
        attributes = data['attributes']
        rulename = attributes["rule-title"]
        category = attributes['status']
        message = attributes['message']
        risk = attributes['risk-level']
        info = data["id"]
        if category == "FAILURE":
            if risk == "EXTREME":
                for data in access2:
                    relationship = data['relationships']
                    rules = relationship['rules']
                    identifier = rules['data']
                    attributes = data['attributes']
                    provider = attributes['provider']
                    awsservice = attributes['name']
                    for data in access3:
                        ruleid = data['id']
                        html = data['knowledge-base-html']
                        for data in identifier:
                            rulenum = data['id']
                            if aruleid == rulenum:
                                if aruleid == ruleid:
                                    if ruleid == rulenum:
                                            test = ( "https://www.cloudconformity.com/knowledge-base/" + provider + "/" + awsservice + "/" + html + ".html")
                                            #print(ruleid)
                                            print("\n", aruleid, "\n", rulename,"\n", category,"\n", message,"\n", risk,"\n", info, "\n", test)

def optionD():
    for data in access:
        rules = data['relationships']
        ruledata = rules['rule']
        rulelist = ruledata['data']
        aruleid = rulelist['id']
        attributes = data['attributes']
        rulename = attributes["rule-title"]
        category = attributes['status']
        message = attributes['message']
        risk = attributes['risk-level']
        info = data["id"]
        if category == "FAILURE":
            if risk == "VERY_HIGH":
                for data in access2:
                    relationship = data['relationships']
                    rules = relationship['rules']
                    identifier = rules['data']
                    attributes = data['attributes']
                    provider = attributes['provider']
                    awsservice = attributes['name']
                    for data in access3:
                        ruleid = data['id']
                        html = data['knowledge-base-html']
                        for data in identifier:
                            rulenum = data['id']
                            if aruleid == rulenum:
                                if aruleid == ruleid:
                                    if ruleid == rulenum:
                                            test = ( "https://www.cloudconformity.com/knowledge-base/" + provider + "/" + awsservice + "/" + html + ".html")
                                            #print(ruleid)
                                            print("\n", aruleid, "\n", rulename,"\n", category,"\n", message,"\n", risk,"\n", info, "\n", test)

def optionE():
    for data in access:
        rules = data['relationships']
        ruledata = rules['rule']
        rulelist = ruledata['data']
        aruleid = rulelist['id']
        attributes = data['attributes']
        rulename = attributes["rule-title"]
        category = attributes['status']
        message = attributes['message']
        risk = attributes['risk-level']
        info = data["id"]
        if category == "FAILURE":
            if risk == "HIGH":
                for data in access2:
                    relationship = data['relationships']
                    rules = relationship['rules']
                    identifier = rules['data']
                    attributes = data['attributes']
                    provider = attributes['provider']
                    awsservice = attributes['name']
                    for data in access3:
                        ruleid = data['id']
                        html = data['knowledge-base-html']
                        for data in identifier:
                            rulenum = data['id']
                            if aruleid == rulenum:
                                if aruleid == ruleid:
                                    if ruleid == rulenum:
                                            test = ( "https://www.cloudconformity.com/knowledge-base/" + provider + "/" + awsservice + "/" + html + ".html")
                                            #print(ruleid)
                                            print("\n", aruleid, "\n", rulename,"\n", category,"\n", message,"\n", risk,"\n", info, "\n", test)

def optionF():
    for data in access:
        rules = data['relationships']
        ruledata = rules['rule']
        rulelist = ruledata['data']
        aruleid = rulelist['id']
        attributes = data['attributes']
        rulename = attributes["rule-title"]
        category = attributes['status']
        message = attributes['message']
        risk = attributes['risk-level']
        info = data["id"]
        if category == "FAILURE":
            if risk == "MEDIUM":
                for data in access2:
                    relationship = data['relationships']
                    rules = relationship['rules']
                    identifier = rules['data']
                    attributes = data['attributes']
                    provider = attributes['provider']
                    awsservice = attributes['name']
                    for data in access3:
                        ruleid = data['id']
                        html = data['knowledge-base-html']
                        for data in identifier:
                            rulenum = data['id']
                            if aruleid == rulenum:
                                if aruleid == ruleid:
                                    if ruleid == rulenum:
                                            test = ( "https://www.cloudconformity.com/knowledge-base/" + provider + "/" + awsservice + "/" + html + ".html")
                                            #print(ruleid)
                                            print("\n", aruleid, "\n", rulename,"\n", category,"\n", message,"\n", risk,"\n", info, "\n", test)

def optionG():
    for data in access:
        rules = data['relationships']
        ruledata = rules['rule']
        rulelist = ruledata['data']
        aruleid = rulelist['id']
        attributes = data['attributes']
        rulename = attributes["rule-title"]
        category = attributes['status']
        message = attributes['message']
        risk = attributes['risk-level']
        info = data["id"]
        if category == "FAILURE":
            if risk == "LOW":
                for data in access2:
                    relationship = data['relationships']
                    rules = relationship['rules']
                    identifier = rules['data']
                    attributes = data['attributes']
                    provider = attributes['provider']
                    awsservice = attributes['name']
                    for data in access3:
                        ruleid = data['id']
                        html = data['knowledge-base-html']
                        for data in identifier:
                            rulenum = data['id']
                            if aruleid == rulenum:
                                if aruleid == ruleid:
                                    if ruleid == rulenum:
                                            test = ( "https://www.cloudconformity.com/knowledge-base/" + provider + "/" + awsservice + "/" + html + ".html")
                                            #print(ruleid)
                                            print("\n", aruleid, "\n", rulename,"\n", category,"\n", message,"\n", risk,"\n", info, "\n", test)

if scan == "all":
    optionA()
elif scan == "fail":
  optionB()
elif scan == "extreme":
      optionC()
elif scan == "veryhigh":
      optionD()
elif scan == "high":
      optionE()
elif scan == "medium":
      optionF()
elif scan == "low":
      optionF()
else:
    print("Not a correct filter option")


    					