from src.app import tedit
from argparse import ArgumentParser
from pathlib import Path

if __name__ == "__main__":
    parser = ArgumentParser("tedit")
    parser.add_argument(
        "folder",
        type=Path,
        nargs="?",
        default=Path(__file__).parent.parent
    )

    args = parser.parse_args()
    folder: Path = args.folder

    if not folder.exists():
        raise FileNotFoundError(f"no folder found for path: {folder}")
    if not folder.is_dir():
        folder = folder.parent
    
    app = tedit(folder)
    app.run()
