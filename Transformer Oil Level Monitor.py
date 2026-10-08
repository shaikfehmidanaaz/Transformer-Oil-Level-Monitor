class TransformerOilLevelMonitor:

    def __init__(self, tank_capacity, minimum_level):
        self.tank_capacity = tank_capacity
        self.minimum_level = minimum_level

    def calculate_level_percentage(self, oil_level):
        if self.tank_capacity <= 0:
            return 0

        return (oil_level / self.tank_capacity) * 100

    def check_oil_level(self, oil_level):
        percentage = self.calculate_level_percentage(oil_level)

        if oil_level < 0:
            return "INVALID OIL LEVEL"

        elif oil_level > self.tank_capacity:
            return "OVERFLOW"

        elif oil_level < self.minimum_level:
            return "LOW OIL LEVEL"

        else:
            return "NORMAL"

    def display_status(self, oil_level):
        percentage = self.calculate_level_percentage(oil_level)
        status = self.check_oil_level(oil_level)

        print("----- Transformer Oil Level Monitor -----")
        print(f"Tank Capacity       : {self.tank_capacity:.2f} L")
        print(f"Oil Level           : {oil_level:.2f} L")
        print(f"Oil Level Percentage: {percentage:.2f}%")
        print(f"Minimum Oil Level   : {self.minimum_level:.2f} L")
        print(f"Status              : {status}")

        if status == "LOW OIL LEVEL":
            print("WARNING: Transformer oil level is LOW!")
            print("Action: Check for leakage and refill oil.")

        elif status == "OVERFLOW":
            print("WARNING: Oil level exceeds tank capacity!")

        elif status == "INVALID OIL LEVEL":
            print("ERROR: Invalid oil level entered.")

        else:
            print("Transformer oil level is NORMAL.")


# Example
tank_capacity = 1000       # Liters
minimum_level = 600        # Liters
current_oil_level = 750    # Liters

monitor = TransformerOilLevelMonitor(
    tank_capacity,
    minimum_level
)

monitor.display_status(current_oil_level)
