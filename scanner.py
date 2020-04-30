import sys
import os
import requests
import json
import argparse
def optionA(access,access2,access3, grade):
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
        if category == grade:
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


def optionG(access,access2,access3, desired_risk):
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
            if risk == desired_risk:
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
                                            

def main():
    # create cli argument for filepath
    parser = argparse.ArgumentParser(description='Scan a CFT Template')
    parser.add_argument("--scan", 
                        choices=["all", "fail", "extreme", "veryhigh", "high", "medium", "low", "default"],
                        required=True, type=str, help="Filter your Scan by Severity")
    parser.add_argument(dest="cloudformationtemp", help="specify file path")
    args = parser.parse_args()

    cloudformationtemp = args.cloudformationtemp
    scan = args.scan

    # set Environment variable. 
    api= os.environ.get('apiKey')
    
    
    #API connection for CC
    endpoint = 'https://us-west-2-api.cloudconformity.com'
    url = endpoint+'/v1/template-scanner/scan'
    url2 = endpoint+'/v1/services' 

    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': api
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

    if scan == "all":
        optionA(access,access2,access3, "SUCCESS")
        optionA(access,access2,access3, "FAILURE")
    elif scan == "fail":
        optionA(access,access2,access3, "FAILURE")
    elif scan == "extreme":
        optionG(access,access2,access3, "EXTREME")
    elif scan == "veryhigh":
        optionG(access,access2,access3, "VERY_HIGH")
    elif scan == "high":
        optionG(access,access2,access3, "HIGH")
    elif scan == "medium":
        optionG(access,access2,access3, "MEDIUM")
    elif scan == "low":
        optionG(access,access2,access3, "LOW")
    elif scan == "default":
        print(TurnResponsetoString)

if __name__ =="__main__":
    main()