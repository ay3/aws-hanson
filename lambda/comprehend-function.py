import json
import boto3

comprehend = boto3.client('comprehend')

def lambda_handler(event, context):
    input_text = '美味しかったです'
    
    response = comprehend.detect_sentiment(
        Text=input_text,
        LanguageCode='ja'
    )
    sentiment_score = response['SentimentScore']
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps({
            'sentiment_score' : sentiment_score
        })
    }
