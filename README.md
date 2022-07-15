# DynamodbJsonToCSV

usage: dynamotocsv [-h] [--csv-header | --no-csv-header] [input] [output]

Parse DynamoDb table Items to a CSV

positional arguments:
  input            Input a Dynamodb JSON file ref:
                   http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.LowLevelAPI.html
  output           Provide a file name [csv], or a keep it blank and the content is sent to STDOUT

optional arguments:
  -h, --help       show this help message and exit
  --csv-header
  --no-csv-header