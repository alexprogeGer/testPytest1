import pytest

@pytest.fixture(params=[
    ([1, 2, 2, 3], [1, 2, 3]),
    ([-5, -4, -5, -16], [-16, -5, -4]),
    ([], []),
])
def sort_and_unique(request):
    return request.param
