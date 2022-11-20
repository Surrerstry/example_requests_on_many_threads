
files = [
    "./big_data_to_upload/1.txt",
    "./big_data_to_upload/2.txt",
    "./big_data_to_upload/3.txt",
    "./big_data_to_upload/4.txt",
    "./big_data_to_upload/5.txt",
]


for n, file in enumerate(files, start=1):
    with open(file, 'w') as f:
        f.write(f"{str(n) * 100000}")
