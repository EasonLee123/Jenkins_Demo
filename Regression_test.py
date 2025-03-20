import json
import os
import sys

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from file {file_path}: {e}")
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred while loading JSON from {file_path}: {e}")
        sys.exit(1)

def save_json(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"An unexpected error occurred while saving JSON to {file_path}: {e}")
        sys.exit(1)

def compare_results(actual, expected):
    return actual == expected

def main():
    config = load_json('config.json')
    test_case_dir = config['test_case_dir']
    expected_results_dir = config['expected_results_dir']
    results_dir = config['results_dir']
    
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    
    test_cases = os.listdir(test_case_dir)
    
    for test_case_file in test_cases:
        if test_case_file.endswith('.json'):
            test_case_path = os.path.join(test_case_dir, test_case_file)
            expected_result_file = f"expected_{test_case_file.split('_')[1]}"
            expected_result_path = os.path.join(expected_results_dir, expected_result_file)
            result_file = f"result_{test_case_file.split('_')[1]}"
            result_path = os.path.join(results_dir, result_file)
            
            input_json = load_json(test_case_path)
            expected_output_json = load_json(expected_result_path)
            actual_output_json = load_json('docker_output.json')
            
            save_json(actual_output_json, result_path)
            
            if compare_results(actual_output_json, expected_output_json):
                print(f"Test {test_case_file}passed.")
            else:
                print(f"Test {test_case_file}failed.")
if __name__ == '__main__':
    main()
