def save_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    data = load_json(input_file)
    if data is None:
        return

    save_json(data, output_file)
    print(f"Successfully converted {input_file} to {output_file}")

if __name__ == "__main__":
    main()
