import json

def lambda_handler(event, context):
    # Extracting numbers from the event
    number1 = event.get('number1')
    number2 = event.get('number2')
    
    # Check if numbers are provided in the event
    if number1 is None or number2 is None:
        return {
            'statusCode': 400,
            'body': json.dumps('Both number1 and number2 must be provided')
        }

    # Adding the numbers
    result = number1 + number2
    
    # Returning the result
    return {
        'statusCode': 200,
        'body': json.dumps({'result': result})
    }
