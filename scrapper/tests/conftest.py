import time

import pytest


def pytest_addoption(parser):
    parser.addoption("--logtime", action="store_true", help="Log test time", default=False)


@pytest.fixture(autouse=True)
def log_time(request):
    """
    log_time is a pytest fixture that automatically gets applied to every test function. It is used
    to measure and log the execution time of test functions if the logging is enabled via a
    command-line option. The fixture records the time at the start of the test function execution
    and displays the elapsed time upon completion of the test.

    :param request: A pytest request object that provides access to the test node and configuration
        details.
    :return: None
    """
    enabled = request.config.getoption("--logtime")

    if enabled:
        start = time.perf_counter()

    yield

    if enabled:
        elapsed = time.perf_counter() - start
        test_id = getattr(request.node, "nodeid", "unknown")
        print(f" [logtime] {elapsed:.2f}s: {test_id}", flush=True)
