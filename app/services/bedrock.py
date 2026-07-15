import os
import boto3
from dotenv import load_dotenv
from botocore.exceptions import ClientError

# Load environment variables
load_dotenv()

# Read configuration
AWS_REGION = os.getenv("AWS_REGION")
MODEL_ID = os.getenv("MODEL_ID")
USE_MOCK = os.getenv("USE_MOCK", "true").lower() == "true"

# Create Bedrock client
client = boto3.client(
    "bedrock-runtime",
    region_name=AWS_REGION
)


def chat_with_bedrock(question: str):
    """
    Returns a mock response if USE_MOCK=True.
    Otherwise, calls Amazon Bedrock.
    """

    # -------------------------
    # Mock Mode
    # -------------------------
    if USE_MOCK:
        return f"[Mock AI] You asked: {question}"

    # -------------------------
    # Real Bedrock Mode
    # -------------------------
    try:
        response = client.converse(
            modelId=MODEL_ID,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "text": question
                        }
                    ]
                }
            ]
        )

        answer = response["output"]["message"]["content"][0]["text"]

        return answer

    except ClientError as e:
        return f"AWS Error: {e.response['Error']['Message']}"

    except Exception as e:
        return str(e)