import re

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

    def limpiar_problemas(self, input_file, match_list):
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines() #lines es una lista con una linea como elemento
            for i in range(len(match_list)):
                filtered_lines = [line for line in lines if match_list[i] not in line]
                lines = filtered_lines
        with open("./gravi_limpio.txt", 'w', encoding='utf-8') as modified_file:
            modified_file.writelines(filtered_lines)

    def separar_problemas(self, source_txt, match_regex):
        """Separates problems in the source text based on a regex pattern."""
        with open(source_txt, 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()
            current_prob = ''
            probs = []
            for line in lines:
                if not re.search(match_regex, line):
                    current_prob += line
                else:
                    probs.append(current_prob)
                    probs.append("\n\n")
                    current_prob = line
            probs.append(current_prob)

        with open("./file_separated.txt", 'w', encoding='utf-8') as modified_file:
            modified_file.writelines(probs)

        print("Lines modified and saved.")

    def run(self):
        """Runs the ETL process."""
        extracted_data = self.extract()
        transformed_data = self.transform(extracted_data)
        self.load(transformed_data)