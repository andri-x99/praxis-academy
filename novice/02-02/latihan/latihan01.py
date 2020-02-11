# uji coba 1
def test_sum1():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum1()
    print("Everything passed")
    print("")

# uji coba 2
def test_sum2():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple2():
    assert sum((1, 2, 2)) == 5, "Should be 6"

if __name__ == "__main__":
    test_sum2()
    test_sum_tuple2()
    print("Everything passed")