from math import ceil


def make_pagination_range(
    page_range: list,
    page_qty: int,
    current_page: int,
) -> dict:
    page_total = len(page_range)
    middle_range = ceil(page_qty / 2)
    start_range = current_page - middle_range
    end_range = current_page + middle_range
    start_range_offset = end_range_offset = 0

    if start_range < 0:
        start_range_offset = abs(start_range)
        start_range += start_range_offset
        end_range += start_range_offset
    if end_range > page_total:
        end_range_offset = end_range - page_total
        start_range -= end_range_offset

    pagination = page_range[start_range:end_range]

    return {
        'pagination': pagination,
        'page_range': page_range,
        'qty_pages': page_qty,
        'current_page': current_page,
        'total_pages': page_total,
        'start_range': start_range,
        'stop_range': end_range,
        'first_page_out_of_range': current_page > middle_range,
        'last_page_out_of_range': end_range < page_total,
    }
