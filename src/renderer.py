# Renderer
#
# Renders the game in console mode


from tabulate import tabulate


class Renderer:
    def renderBanner() -> None:
        print("------------------------")
        print("Welcome to NOT The Game!")
        print("------------------------")
        print()

    def renderAllCards(cards) -> None:
        headers = ["Card", "State"]
        values = [[card.value, card.state.value] for card in cards]
        table = tabulate(values, headers)
        print(table)
        print()
