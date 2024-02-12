import typer

app = typer.Typer()


@app.command()
def keygen() -> None:
    typer.echo("Implement your keygen for crackme_651db8f78b6aa566ae7234ec here.")


if __name__ == "__main__":
    app()
