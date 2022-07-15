import csv, json, sys, argparse

def main(**kwargs):
    values = transform_values(parse_json(kwargs['file_input']))
    write_csv(values, kwargs['save'], kwargs['header'])


def transform_values(items):
    """
        Transform a Item[n]:
            {
                "id": {
                    "N": "123"
                },
                "ttl": {
                    "N": "594777600"
                },
                ...
           }
        Into:
            {"id": "123", "ttl" :"594777600"}
    """
    returnvalues = []
    for item in items:
        keys = item.keys()
        itemloop = {}
        for value in keys:
            k, v = item.get(value).popitem()
            itemloop[value] = v
        returnvalues.append(itemloop)
    return returnvalues


def parse_json(file_path):
    data = json.load(file_path)
    return data.get('Items', None)


def write_csv(values, save, header):
    """
        Write a dict to CSV format including the header
    """
    output = csv.writer(save)
    if header:
        output.writerow(values[0].keys())

    for row in values:
        output.writerow(row.values())


def clistart():
    parser = argparse.ArgumentParser(description='Parse DynamoDb table Items to a CSV')

    parser.add_argument('input', nargs='?', type=argparse.FileType('r'),
                        default=(None if sys.stdin.isatty() else sys.stdin),
                        help="""Input a Dynamodb JSON file ref: 
						 http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.LowLevelAPI.html""")

    parser.add_argument('output', nargs='?', type=argparse.FileType('w', encoding='UTF-8'),
                        default=sys.stdout,
                        help="""Provide a file name [csv], or a keep it blank and the content is sent to STDOUT""")

    group = parser.add_mutually_exclusive_group()
    group.add_argument('--csv-header', dest="header", action='store_true')
    group.add_argument('--no-csv-header', dest="header", action='store_false')

    parser.set_defaults(header=True)

    args = parser.parse_args()


    if(args.input is None):
        sys.stderr.write('Missing input argument\n')
        parser.print_help()
        sys.exit(2)

    main(file_input=args.input,
         save=args.output,
         header=args.header)