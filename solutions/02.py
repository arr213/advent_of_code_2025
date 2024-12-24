

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().splitlines()
        reports = [[int(num) for num in line.split(' ')] for line in lines]
    return reports


def is_valid_decreasing_sequence(report):
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if diff > -1 or diff < -3:  # Check if the difference is not between 1 and 3
            return False
    return True


def is_valid_increasing_sequence(report):
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if diff < 1 or diff > 3:  # Check if the difference is not between 1 and 3
            return False
    return True


def is_safe_report(report):
    return is_valid_decreasing_sequence(report) or \
        is_valid_increasing_sequence(report)


def count_safe_reports(reports) -> int:
    safe_reports = [
        report for report in reports
        if (is_safe_report(report))
    ]
    return len(safe_reports)


def count_damp_safe_reports(reports) -> int:
    safe_reports = [
        report for report in reports
        if (is_safe_report(report) or any(
            is_safe_report(report[:i] + report[i+1:])  # Remove each element one by one
            for i in range(len(report))
        ))

    ]

    return len(safe_reports)


if __name__ == '__main__':
    reports = read_input('solutions/02.txt')
    count_safe = count_safe_reports(reports)
    print(count_safe == 421)
    count_damp_safe = count_damp_safe_reports(reports)
    print(count_damp_safe == 476)
