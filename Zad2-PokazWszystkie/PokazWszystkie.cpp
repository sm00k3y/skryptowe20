#include <iostream>

int main(int argc, char* argv[], char* env[])
{
    std::cout << "ENVIRONMENTAL VARIABLES:\n" << std::endl;
    while (*env != NULL) {
        std::cout << *env++ << std::endl;
    }

    std::cout << "\nPROGRAM VARIABLES:\n" << std::endl;
    for (int i = 0; i < argc; i++) {
        std::cout << argv[i] << std::endl;
    }

    return 0;
}
