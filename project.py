import sys
import json

def load_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Invalid JSON format")
        return None

def main():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    data = load_json(input_file)
    if data is None:
        return

    print(f"Successfully loaded {input_file}")

if __name__ == "__main__":
    main()
