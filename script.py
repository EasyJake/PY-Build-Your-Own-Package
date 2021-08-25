from math_package.math_module import add, multiply, subtract
from math_package.sub_package.math_helper import list_to

if __name__ == '__main__':
    print(list_to(5))
    print(add(*list_to(5)))
    print(subtract(
        *list_to(
            ((add(multiply(*list_to(5)), multiply(*list_to(6)))))
            )))