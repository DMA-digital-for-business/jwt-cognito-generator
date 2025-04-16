# 🔐 JWT Generation – AWS Cognito

This guide provides a script-based method for generating **signed JWT tokens** from an Amazon Cognito User Pool. It is useful for development, automated testing, or secure integration tasks.

> ⚠️ The following guide is intended for Unix system.


## 📋 Requirements

Before setup and run the script, make sure the following are installed on your system:

* **`python3`**
* **`pip3`**

To check if the requirements are installed:

```bash
python3 --version
pip3 --version
```

## ⚡ TL;DR

```bash
# From the repository root
# 1. Create and activate a virtual environment
python3 -m venv ./venv
source ./venv/bin/activate

# 2. Install dependencies
pip3 install -r requirements.txt

# 3. Edit credentials inside the script:
#    - client_id
#    - client_secret (optional)
#    - userpool_id
#    - username
#    - password

# 4. Run the script
python3 jwt-cognito-generator.py
```

### 🧰 Requirements & Setup

#### 1. Create a Python Virtual Environment (Recommended)

To avoid dependency conflicts:

```bash
python3 -m venv /path/to/project
source /path/to/project/bin/activate
```

### 2. Install Python Dependencies

From within the virtual environment:

```bash
pip3 install -r /path/to/requirements.txt
```

### 3. Configure Cognito Credentials

Open the `jwt-cognito-generator.py` file and modify the following variables:

```python
client_id = "<YOUR_CLIENT_ID>"
client_secret = "<YOUR_CLIENT_SECRET>" (optional)
userpool_id = "<YOUR_USERPOOL_ID>"
username = "<YOUR_COGNITO_USERNAME>"
password = "<YOUR_COGNITO_PASSWORD>"
```

> ⚠️ If the authentication flow requires **SRP (Secure Remote Password)** , you need to configure the **client secret** as well. Once the client secret is configured, you should include the `SECRET_HASH` field in the `AuthParameters` of the `initiate_auth` request.

> To do this, simply uncomment the corresponding line in the code, and the `SECRET_HASH` will be automatically generated and sent along with the other parameters.


## ▶️ Script Execution

Once configuration is complete, run the script:

```bash
python3 /path/to/jwt-cognito-generator.py
```

If successful, it will output signed **JWT access and id token**.


## 🔒 Security Notes

- **Never commit your credentials** to source control.
- Use environment variables or secure secret storage for production-grade automation.
- Make sure the Cognito App Client supports the selected authentication flow.
