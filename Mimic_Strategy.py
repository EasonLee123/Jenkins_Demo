import json
import sys
def process_input(input_data):
    # Process the input data
    processed_value = f"processed_{input_data['input_parameter_1']}"
    calculation_result = input_data['input_parameter_2'] * 2
    nested_result = {
        "processed_key": f"transformed_{input_data['nested_parameter']['key1']}",
        "sum_of_array": sum(input_data['nested_parameter']['key2'])
    }
    # Create the output data
    output_data = {
        "result": "success",
        "processed_value": processed_value,
        "calculation_result": calculation_result,
        "nested_result": nested_result
    }
    return output_data
def main():
    # Read input JSON from stdin
    input_json = sys.stdin.read()
    input_data = json.loads(input_json)
    # Process the input data
    output_data = process_input(input_data)
    # Print the output JSON to stdout
    print(json.dumps(output_data, indent=4))
if __name__ == '__main__':
    main()
