from argparse import ArgumentParser
from generator.core.image_generator import search_and_download

argparser = ArgumentParser(
    prog='generator',
    description="Generate image datasets from Google via your terminal"
)

reqd = argparser.add_argument_group('required_arguments')
reqd.add_argument(
    '-q', '--query',
    required=True,
    help='Query to search for images to be downloaded'
)

argparser.add_argument(
    '-s', '--size',
    help='Number of images to be downloaded in the dataset',
    type=int,
    default=5000
)

argparser.add_argument(
    '-p', '--path',
    help='Path of dataset directory to store the images',
    default='./dataset'
)

args = argparser.parse_args()

print(args)

search_and_download(args.query, args.path, int(args.size))