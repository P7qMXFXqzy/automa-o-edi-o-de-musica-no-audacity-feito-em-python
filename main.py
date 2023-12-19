def main():
    import mecanicas
    continuar = None
    while(continuar != "n"):
        mecanicas.funcaoPrincipal()
        continuar = input("continuar? (s/n) ")
        while (continuar != "s" and continuar != "n"):
            continuar = input("valor inválido!\ncontinuar? (s/n) ")

# This block ensures that the main method is only called if the script is executed directly
if __name__ == "__main__":
    main()
