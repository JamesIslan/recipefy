from pytest import mark

from utils.pagination import make_pagination_range


@mark.parametrize(
    'current_page, expected_output',
    [
        (1, [1, 2, 3, 4]),  # Initial range
        (2, [1, 2, 3, 4]),  # Initial range
        (6, [5, 6, 7, 8]),  # Middle range
        (9, [8, 9, 10, 11]),  # Middle range
        (14, [12, 13, 14, 15]),  # End range
        (15, [12, 13, 14, 15]),  # End range
    ],
)
def test_make_pagination_range_returns_pagination_range(current_page, expected_output):
    pagination = make_pagination_range(
        page_range=list(range(1, 16)),
        page_qty=4,
        current_page=current_page,
    )
    assert pagination['pagination'] == expected_output
