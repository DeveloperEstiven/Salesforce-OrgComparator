from salesforce_connect import (
    connect_to_org, 
    retrieve_metadata, 
    ORG1_NAME, 
    ORG2_NAME, 
    IS_DEBUG, 
    ORG1_USERNAME, 
    ORG1_PASSWORD, 
    ORG1_SECURITY_TOKEN, 
    ORG2_USERNAME, 
    ORG2_PASSWORD, 
    ORG2_SECURITY_TOKEN,
    STANDARD_OBJECTS  # Import STANDARD_OBJECTS
)
from comparison import compare_and_write_sheet
from utils import create_dropdowns, auto_adjust_column_widths
from openpyxl import Workbook

# Connect to orgs
org1 = connect_to_org(ORG1_USERNAME, ORG1_PASSWORD, ORG1_SECURITY_TOKEN)
org2 = connect_to_org(ORG2_USERNAME, ORG2_PASSWORD, ORG2_SECURITY_TOKEN)

# Retrieve metadata
org1_custom_objects, org2_custom_objects, org1_standard_objects, org2_standard_objects = retrieve_metadata(org1, org2, STANDARD_OBJECTS)

# Handle debug mode
if IS_DEBUG:
    objects_to_compare = [{'name': 'Account'}, {'name': 'Contact'}], [{'name': 'Account'}, {'name': 'Contact'}]
else:
    objects_to_compare = org1_custom_objects + org1_standard_objects, org2_custom_objects + org2_standard_objects

# Create workbook
wb = Workbook()
ws_custom = wb.active
ws_custom.title = "Objects Comparison"

# Compare and write data to Excel
compare_and_write_sheet(ws_custom, objects_to_compare[0], objects_to_compare[1], org1, org2, ORG1_NAME, ORG2_NAME)

# Auto-adjust columns and create dropdowns
auto_adjust_column_widths(ws_custom)
create_dropdowns(ws_custom, ws_custom.max_row, ['E', 'F', 'G'], ORG1_NAME, ORG2_NAME)

# Save Excel file
wb.save("salesforce_org_comparison.xlsx")

print("Comparison completed and saved to 'salesforce_org_comparison.xlsx'")
