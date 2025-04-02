import sys
import shutil
from pathlib import Path

def create_dataset_directories(base_dir: Path) -> None:
    print("Start creation of dataset directories...")

    base_dir.mkdir(parents=True, exist_ok=True)

    for directory in ["train", "validation", "test"]:
        sub_dir = base_dir / directory
        sub_dir.mkdir(exist_ok=True)
        (sub_dir / "cats").mkdir(exist_ok=True)
        (sub_dir / "dogs").mkdir(exist_ok=True)

    print("Done")


def copy_data(src: Path, dst: Path, example_name: str, start: int, end: int) -> None:
    fnames = [f"{example_name}.{i}.jpg" for i in range(start, end)]
    print("Copying...")
    
    for fname in fnames:
        src_path = src / fname
        dst_path = dst / fname
        if src_path.exists():
            print(f"Copying {fname} to {dst}")
            shutil.copyfile(src_path, dst_path)
        else:
            print(f"Warning: {fname} not found in {src}")


def main(argv):
    if len(argv) != 3:
        print("Bad arguments")
        sys.exit(-1)

    src = Path(argv[1]).resolve()  # Convert to absolute path
    dst = Path(argv[2]).resolve()  # Convert to absolute path

    create_dataset_directories(dst)

    copy_data(src, dst / "train/cats", "cat", 0, 1000)
    copy_data(src, dst / "train/dogs", "dog", 0, 1000)

    copy_data(src, dst / "validation/cats", "cat", 1000, 1500)
    copy_data(src, dst / "validation/dogs", "dog", 1000, 1500)

    copy_data(src, dst / "test/cats", "cat", 1500, 2000)
    copy_data(src, dst / "test/dogs", "dog", 1500, 2000)


if __name__ == "__main__":
    main(sys.argv)