import os
import subprocess


class FastCheck:
    project_path = None

    def run(self, path=None, mypy_enabled=False):
        if path:
            # change directory
            os.chdir(path)

        print("Compiling the project")
        os.system(f"python -m compileall -q {path}")

        if mypy_enabled:
            print("Running type checker")
            os.system(f"mypy {path} ")
        print("Running ruff")
        os.system("ruff clean")
        os.system(f"ruff format {path} ")
        os.system(f"ruff check {path} --fix")

        if not os.path.exists("tests"):
            print("No tests folder found")

        print("Running Tests")
        os.system("pytest")

        print("Done!")

    def select_and_run(self):
        project = subprocess.check_output(
            "cd /Users/jean.machado/projects ; ls | /Users/jean.machado/.fzf/bin/fzf ",
            shell=True,
            text=True,
        )
        self.set_current_project(f"/Users/jean.machado/projects/{project.strip()}")

        self.run()

    def run_current_project(self):
        self.run(self.get_current_project())

    def set_current_project(self, project_path: str):
        from tiny_data_warehouse import DataWarehouse

        # write event
        tdw = DataWarehouse()
        tdw.write_event("fast_check_current_project", {"path": project_path})

    def get_current_project(self):
        from tiny_data_warehouse import DataWarehouse

        # write event
        tdw = DataWarehouse()
        project_path = (
            tdw.event("fast_check_current_project").iloc[-1].to_dict()["path"]
        )

        print("Current project: ", project_path)

        return project_path


def main():
    import fire

    fire.Fire(FastCheck)


if __name__ == "__main__":
    main()
