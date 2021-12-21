from decimal import Decimal
import json
from pprint import pprint

import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError


def create_movie_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb',
            aws_access_key_id='AKIARHJNYUABV7AVS226',
            aws_secret_access_key='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',
            region_name='us-west-2'
        )

    table = dynamodb.create_table(
        TableName='Movies',
        KeySchema=[
            {
                'AttributeName': 'year',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'title',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


def put_movie(title, year, plot, rating, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb',
            aws_access_key_id='AKIARHJNYUABV7AVS226',
            aws_secret_access_key='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',
            region_name='us-west-2'
        )

    table = dynamodb.Table('Movies')
    response = table.put_item(
        Item={
            'year': year,
            'title': title,
            'info': {
                'plot': plot,
                'rating': rating
            }
        }
    )
    return response


if __name__ == '__main__':
    movie_table = create_movie_table()
    print("Table status:", movie_table.table_status)
    movie_resp = put_movie("The Big New Movie", 2015,
                           "Nothing happens at all.", 0)
    pprint(movie_resp, sort_dicts=False)
    ...
