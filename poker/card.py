# from typing import Tuple

# class Card():
#     SUITS: list[str] = ("Hearts", "Clubs", "Spades", "Diamonds")

#     RANKS: Tuple[str] = (
#                 "2", "3", "4", "5", "6", "7", "8", "9", "10",
#                 "Jack", "Queen", "King", "Ace"
#             )
    
#     @classmethod
#     def create_standard_52_cards(cls):
#         return [
#             cls(rank=rank, suit=suit)
#             for suit in cls.SUITS
#             for rank in cls.RANKS
#         ]
    
#         # cards = []
#         # for suit in cls.SUITS:
#         #     for rank in cls.RANKS:
#         #         cards.append(cls(rank=rank, suit=suit))
#         # return cards

#     def __init__(self, rank:str, suit:str):
#         if rank not in self.RANKS:
#             raise ValueError(f"Invalid rank. Rank must be one of the following: {self.RANKS}")

#         if suit not in self.SUITS:
#             raise ValueError(f"Invalid suit. Suit must be one of the following: {self.SUITS}")

#         self.rank = rank
#         self.suit = suit

#     def __str__(self):
#         return f"{self.rank} of {self.suit}"

#     def __repr__(self):
#         return f"Card('{self.rank}', '{self.suit}')"
    
#     def __eq__(self, value):
#         if not isinstance(value, Card):
#             return NotImplemented
#         return self.rank == value.rank and self.suit == value.suit
    
from __future__ import annotations

from typing import ClassVar, Literal, Tuple, Type, TypeVar, List

CardSuit = Literal["Hearts", "Clubs", "Spades", "Diamonds"]
CardRank = Literal[
    "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "Jack", "Queen", "King", "Ace",
]

TCard = TypeVar("TCard", bound=Card)


class Card():
    SUITS: ClassVar[Tuple[CardSuit, ...]] = ("Hearts", "Clubs", "Spades", "Diamonds")

    RANKS: ClassVar[Tuple[CardRank, ...]] = (
        "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "Jack", "Queen", "King", "Ace"
    )

    @classmethod
    def create_standard_52_cards(cls: Type[TCard]) -> List[TCard]:
        return [
            cls(rank=rank, suit=suit)
            for suit in cls.SUITS
            for rank in cls.RANKS
        ]

    def __init__(self, rank: CardRank, suit: CardSuit) -> None:
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank. Rank must be one of the following: {self.RANKS}")

        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit. Suit must be one of the following: {self.SUITS}")

        self.rank: CardRank = rank
        self.suit: CardSuit = suit

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def __repr__(self) -> str:
        return f"Card('{self.rank}', '{self.suit}')"

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Card):
            return NotImplemented
        return self.rank == value.rank and self.suit == value.suit

