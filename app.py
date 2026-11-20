import os

def main():
    print("Proyecto de seguridad de credenciales")
    print("Cloud Computing")

    api_key = os.getenv("API_KEY")

    if api_key:
        print("Variable de entorno configurada.")
    else:
        print("No se encontró la variable API_KEY.")

if __name__ == "__main__":
    main()
