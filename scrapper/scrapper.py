import os

__version__ = "1.0.0"

DEFAULT_URLS_FILE = "list.txt"


def _is_url_line(line: str) -> bool:
    stripped = line.strip()
    return bool(stripped) and not stripped.startswith("#")


def read_urls(path: str | os.PathLike[str] = DEFAULT_URLS_FILE) -> set[str]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    with open(path, encoding="utf-8") as file:
        return {line.strip() for line in file if _is_url_line(line)}


def main():
    urls = read_urls()
    for n, url in enumerate(urls, start=1):
        print(f"{n:3}. {url}")
    total = len(urls)
    print(f"Total URLs: {total}")


if __name__ == "__main__":
    main()
