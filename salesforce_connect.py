from simple_salesforce import Salesforce
from dotenv import load_dotenv
import os

load_dotenv()

ORG1_NAME = os.getenv('ORG1_NAME')
ORG1_USERNAME = os.getenv('ORG1_USERNAME')
ORG1_PASSWORD = os.getenv('ORG1_PASSWORD')
ORG1_SECURITY_TOKEN = os.getenv('ORG1_SECURITY_TOKEN')

ORG2_NAME = os.getenv('ORG2_NAME')
ORG2_USERNAME = os.getenv('ORG2_USERNAME')
ORG2_PASSWORD = os.getenv('ORG2_PASSWORD')
ORG2_SECURITY_TOKEN = os.getenv('ORG2_SECURITY_TOKEN')

IS_DEBUG = os.getenv('IS_DEBUG') == 'true'

STANDARD_OBJECTS = {'Account', 'Task', 'Case', 'Lead', 'Event', 'EmailMessage', 'Contact'}

def connect_to_org(username, password, security_token):
    return Salesforce(username=username, password=password, security_token=security_token)

def filter_objects(objects, standard_objects):
    custom_objs = [obj for obj in objects if obj['custom']]
    standard_objs = [obj for obj in objects if obj['name'] in standard_objects]
    return custom_objs, standard_objs

def retrieve_metadata(org1, org2, standard_objects):
    if IS_DEBUG:
        print("Debug mode: querying only 'Account' and 'Contact'.")
        return [{'name': 'Account'}, {'name': 'Contact'}], [{'name': 'Account'}, {'name': 'Contact'}], [], []
    
    org1_custom_objects, org1_standard_objects = filter_objects(org1.describe()['sobjects'], standard_objects)
    org2_custom_objects, org2_standard_objects = filter_objects(org2.describe()['sobjects'], standard_objects)
    return org1_custom_objects, org2_custom_objects, org1_standard_objects, org2_standard_objects
