#!/usr/bin/env python3
import typer
from rich import print
from transformers import pipeline

app = typer.Typer(help="Fantasy Name Generator")
generator = pipeline("text-generation", model="gpt2", device=-1)

@app.command()
def name(type: str = typer.Option("character", help="Type: character, place, item")):
    prompt = f"Tell me a girl name"
    result = generator(prompt, max_length=25, truncation=True)[0]["generated_text"].replace(prompt, "").strip()
    print(f"[bold cyan]{result}[/bold cyan]")

if __name__ == "__main__":
    app()