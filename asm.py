import subprocess
import os

def disassemble_source(source_file, output_file):
    try:
        cmd = ['g++', '-S', '-o', output_file, source_file]
        subprocess.run(cmd, check=True)
        print(f"Disassembly saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during disassembly: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    source_file = "main.cpp"  
    output_file = "output/example.S"  

    if os.path.isfile(source_file):
        disassemble_source(source_file, output_file)
    else:
        print(f"Source file '{source_file}' not found.")
