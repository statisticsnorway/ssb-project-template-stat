from pathlib import Path
import shutil

altinn_folder = Path("src") / "altinn"

altinn_enabled = {{ cookiecutter.altinn }}

TEMPLATE_PATHS = {
    Path("README.md"),
    Path("form_export.py"),
    Path("app/app.py"),
    Path("app/app-config/app.yaml"),
    Path("processing/automation.py"),
    Path("processing/form_processing.py"),
}

def is_template_only(directory: Path) -> bool:
    actual = {
        path.relative_to(directory)
        for path in directory.rglob("*")
        if path.is_file()
    }

    for file in actual:
        if file not in TEMPLATE_PATHS:
            return False

    return True

if not altinn_enabled and altinn_folder.exists():
    if is_template_only(altinn_folder):
        shutil.rmtree(altinn_folder)
    else:
        raise RuntimeError(
            f"{altinn_folder} contains files not owned by the template; "
            "refusing to delete it."
        )