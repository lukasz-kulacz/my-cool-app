from my_package import hello

def cli_entrypoint():
    print(hello())

if __name__ == "__main__":
    cli_entrypoint()