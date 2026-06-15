import re
from typing import Literal, List, Union

# Idea from from https://github.com/realvitya/pyfortinet/tree/master

OP = {
    "eq": "==",
    "neq": "!=",
    "lt": "<",
    "le": "<=",
    "gt": ">",
    "ge": ">=",
    "or": "&",
    "in": "in",
    "contain": "contain",
    "like": "like",
    "not_like": "!like",
    "glob": "glob",
    "not_glob": "!glob",
}

FiltersType = Union["F", "FilterList", "ComplexFilter"]

class F:
    """Filter class that allows us to define a single filter for an object

    Argument format is {field}={value} or {field}__{operator}={value}
    Only one argument can be passed!

    Attributes:
        negate (bool): If true the filter is negated
        source (str): The source is the API attribute we are looking at
        op (str): The operator for the search
        targets (str): The target is the value we are searching for
    """

    negate: bool = False
    source: str = ""
    op: str = ""
    targets: Union[List[Union[int, str]], Union[int, str]]

    def __init__(self, **kwargs):
        """Filter initialization"""
        if len(kwargs) > 1:
            raise ValueError("F only accepts one filter condition at a time!")
        
        # support things like switch-id by using underscore, and then replacing it
        rx = re.compile(r'([a-zA-Z0-9])(_)([a-zA-Z0-9])')
        kwargs = { rx.sub(r"\g<1>-\g<3>", key):value for key, value in kwargs.items() }

        for key, value in kwargs.items():
            if "__" in key:
                self.source, self.op = key.split("__")
                if self.op not in OP:
                    raise ValueError(f"Unknown operation: '{self.op}' !")
                self.op = OP[self.op]
            else:
                self.source = key
                self.op = "=="
            self.targets = value

    def generate(self) -> List[str]:
        """Generate API filter list"""
        out = []
        if self.negate:
            out.append("!")
        out.append(self.source)
        out.append(self.op)
        if isinstance(self.targets, list):
            out.extend(self.targets)
        else:
            out.append(self.targets)
        return out

    def __and__(self, other) -> "ComplexFilter":
        return ComplexFilter(self, "&&", other)

    def __or__(self, other) -> "ComplexFilter":
        return ComplexFilter(self, "||", other)

    def __invert__(self):
        self.negate = not self.negate
        return self

    def __add__(self, other: Union["F", "FilterList"]):
        return FilterList(self, other)


class FilterList:
    """List of F objects"""

    members: list[F]

    def __init__(self, *members: Union[F, "FilterList"]):
        self.members = []
        for member in members:
            self + member

    def __add__(self, other: Union[F, "FilterList"]):
        if isinstance(other, F):
            self.members.append(other)
        elif isinstance(other, FilterList):
            self.members.extend(other.members)
        else:
            raise ValueError(f"Elements '{other}' can't be added to FilterList")
        return self

    def __and__(self, other) -> "ComplexFilter":
        return ComplexFilter(self, "&&", other)

    def __or__(self, other) -> "ComplexFilter":
        return ComplexFilter(self, "||", other)

    def __len__(self):
        return len(self.members)

    def generate(self) -> List[List[str]]:
        """Generate API filter output"""
        return [member.generate() for member in self.members]


class ComplexFilter:
    """Complex handling of filters and their operator"""

    def __init__(
        self,
        a: Union["ComplexFilter", FilterList, F],
        op: Literal["||", "&&"],
        b: Union["ComplexFilter", FilterList, F],
    ):
        self.a = a
        self.op = op
        self.b = b

    def generate(self) -> list:
        """Generate API filter output"""
        out = [self.a.generate(), self.op, self.b.generate()]
        return out

    def __and__(self, other) -> "ComplexFilter":
        return ComplexFilter(self, "&&", other)

    def __or__(self, other):
        return ComplexFilter(self, "||", other)
