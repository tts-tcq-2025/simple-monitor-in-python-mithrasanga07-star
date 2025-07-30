
def check_in_range(value, lower, upper, message):
    if not (lower < value < upper):
        print(f'{message} is out of range!')
        return False
    return True

def battery_is_ok(temperature, soc, charge_rate):
    checks = [
        check_in_range(temperature, 0, 45, 'Temperature'),
        check_in_range(soc, 20, 80, 'State of Charge'),
        check_in_range(charge_rate, 0, 0.8, 'Charge Rate')  # 0 is min here for clarity
    ]
    return all(checks)

if __name__ == '__main__':
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)
