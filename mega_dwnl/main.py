from ez_pyload import download

import rarfile
import os
from pathlib import Path
import re

OUT_PATH = Path("./tdatas")
OUT_ARCHIVES = Path("./tdatas_zips")
LINKS_PATH = Path("./links.txt")
for i in [OUT_ARCHIVES, OUT_PATH]:
    if not os.path.exists(i):
        os.mkdir(i)


def extract_links_from_file(file_path: Path | str):
    # Регулярное выражение для поиска URL
    url_pattern = re.compile(r"(https?://\S+)")

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Найти все ссылки
    links = url_pattern.findall(content)

    return links


def extract_rar(file_path: Path | str, extract_path: Path | str):
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)

    with rarfile.RarFile(file_path) as rf:
        rf.extractall(extract_path)


# out = download(
#     "https://mega.nz/file/RNBlASrY#qqziLLjIV3H-LcYFuiH6Oprr22GTZtyeIIhi5zpS6Nw",
#     download_dir=OUT_ARCHIVES,
# )


# extract_rar(file_path=out, extract_path=OUT_PATH)
def main():

    for url in extract_links_from_file(LINKS_PATH):
        out = download(url, download_dir=OUT_ARCHIVES)
        extract_rar(file_path=out, extract_path=OUT_PATH)


if __name__ == "__main__":
    main()
