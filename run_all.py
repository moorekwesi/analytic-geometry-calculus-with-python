"""
Run every Python program of the book "Analytic Geometry and Calculus with Python".

For each program  code/chNN/name.py  the printed output is written to
code/chNN/name.out  (the same output that is printed in the book), and every
figure the program shows is saved in the folder  figures/  as  name.png
(name_2.png, ... if there are several).

Usage:
    python run_all.py            # run everything
    python run_all.py ch04       # run only Chapter 4
"""
import os
import runpy
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.join(ROOT, "code")
FIGS = os.path.join(ROOT, "figures")


def run_one(path):
    """Run a single program, saving figures instead of opening windows."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    stem = os.path.splitext(os.path.basename(path))[0]
    count = [0]

    def save(*args, **kwargs):
        for num in plt.get_fignums():
            count[0] += 1
            suffix = "" if count[0] == 1 else f"_{count[0]}"
            plt.figure(num).savefig(os.path.join(FIGS, f"{stem}{suffix}.png"),
                                    dpi=120, bbox_inches="tight")
        plt.close("all")

    plt.show = save
    runpy.run_path(path, run_name="__main__")
    save()


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--one":
        run_one(sys.argv[2])
        return
    only = sys.argv[1:]
    os.makedirs(FIGS, exist_ok=True)
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    failures = []
    t0 = time.time()
    for chap in sorted(os.listdir(CODE)):
        if only and chap not in only:
            continue
        cdir = os.path.join(CODE, chap)
        if not os.path.isdir(cdir):
            continue
        for fname in sorted(os.listdir(cdir)):
            if not fname.endswith(".py"):
                continue
            path = os.path.join(cdir, fname)
            res = subprocess.run([sys.executable, os.path.abspath(__file__), "--one", path],
                                 cwd=cdir, env=env, capture_output=True, text=True,
                                 encoding="utf-8", timeout=300)
            out = res.stdout.replace("\r\n", "\n").rstrip()
            if out:
                with open(path[:-3] + ".out", "w", encoding="utf-8") as fh:
                    fh.write(out + "\n")
            status = "ok " if res.returncode == 0 else "ERR"
            print(f"[{status}] {chap}/{fname}")
            if res.returncode != 0:
                failures.append(f"{chap}/{fname}")
                print(res.stderr)
    print(f"\n{len(failures)} failure(s) in {time.time() - t0:.1f}s")
    for f in failures:
        print("   ", f)
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
