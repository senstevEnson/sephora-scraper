thonimport json
import requests
from extractors.product_parser import ProductParser
from outputs.exporters import Exporter

def run_scraper(input_file, output_file):
    # Load input data
    with open(input_file, 'r') as f:
        products_data = json.load(f)

    # Initialize product parser and exporter
    parser = ProductParser()
    exporter = Exporter()

    # Extract and process product data
    processed_data = []
    for product in products_data:
        processed_data.append(parser.parse_product(product))

    # Export the processed data
    exporter.export_to_json(processed_data, output_file)
    print(f"Data exported to {output_file}")

if __name__ == '__main__':
    run_scraper('data/inputs.sample.json', 'data/sample_output.json')