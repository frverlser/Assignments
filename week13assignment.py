from abc import ABC, abstractmethod


class Package(ABC):
    def __init__(self, subscriber):
        self.subscriber = subscriber
    @abstractmethod
    def amount(self):
        pass
class Small(Package):  
    def amount(self):
        return 10000
class Medium(Package):
    def amount(self):
        return 30000
class Large(Package):
    def amount(self):
        return 70000

class TopupService:
    def __init__(self):
        self.topups = []  
    def add(self, package: Package):
        return self.topups.append(package)
    def run(self, receipt, confirmation):
        receipt.write(self.topups)
        confirmation.confirm(self.topups)

class Receipt(ABC):
    @abstractmethod
    def write(self, topups):
        pass

class TextReceipt(Receipt):
    def write(self, topups):
        for topup in topups:
            print(f"RECEIPT: {topup.subscriber} +{topup.amount()}")

class Confirmation(ABC):
    @abstractmethod
    def confirm(self, topups):
        pass

class SmsConfirmation(Confirmation):
    def confirm(self, topups):
        for topup in topups:
            print(f"[SMS → {topup.subscriber}] Top-up of {topup.amount()} so'm successful")


carrier = TopupService()
carrier.add(Small("Peter"))
carrier.add(Medium("Natasha"))
carrier.add(Large("Bruce"))

carrier.run(TextReceipt(), SmsConfirmation())


# RECEIPT: Peter +10000
# RECEIPT: Natasha +30000
# RECEIPT: Bruce +70000
# [SMS → Peter] Top-up of 10000 so'm successful
# [SMS → Natasha] Top-up of 30000 so'm successful
# [SMS → Bruce] Top-up of 70000 so'm successful