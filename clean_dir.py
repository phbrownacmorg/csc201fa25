from pathlib import Path
from tkinter.filedialog import askdirectory

def clean_dir_walk(directory: Path) -> int:
    dirs_to_ignore = ['__pycache__', '.mypy_cache', '.git']
    patterns_to_clean = ['*.bak', '*.bak2', '*~', '#*']

    cleaned = 0
    for root, dirs, files in directory.walk(): # type: ignore
        for d in dirs_to_ignore:
            if d in dirs:
                dirs.remove(d)
        for f in files:
            p = Path(f).absolute()
            for pattern in patterns_to_clean:
                if p.match(pattern):
                    print('Deleting', p)
                    p.unlink()
                    cleaned = cleaned + 1
                    break # Break out of the patterns loop
    return cleaned

def main(args: list[str]) -> int:
    """Remove the backup files from the current directory and all its
       subdirectories."""
    dir: Path = Path(askdirectory(title="Please select a directory to clean",
                                  mustexist=True, initialdir='..'))
    print('')
    print('Cleaned', clean_dir_walk(dir), 'files by walking.')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
