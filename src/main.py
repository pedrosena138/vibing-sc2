from sc2 import maps
from sc2.data import Difficulty, Race
from sc2.main import run_game
from sc2.player import Bot, Computer

from bot import VibeBot


def main() -> None:
    players = [
        Bot(Race.Terran, VibeBot()),
        Computer(Race.Zerg, Difficulty.Easy),
    ]
    run_game(maps.get("AcropolisLE"), players=players, realtime=False)


if __name__ == "__main__":
    main()
