import os


class Checker:
    def run(self):
        print("Compiling the project")
        os.system("python -m compileall -q .")
        print("Running Tests")
        os.system("pytest")
        print("Running type checker")
        os.system("mypy . ")
        print("Formatting the project")
        os.system("black . ")


def main():
    import fire

    fire.Fire(Checker)


if __name__ == "__main__":
    main()
