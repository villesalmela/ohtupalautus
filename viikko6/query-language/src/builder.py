from matchers import All, PlaysIn, HasAtLeast, HasFewerThan, And, Or
from typing import Self

class QueryBuilder:
    def __init__(self, query=All()) -> None:
        self._query_object = query

    def playsIn(self, team) -> Self:
        return QueryBuilder(And(PlaysIn(team), self._query_object))
    
    def hasFewerThan(self, count, item) -> Self:
        return QueryBuilder(And(HasFewerThan(count, item), self._query_object))
    
    def hasAtLeast(self, count, item) -> Self:
        return QueryBuilder(And(HasAtLeast(count, item), self._query_object))
    
    def oneOf(self, *matchers) -> Self:
        return QueryBuilder(And(Or(*matchers), self._query_object))

    def build(self):
        return self._query_object