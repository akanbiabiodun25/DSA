
import otter

grader = otter.Notebook(tests_dir="tests")

grader.check_all()


grader.export(run_tests=True)