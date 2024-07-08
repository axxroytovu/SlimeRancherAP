import typing
from dataclasses import dataclass
from Options import DeathLink, PerGameCommonOptions

@dataclass
class SlimeOptions(PerGameCommonOptions):
    death_link: DeathLink
