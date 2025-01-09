"""
Memory-efficient generator for processing large files.
"""


def process_large_file(file_path, chunk_size=8192):
    """Process a large file in chunks using a generator."""

    def line_generator():
        buffer = ""
        with open(file_path, 'r') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    if buffer:
                        yield buffer
                    break

                buffer += chunk
                while '\n' in buffer:
                    line_, buffer = buffer.split('\n', 1)
                    yield line_

    total_lines = 0
    total_chars = 0

    for line in line_generator():
        total_lines += 1
        total_chars += len(line)
        # Process line here

    return total_lines, total_chars


# Usage
filepath = "large_file.txt"
lines, chars = process_large_file(filepath)
