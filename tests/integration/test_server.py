from mocks.mock_bot import MockBot
from sc2.data import Difficulty, Race
from sc2.player import Bot, Computer

from main import maps, run_game


def test_initialization(capfd):
    """
    GIVEN I'm a player
    WHEN the game server starts
    THEN I want to be able to verify the server status.
    AND verify the game logs.
    """
    players = [
        Bot(Race.Zerg, MockBot()),
        Computer(Race.Terran, Difficulty.VeryEasy),
    ]
    game_result = run_game(maps.get("Flat32"), players=players, realtime=False)

    # THEN: Verify the server status
    assert game_result is not None
    assert game_result.name == "Defeat"

    # Capture stdout/stderr to verify logs
    captured = capfd.readouterr()

    # AND: Verify the game logs (using captured output)
    assert "Creating new game" in captured.out
    assert "Flat32" in captured.out
    assert "Hi from step: 0" in captured.out
