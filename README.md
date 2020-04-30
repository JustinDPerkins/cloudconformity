# Cloud Conformity Template Scanner API tool

This is a python package to Cloud Conformity Template Scanner. 

## Installing

To start using we need to setup the config.ini file first.
Navigate to the install pip package. <br>

Add your apiKey. We have created and environment variable
```
api= os.environ.get('apiKey')
``` 

Endpoint Region is set as US(Oregon - us-west-2)<br>
<br>
For reference, check out the conformity API documentation.<br>
https://github.com/cloudconformity/documentation-api


## Running a scan

Finally, we can scan a CloudFormation Template for misconfigurations before deployment into your AWS infrastructure.

We can scan by default or failures using either [all, fail]
Alternatively, we can filter by severity [Extreme, Very High, High, Medium, Low]

For example, a scan looking for any failure in your template
```
cloudconformity --scan fail C:\MyExample\template.yaml
```
Another example, a scan looking for extreme failures in your template
```
cloudconformity --scan extreme C:\MyExample\template.yaml
```
To see the original json response from API call
```
cloudconformity --scan default C:\MyExample\template.yaml