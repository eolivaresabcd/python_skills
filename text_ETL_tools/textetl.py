class TextETL:
    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file

    def extract(self):
        """Extracts data from the input file."""
        with open(self.input_file, 'r') as file:
            data = file.readlines()
        return data

    def transform(self, data):
        """Transforms the extracted data."""
        transformed_data = [line.strip().upper() for line in data]
        return transformed_data

    def load(self, data):
        """Loads the transformed data into the output file."""
        with open(self.output_file, 'w') as file:
            for line in data:
                file.write(line + '\n')

    def run(self):
        """Runs the ETL process."""
        extracted_data = self.extract()
        transformed_data = self.transform(extracted_data)
        self.load(transformed_data)