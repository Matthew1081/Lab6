import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    print(f"Converting {input_file} to {output_file}")

if __name__ == "__main__":
    main()
