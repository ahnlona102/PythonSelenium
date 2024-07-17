import unittest
import multiprocessing
from XTestRunner import HTMLTestRunner

from create_account_test import CreateAccountTest
from login_test import LoginTest
from logout_test import LogoutTest

# List of test classes to run
test_classes = [LoginTest, LogoutTest, CreateAccountTest]


def run_tests(test_class):
    try:
        suite = unittest.TestLoader().loadTestsFromTestCase(test_class)

        report_file = f'reports/{test_class.__name__}_result.html'

        with open(report_file, 'wb') as fp:
            runner = HTMLTestRunner(
                tester='Loan Le',
                stream=fp,
                title=f'Test Report - {test_class.__name__}',
                description=f'Test Description for {test_class.__name__}',
                language='en',
            )
            runner.run(suite)

    except Exception as e:
        print(f"Error running {test_class.__name__} tests: {e}")


if __name__ == '__main__':
    # Number of parallel processes
    num_processes = 4

    # Create a process pool
    pool = multiprocessing.Pool(processes=num_processes)

    try:
        # Run tests in parallel
        pool.map(run_tests, test_classes)
    except Exception as e:
        print(f"Error in multiprocessing: {e}")
    finally:
        # Close the pool
        pool.close()
        pool.join()
