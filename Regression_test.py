import json
import os
import subprocess
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
        result.check_returncode()  # Check if the command was successful
        return json.loads(result.stdout)
    except subprocess.TimeoutExpired:
        print(f"Error: Docker command timed out after {timeout} seconds.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error: Docker command failed with return code {e.returncode}")
        print(f"stderr: {e.stderr}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON from Docker output: {e}")
        print(f"stdout: {result.stdout}")
        print(f"stderr: {result.stderr}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred while running Docker command: {e}")
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
