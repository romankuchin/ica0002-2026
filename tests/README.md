# (experimental) Add tests to your repository

Copy `run-tests.sh` to your repository, make it executable, commit and push to GitHub:

	wget https://raw.githubusercontent.com/romankuchin/ica0002-2026/refs/heads/tests/tests/run-tests.sh
	chmod +x run-tests.sh

	git add run-tests.sh
	git commit -m 'Add tests'
	git push

You're all set! Now you can run `./run-tests.sh` any time to test your solution.

Feel free to update the script in your repository to better match your needs. Make sure to commit and push the changes!

Test cases are available [here](https://github.com/romankuchin/ica0002-2026/blob/tests/tests/test_all.py); we'll update them for (almost) every lab, and the script will download the updated version to your repository.


# (experimental) Configure automatic tests in your repository

Create GitHub actions directory:

	mkdir -p .github/workflows

Add test workflow:

	wget https://raw.githubusercontent.com/romankuchin/ica0002-2026/refs/heads/tests/tests/.github/workflows/test.yaml -P .github/workflows

Commit and push the changes:

	git add .github
	git commit -m 'Add tests'
	git push

Once these changes are pushed (or merged) to the `main` branch, tests will be run automatically every time you update the `main` branch from now on.

You can find the results in Actions --> Test in your course repository; "Run tests" step shows the test results.

Test cases are available [here](https://github.com/romankuchin/ica0002-2026/blob/tests/tests/test_all.py); we'll update them for (almost) every lab.

More info on GitHub actions [here](https://docs.github.com/en/actions/get-started/quickstart).
