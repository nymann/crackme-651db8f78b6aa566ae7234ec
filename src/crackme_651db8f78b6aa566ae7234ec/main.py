import typer

from crackme_651db8f78b6aa566ae7234ec.key_generator import KeyGenerator

app = typer.Typer()


@app.command()
def keygen(keys_to_generate: int = 1) -> None:
    key_generator = KeyGenerator()
    for _ in range(keys_to_generate):
        typer.echo(key_generator.generate())


if __name__ == "__main__":
    app()
