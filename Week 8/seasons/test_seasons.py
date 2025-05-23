from seasons import Date

def test_valid_date():
    dob = Date("2000-01-01")
    assert dob.year == 2000
    assert dob.month == 1
    assert dob.day == 1
