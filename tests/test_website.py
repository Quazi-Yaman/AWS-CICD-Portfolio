from pathlib import Path


def test_frontend_files_exist():
    project_root = Path(__file__).resolve().parent.parent
    frontend = project_root / "frontend"

    assert (frontend / "index.html").exists()
    assert (frontend / "style.css").exists()
    assert (frontend / "script.js").exists()


def test_index_contains_project_title():
    project_root = Path(__file__).resolve().parent.parent
    index_file = project_root / "frontend" / "index.html"

    content = index_file.read_text(encoding="utf-8")

    assert "THIS SHOULD FAIL" in content


def test_index_contains_cicd_project():
    project_root = Path(__file__).resolve().parent.parent
    index_file = project_root / "frontend" / "index.html"

    content = index_file.read_text(encoding="utf-8")

    assert "AWS CI/CD Portfolio" in content
