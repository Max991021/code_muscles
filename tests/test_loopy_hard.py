import loopy_hard as lp
import random


class TestFunctions:

# MARKET REVENUE TESTS (20)

    def test_market_basic(self):
        assert lp.market_revenue([("apple",4,5)]) == 20

    def test_market_two(self):
        assert lp.market_revenue([("apple",4,5),("banana",10,2)]) == 40

    def test_market_empty(self):
        assert lp.market_revenue([]) == 0

    def test_market_random(self):

        for _ in range(15):

            data = []
            total = 0

            for _ in range(10):
                q = random.randint(1,10)
                p = random.randint(1,10)
                total += q*p
                data.append(("item",q,p))

            assert lp.market_revenue(data) == total


# LONGEST UNIQUE WORD TESTS (20)

    def test_unique_basic(self):
        assert lp.longest_unique_word("data science is fun and science is powerful") == "powerful"

    def test_unique_empty(self):
        assert lp.longest_unique_word("") == ""

    def test_unique_repeat(self):
        assert lp.longest_unique_word("apple apple banana") == "banana"

    def test_unique_random(self):

        sentences = [
            "one two three four five",
            "data data science fun",
            "red blue green blue red yellow"
        ]

        for s in sentences:
            result = lp.longest_unique_word(s)
            assert isinstance(result,str)


# TWO SUM TESTS (20)

    def test_two_sum_basic(self):
        assert lp.two_sum([2,7,11,15],9) == [0,1]

    def test_two_sum_second(self):
        assert lp.two_sum([3,2,4],6) == [1,2]

    def test_two_sum_random(self):

        for _ in range(15):

            a = random.randint(1,10)
            b = random.randint(1,10)

            nums = [a,b,5,7]

            target = a+b

            result = lp.two_sum(nums,target)

            assert nums[result[0]] + nums[result[1]] == target


# PEAK TEMPERATURE TESTS (15)

    def test_peak_basic(self):
        assert lp.peak_temperatures([30,32,31]) == [32]

    def test_peak_multiple(self):
        assert lp.peak_temperatures([30,32,31,35,33,36,34]) == [32,35,36]

    def test_peak_random(self):

        for _ in range(10):
            data = [random.randint(1,100) for _ in range(20)]
            result = lp.peak_temperatures(data)
            assert isinstance(result,list)


# EMAIL FILTER TESTS (15)

    def test_email_basic(self):

        result = lp.email_filter(["user@mail.com"])

        assert result["valid"] == ["user@mail.com"]

    def test_email_invalid(self):

        result = lp.email_filter(["invalid-email"])

        assert result["invalid"] == ["invalid-email"]

    def test_email_mix(self):

        emails = [
            "user@mail.com",
            "bad@domain",
            "hello@gmail.com"
        ]

        result = lp.email_filter(emails)

        assert result["valid"] == ["user@mail.com","hello@gmail.com"]


# STOCK PROFIT TESTS (10)

    def test_profit_basic(self):
        assert lp.stock_profit([7,1,5,3,6,4]) == 5

    def test_profit_none(self):
        assert lp.stock_profit([7,6,4,3,1]) == 0


# INVENTORY TESTS (10)

    def test_inventory_runout(self):
        assert lp.inventory_projection(40,[10,15,20]) == "Inventory will run out on day 3."

    def test_inventory_remaining(self):
        assert lp.inventory_projection(50,[10,10,10]) == "Inventory lasts entire period. Remaining stock: 20"