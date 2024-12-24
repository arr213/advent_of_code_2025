def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().splitlines()
    
        rules = [
            [int(num) for num in rule.split('|')] 
            for rule in lines if '|' in rule
        ]
        
        updates = [
            [int(num) for num in update.split(',')] 
            for update in lines if ',' in update
        ]
        
    return rules, updates


def build_rules_dict(rules):
    rules_dict = {}
    for rule in rules:
        if rule[1] not in rules_dict:
            rules_dict[rule[1]] = set()
        rules_dict[rule[1]].add(rule[0])

    return rules_dict


def is_correct_order(rules_dict, update):
    # Check that the order of the update numbers does not violate a case where
    # rule[0] appears anywhere after rule[1]
    for i in range(len(update) - 1):
        for j in range(i + 1, len(update)):
            if update[i] in rules_dict and update[j] in rules_dict[update[i]]:
                return False
    return True


def sum_valid_middle_pages(rules, updates):
    rules_dict = build_rules_dict(rules)

    # Filter out updates with incorrect order
    # and sum the middle page of what remains
    valid_updates = [
        update
        for update in updates
        if is_correct_order(rules_dict, update)
    ]

    # Add the middle page of each valid update
    total_sum = sum([u[len(u) // 2] for u in valid_updates])

    return total_sum


def sum_corrected_middle_pages(rules, updates):
    rules_dict = build_rules_dict(rules)

    # Filter out updates with correct order
    # and sum the middle page of what remains
    invalid_updates = [
        update
        for update in updates
        if not is_correct_order(rules_dict, update)
    ]

    # Correct the order of each invalid update
    for update in invalid_updates:
        for i in range(len(update) - 1):
            for j in range(i + 1, len(update)):
                if update[i] in rules_dict and update[j] in rules_dict[update[i]]:
                    update[i], update[j] = update[j], update[i]

    # Add the middle page of each valid update
    total_sum = sum([u[len(u) // 2] for u in invalid_updates])

    return total_sum


if __name__ == '__main__':
    rules, updates = read_input('solutions/05.txt')
    total_sum = sum_valid_middle_pages(rules, updates)
    print(total_sum == 4924)
    total_sum = sum_corrected_middle_pages(rules, updates)
    print(total_sum == 6085)
