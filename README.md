# **Salesforce Org Comparator**

This tool compares metadata between two Salesforce orgs and generates an Excel report showing differences in custom and standard objects, fields, and other configurations.

## **Features**

- Compares custom objects and specific standard objects (Account, Task, Case, Lead, Event, EmailMessage).
- Generates a detailed Excel report highlighting differences.
- Caches API results for efficient performance.
- Includes a debug mode for testing with limited API calls.

## **Requirements**

- Python 3.x
- Salesforce credentials for both orgs
- [simple-salesforce](https://pypi.org/project/simple-salesforce/)
- [openpyxl](https://pypi.org/project/openpyxl/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## **Setup Instructions**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/DeveloperEstiven/Salesforce-OrgComparator.git
   cd Salesforce-OrgComparator
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the root of the project and add your Salesforce credentials:

   ```ini
   ORG1_NAME=Org1
   ORG1_USERNAME=your_org1_username
   ORG1_PASSWORD=your_org1_password
   ORG1_SECURITY_TOKEN=your_org1_security_token

   ORG2_NAME=Org2
   ORG2_USERNAME=your_org2_username
   ORG2_PASSWORD=your_org2_password
   ORG2_SECURITY_TOKEN=your_org2_security_token

   IS_DEBUG=true  # Set to false to compare all objects
   ```

5. **Run the tool:**

   ```bash
   python main.py
   ```

6. **Check the generated Excel report**: The report will be saved as `salesforce_org_comparison.xlsx` in the project root.
