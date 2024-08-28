import typer
import os
from app.certificate_manager import CertificateManager

app = typer.Typer()
cert_manager = CertificateManager("berjan@bruens.it", "/app/letsencrypt")
DOMAINS_FILE = "/app/data/domains.txt"

def load_domains():
    if os.path.exists(DOMAINS_FILE):
        with open(DOMAINS_FILE, "r") as f:
            return [line.strip() for line in f if line.strip()]
    return []

def save_domain(domain):
    domains = load_domains()
    if domain not in domains:
        with open(DOMAINS_FILE, "a") as f:
            f.write(f"{domain}\n")
        typer.echo(f"Domain {domain} added to the list.")
    else:
        typer.echo(f"Domain {domain} is already in the list.")


@app.command()
def add_domain(domain: str):
    save_domain(domain)
    try:
        cert_manager.add_domain(domain)
        typer.echo(f"Certificate for {domain} has been created successfully.")
    except Exception as e:
        typer.echo(f"Failed to create certificate for {domain}. Error: {str(e)}")

@app.command()
def list_domains():
    domains = load_domains()
    if domains:
        typer.echo("Registered domains:")
        for domain in domains:
            typer.echo(f"- {domain}")
    else:
        typer.echo("No domains registered yet.")

@app.command()
def renew_certificates():
    domains = load_domains()
    if not domains:
        typer.echo("No domains registered. Nothing to renew.")
        return
    
    try:
        cert_manager.renew_certificates()
        typer.echo("All certificates have been renewed successfully.")
    except Exception as e:
        typer.echo(f"Failed to renew certificates. Error: {str(e)}")

@app.command()
def check_cert_status(domain: str):
    cert_path = os.path.join("/app/letsencrypt", "live", domain, "fullchain.pem")
    if os.path.exists(cert_path):
        typer.echo(f"Certificate for {domain} exists.")
    else:
        typer.echo(f"No certificate found for {domain}.")

if __name__ == "__main__":
    app()
