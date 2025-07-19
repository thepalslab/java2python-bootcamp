# scaffold.py (place at repo root)
import os, textwrap

BASE = os.path.join("src", "py100days", "days")

def ensure(path: str):
    os.makedirs(path, exist_ok=True)
    init = os.path.join(path, "__init__.py")
    if not os.path.exists(init):
        open(init, "w").close()

def make_day(n: int):
    day_dir = os.path.join(BASE, f"day{n:02d}")
    ensure(BASE)
    ensure(day_dir)
    task_py = os.path.join(day_dir, "task.py")
    if not os.path.exists(task_py):
        with open(task_py, "w") as f:
            f.write(textwrap.dedent(f"""\
                def main():
                    print("Hello from Day {n:02d}!")
            """))
        print(f"Created {task_py}")
    else:
        print(f"Exists {task_py}")

if __name__ == "__main__":
    for i in range(1, 101):
        make_day(i)
