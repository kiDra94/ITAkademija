from typing import Any, List, TypeVar, Dict

def first(container):
    return container[0]


def first2(container: List[Any]) -> Any:
    return container[0]

T = TypeVar("T")

def first3(container: List[T]) -> T:
    return container[0]

def first4(container: List[T]) -> T:
    print(container)
    return container[0] #return "a"  # mypy raises: Incompatible return value type (got "str", expected "T")

K = TypeVar("K")
V = TypeVar("V")


def get_item(key: K, container: Dict[K, V]) -> V:
    return container[key]

def get_first5(container: Dict[K, V]) -> K:
    return list(container.keys())[0]


def get_first6(container: Dict[K, V]) -> V:
    return list(container.values())[0] 

T1 = TypeVar("T1", str, int, float)  # T1 can only represent types of int and str


def first5(container: List[T1]) -> T1:
    return container[0]


T2 = TypeVar("T2", bound=int)  # T2 can only be an int or subtype of int


def first6(container: List[T2]) -> T2:
    return container[0]

if __name__ == "__main__":
    list_one = ["a", "b", "c"]
    print(first(list_one))

    list_two = [1, 2, 3]
    print(first(list_two))

    list_one3: List[str] = ["a", "b", "c"]
    print(first3(list_one3))

    list_two3: List[int] = [1, 2, 3]
    print(first3(list_two3))

    list_one4: List[str] = ["a", "b", "c"]
    print(first4(list_one4))

    test: Dict[str, int] = {"k": 1}
    print(get_item("k", test))

    print(get_first5(test))

    print(get_first6(test))

    list_one5: List[str] = ["a", "b", "c"]
    print(first5(list_one5))

    list_one6: List[float] = [1.5, 2.5, 3.5]
    print(first5(list_one6))

    list_one7: List[bool] = [True, False, True]
    print(first6(list_one7))

    list_one8: List[str] = ["a", "b", "c"]
    print(first5(list_one8))#print(first6(list_one8))
