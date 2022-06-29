from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    # Read/write to the file
    f.write('Hello World\n')
    f.write('Testing\n')
    # Seek back to beginning and read the data
    f.seek(0)
    data = f.read()
    print(data)

# Temporary file is destroyed
