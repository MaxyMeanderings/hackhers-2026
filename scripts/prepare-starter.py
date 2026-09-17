"""Package only the student starter and synchronize its public handouts."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
STARTER = ROOT / "starter"
PUBLIC = ROOT / "slides" / "public"
FILES = ("README.md", "BUILD-BRIEF.md", "BUILD-STEPS.md", ".gitignore")


def main():
    actual = {path.name for path in STARTER.iterdir()}
    if actual != set(FILES):
        raise SystemExit("Starter must contain only README, brief, build steps, and ignore rules.")
    if (PUBLIC / "coach").exists():
        raise SystemExit("Completed coach files must not be bundled with the student site.")
    handouts = PUBLIC / "walkthrough"
    handouts.mkdir(parents=True, exist_ok=True)
    for source, target in (("BUILD-BRIEF.md", "BUILD-BRIEF.md"),
                           ("BUILD-STEPS.md", "CLAUDE-CODE-STEPS.md")):
        (handouts / target).write_bytes((STARTER / source).read_bytes())
    archive = PUBLIC / "hackhers-starter.zip"
    with ZipFile(archive, "w", compression=ZIP_DEFLATED) as bundle:
        for name in FILES:
            info = ZipInfo("hackhers-starter/" + name, date_time=(2026, 9, 16, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, (STARTER / name).read_bytes())
    with ZipFile(archive) as bundle:
        assert set(bundle.namelist()) == {"hackhers-starter/" + name for name in FILES}
        assert bundle.testzip() is None
    print("Prepared student starter: 4 files, no completed implementation.")


if __name__ == "__main__":
    main()
