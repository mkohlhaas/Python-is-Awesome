import nox

nox.options.sessions = ["format_riff"]


@nox.session(
    # python=["3.13" "3.10"],
    # reuse_venv=True,
    venv_backend="uv",
)
def format_black(session: nox.Session):
    session.install("black")
    # session.install("-U", "black")  # for reuse_venv=True
    session.run("black", ".")


@nox.session(venv_backend="uv")
def format_riff(session: nox.Session):
    session.install("ruff")
    session.run("ruff", "format", ".")


@nox.session(venv_backend="uv")
@nox.parametrize("version", ["5.3.0", "5.2.1", "5.1.1"])
def analytix(session: nox.Session, version: str):
    session.install(f"analytix=={version}")
    session.run("python", "-m", "analytix")
