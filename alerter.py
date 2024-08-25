alert_failure_count = 0

def network_alert_stub(celcius, fail=False):
    print(f'ALERT: Temperature is {celcius} celcius')
    if fail:
        return 500  # Simulate network failure
    return 200  # Simulate successful alert

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        # Update failure count correctly
        global alert_failure_count
        alert_failure_count += 1

# Tests
def test_alert_failure_handling():
    global alert_failure_count
    
    # Reset failure count before the test
    alert_failure_count = 0

    # Test successful alert
    network_alert_stub = lambda celcius: 200  # Success stub
    alert_in_celcius(400.5)
    assert alert_failure_count == 0, "Failure count should be 0 on success"

    # Test failure alert
    network_alert_stub = lambda celcius: 500  # Failure stub
    alert_in_celcius(303.6)
    alert_in_celcius(150.0)
    assert alert_failure_count == 2, "Failure count should be 2 on failure"

    print("test_alert_failure_handling() passed!")

# Run the test
test_alert_failure_handling()

print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')

