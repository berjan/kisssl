import typer
from app.cli import (
    add_domain,
    list_domains,
    renew_certificates,
    check_cert_status,
    load_domains,
    save_domain
)

def interactive_menu():
    while True:
        print("\nSSL Certificate Management Tool")
        print("1. Add a domain")
        print("2. Show all domains")
        print("3. Renew certificates")
        print("4. Check certificate status")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            domain = input("Enter the domain name: ")
            save_domain(domain)
            add_domain(domain)
        elif choice == '2':
            list_domains()
        elif choice == '3':
            renew_certificates()
        elif choice == '4':
            domain = input("Enter the domain name to check: ")
            check_cert_status(domain)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def main(interactive: bool = typer.Option(False, "--interactive", "-i")):
    if interactive:
        interactive_menu()
    else:
        typer.echo("Use --interactive or -i flag for interactive mode")
        typer.echo("Or use the following commands:")
        typer.echo("  add-domain DOMAIN")
        typer.echo("  list-domains")
        typer.echo("  renew-certificates")
        typer.echo("  check-cert-status DOMAIN")

if __name__ == "__main__":
    typer.run(main)
