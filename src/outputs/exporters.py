thonimport json

class Exporter:
    def export_to_json(self, data, output_file):
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data exported to {output_file}")