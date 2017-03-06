from math import sqrt


class AbCalc:

    def __init__(self):
        self._significance = .95
        self._power = .8

        self._zs_1s = 1.644853625  # One-tailed Z-value for statistical significance equal 0.95
        self._zs_2s = 1.959963986  # Two-tailed Z-value for statistical significance equal 0.95
        self._zp = .8416212327  # Two-tailed Z-value for statistical power equal 0.8

        self.is_significant = False
        self.effect_size = 0
        self.sample_size = 0

    def calculate(self, control_total, control_events, test_total, test_events, minimum_effect=.05):
        if control_total <= 0 or test_total <= 0:
            return

        p = test_events / test_total
        pc = control_events / control_total

        # One-tailed significance test
        z = (p - pc) / sqrt((p * (1 - p) / test_total) + (pc * (1 - pc) / control_total))

        if z > self._zs_1s:
            self.is_significant = True

        self.effect_size = round(p / pc - 1., 4)

        sd1 = sqrt(2 * pc * (1 - pc))
        sd2 = sqrt(pc * (1 - pc) + (pc + minimum_effect) * (1 - pc - minimum_effect))

        self.sample_size = round((self._zs_2s * sd1 + self._zp * sd2) ** 2 / minimum_effect ** 2)
