import os


def write_word_counts(output_folder, word_counts):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Guardar los conteos en un archivo llamado "wordcount.tsv"
    output_path = os.path.join(output_folder, "wordcount.tsv")
    with open(output_path, "w", encoding="utf-8") as f:
        for key, value in word_counts.items():
            f.write(f"{key}\t{value}\n")
