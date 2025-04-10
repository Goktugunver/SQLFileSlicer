def split_sql_file(input_file, chunk_size_mb=50):
    chunk_size = chunk_size_mb * 1024 * 1024 
    file_count = 1
    output_file = open(f"part_{file_count}.sql", "w", encoding="utf-8")
    current_size = 0

    with open(input_file, "r", encoding="utf-8") as infile:
        for line in infile:
            current_size += len(line.encode("utf-8"))
            if current_size >= chunk_size:
                output_file.close()
                file_count += 1
                output_file = open(f"part_{file_count}.sql", "w", encoding="utf-8")
                current_size = len(line.encode("utf-8"))
            output_file.write(line)

    output_file.close()
    print(f"{file_count} adet dosya oluşturuldu.")

split_sql_file("/file.sql", chunk_size_mb=120)
