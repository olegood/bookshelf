import time

import pytest


def pytest_addoption(parser):
    parser.addoption("--logtime", action="store_true", help="Log test time", default=False)


@pytest.fixture(autouse=True)
def log_time(request):
    enabled = request.config.getoption("--logtime")

    if enabled:
        start = time.perf_counter()

    yield

    if enabled:
        elapsed = time.perf_counter() - start
        test_id = getattr(request.node, "nodeid", "unknown")
        print(f" [logtime] {elapsed:.2f}s: {test_id}", flush=True)
