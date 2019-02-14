class Job:

    def __init__(self, extra_margin = False):
        self.extra_margin = extra_margin
        self.goods = []

    def add_new_good(self, good):
        self.goods.append(good)

    def count_total(self, total = 0):
        for good in self.goods:
            if self.extra_margin == 'extra-margin\n':
                almost_total = good.price*0.16
            else:
                almost_total = good.price*0.11
            self.total = good.price + almost_total
        return

    def __str__(self):
        return "total:" + self.total
