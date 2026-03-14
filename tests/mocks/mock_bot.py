"""Mock classes for BotAI and related components."""

from sc2.bot_ai import BotAI


class MockBot(BotAI):
    """A mock Bot class for testing without requiring a real game."""

    async def on_step(self, iteration: int):
        """Handle each game step."""
        print(f"Hi from step: {iteration}")
        await self.client.leave()
