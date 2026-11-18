
def transfer_air(source, target, amount):
    before = source.get_bar()

    source.release(amount)

    after = source.get_bar()

    if before - after == amount and amount > 0:
        target.fill(amount)
