from interpreter import run_code

def main():
    with open("samples/hello.ved", "r", encoding="utf-8") as f:
        lines = f.readlines()
    run_code(lines)

if __name__ == "__main__":
    main()
