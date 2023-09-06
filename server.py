import boto3

def get_gif(map, character):
    dynamodb = boto3.client('dynamodb', region_name='us-west-1')

    table_name = 'lineupinfo'

    response = dynamodb.scan(TableName=table_name)

    items = response.get('Items', [])

    for item in items:
        map_item = item.get('map', {}).get('S', None)
        character_item = item.get('character', {}).get('S', None) 
        link_item = item.get('link', {}).get('S', None)
        if(map_item == map and character_item == character):
            yield(str(link_item))

if __name__ == '__main__':
    get_gif('ascent', 'brimstone')