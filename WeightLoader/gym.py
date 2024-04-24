class Gym:

    def __init__(self, unit="lbs", bar_weight=45):
        self.unit = unit
        self.bar_weight = bar_weight
        self.total_weight = bar_weight
        self.loaded_plates = []
        self.avail_plates = [45, 35, 25, 15, 10, 5, 2.5]

    def update_bar(self, target_weight):
        if target_weight == self.total_weight:
            return "Already perfectly loaded."
        elif target_weight < self.bar_weight:
            return "Can not go lower than bar weight."
        elif target_weight > self.bar_weight + 2 * sum(self.avail_plates):
            return "Can not go higher than bar weight + all plates."
        else:
            # dps = difference per side
            dps = abs(target_weight - self.total_weight) / 2

            # check if one can achieve weight by adding avail plates
            if (dps < 2.5) or (dps % 2.5 != 0):
                return "Can not achieve."

        if target_weight > self.total_weight:
            return self.load_bar(target_weight, dps)
        else:
            return self.unload_bar(target_weight, dps)

    def load_bar(self, target_weight, dps, removed_this_load=None):
        if removed_this_load is None:
            removed_this_load = []
        else:
            removed_this_load = removed_this_load
        added_this_load = []
        self.avail_plates = sorted(self.avail_plates, reverse=True)
        w_dps = dps
        for plate in self.avail_plates:
            if w_dps - plate >= 0:
                w_dps -= plate
                added_this_load.append(plate)
                if w_dps == 0.0:
                    break

        if w_dps != 0.0:
            added_this_load.clear()
            plate = self.loaded_plates.pop()
            self.avail_plates.append(plate)
            self.total_weight -= 2 * plate
            dps += plate
            removed_this_load.append(plate)
            return self.load_bar(target_weight, dps, removed_this_load)
        else:
            for plate in added_this_load:
                self.loaded_plates.append(plate)
                self.avail_plates.remove(plate)
                self.total_weight += 2 * plate
            return f"Remove the following plates: {removed_this_load}. Add the following plates: {added_this_load} for a total of {int(self.total_weight)}{self.unit}."

    def unload_bar(self, target_weight, dps):
        removed_this_load = []
        w_dps = dps
        for i in range(len(self.loaded_plates)-1, -1, -1):
            plate = self.loaded_plates[i]
            w_dps -= plate
            removed_this_load.append(plate)
            if w_dps <= 0.0:
                break

        for plate in removed_this_load:
            # self.loaded_plates.pop()
            self.total_weight -= 2 * plate
            self.avail_plates.append(plate)
        if w_dps != 0.0:
            return self.load_bar(target_weight, dps, removed_this_load)
        else:
            return f"Remove the following plates: {removed_this_load} a total of {int(self.total_weight)}{self.unit}."

    def display_bar(self):
        for i in range(len(self.loaded_plates)-1, -1, -1):
            print(f"({self.loaded_plates[i]})", end='')
        print("|-----------------------------|", end='')
        for i in range(len(self.loaded_plates)):
            print(f"({self.loaded_plates[i]})", end='')
        print()

        return f"There is {self.total_weight}{self.unit} loaded onto the bar with the following plates on each side: {self.loaded_plates}."