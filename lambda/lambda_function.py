import json
import boto3
import traceback 
# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Customer-Data')

#define lambda fucntion
def lambda_handler(event, context):
    try:
        http_method = str(event.get("httpMethod", "")).upper()

        # ==================================
        # POST - Add Customer Record
        #  ==================================
        if http_method == "POST":
        
            # Safely parse the JSON body
            body = json.loads(event.get("body", "{}"))

            # Use .get() to prevent any KeyError crashes
            cust_id = body.get("Customer_id") or body.get("customer_id") or ""
            cust_name = body.get("CustomerName") or body.get("customerName") or ""

            # Stop the code if required fields are missing
            if not cust_id or not cust_name:
                return {
                    "statusCode": 400,
                    "headers": {
                        "Content-Type": "application/json",
                        "Access-Control-Allow-Origin": "*",
                        "Access-Control-Allow-Headers": "Content-Type",
                        "Access-Control-Allow-Methods": "GET,POST,OPTIONS"
                    },
                    "body": json.dumps({"message": "Missing Customer_id or CustomerName"})
                }

            # Map fields safely into your DynamoDB dictionary layout
            customer = {
                "Customer_id": str(cust_id).strip(),
                "CustomerName": str(cust_name).strip(),
                "Email": str(body.get("Email") or body.get("email") or "").strip(),
                "Phone": str(body.get("Phone") or body.get("phone") or "").strip(),
                "City": str(body.get("City") or body.get("city") or "").strip()
            }

            # Write cleanly to DynamoDB
            table.put_item(Item=customer)

            return {
                "statusCode": 200,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Methods": "GET,POST,OPTIONS"
                },
                "body": json.dumps({"message": "Customer added successfully"})
            }
        # ==================================
        # GET - Handles Web Page AND Search Queries
        # ==================================
        elif http_method == "GET":
            params = event.get("queryStringParameters") or {}

            # If no tracking variable parameter exists, instantly serve the frontend layout page!
            if "Customer_id" not in params:
                return {
                    "statusCode": 200,
                    "headers": {
                        "Content-Type": "text/html",
                        "Access-Control-Allow-Origin": "*",
                        "Access-Control-Allow-Headers": "Content-Type",
                        "Access-Control-Allow-Methods": "GET,POST,OPTIONS"
                    },
                    "body": str(HTML_UI)
                }

            # If tracking variable parameters exist, safely extract data row elements from NoSQL mapping
            customer_id = params["Customer_id"]
            response = table.get_item(Key={"Customer_id": customer_id})

            if "Item" in response:
                return {
                    "statusCode": 200,
                    "headers": {
                        "Content-Type": "application/json",
                        "Access-Control-Allow-Origin": "*",
                        "Access-Control-Allow-Headers": "Content-Type",
                        "Access-Control-Allow-Methods": "GET,POST,OPTIONS"
                    },
                    "body": json.dumps(response["Item"])
                }
            else:
                return {
                    "statusCode": 404,
                    "headers": {
                        "Content-Type": "application/json",
                        "Access-Control-Allow-Origin": "*",
                        "Access-Control-Allow-Headers": "Content-Type",
                        "Access-Control-Allow-Methods": "GET,POST,OPTIONS"
                    },
                    "body": json.dumps({"message": "Customer not found"})
                }

        # ==================================
        # OPTIONS - CORS preflight
        # ==================================
        elif http_method == "OPTIONS":
            return {
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Methods": "GET,POST,OPTIONS"
                },
                "body": ""
            }

        else:
            return {
                "statusCode": 405,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Methods": "GET,POST,OPTIONS"
                },
                "body": json.dumps({"message": "Method Not Allowed"})
            }

    except Exception as e:
        print(traceback.format_exc())
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "GET,POST,OPTIONS"
            },
            "body": json.dumps({"message": f"Server Error: {str(e)}"})
        } # <--- Closes the body/return dictionary