from flask import Flask, request, jsonify
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import requests

app = Flask(__name__)

@app.route('/analyze_user_input', methods=['POST'])
def analyze_user_input():
    # Extract user input from request
    user_input = request.json['user_input']

    # Analyze user input using Azure Text Analytics
    text_analytics_client = TextAnalyticsClient(endpoint=TEXT_ANALYTICS_ENDPOINT, credential=AzureKeyCredential(TEXT_ANALYTICS_KEY))
    result = text_analytics_client.extract_key_phrases([user_input])
    keywords = result[0].key_phrases

    # Calculate distance using Azure Maps
    response = requests.get(f"https://atlas.microsoft.com/route/directions/json?api-version=1.0&subscription-key={MAPS_SUBSCRIPTION_KEY}&query=origin:New York&destination:Los Angeles")
    data = response.json()
    distance = data['routes'][0]['summary']['lengthInMeters']

    # Store user preferences in Azure Cosmos DB (dummy code)
    # cosmos_db_client = CosmosClient(endpoint=COSMOS_DB_ENDPOINT, key=COSMOS_DB_KEY)
    # cosmos_db_client.create_database_if_not_exists("trip_planner")
    # cosmos_db_client.create_container_if_not_exists("trip_planner", "user_preferences")
    # cosmos_db_client.upsert_item("trip_planner", "user_preferences", {"keywords": keywords})

    return jsonify({'keywords': keywords, 'distance': distance})

if __name__ == '__main__':
    app.run(debug=True)
