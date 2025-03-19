import json
import os
import subprocess
import sys

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
def run_docker_command(docker_command, input_json, timeout):
    try:
        result = subprocess.run(
            docker_command,
            input=json.dumps(input_json),
            text=True,
            capture_output=True,
            timeout=timeout,
            shell=True
        )
        return json.loads(result.stdout)
    except subprocess.TimeoutExpired:
        print(f"Error: Docker command timed out after {timeout} seconds.")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from Docker output.")
        sys.exit(1)
      
def compare_results(actual, expected):
    return actual == expected
  
def main():
    config = load_json('config.json')
    docker_image_name = config['docker_image_name']
    test_case_dir = config['test_case_dir']
    expected_results_dir = config['expected_results_dir']
    results_dir = config['results_dir']
    docker_command_template = config['docker_command']
    timeout = config['timeout']
    docker_command = docker_command_template.format(image_name=docker_image_name)
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
            actual_output_json = run_docker_command(docker_command, input_json, timeout)
            save_json(actual_output_json, result_path)
            if compare_results(actual_output_json, expected_output_json):
                print(f"Test {test_case_file} passed.")
            else:
                print(f"Test {test_case_file} failed.")
if __name__ == '__main__':
    main()
