#include <iostream>
#define NO_PARAM_ERR_CODE 11
#define NOT_DIGIT_ERR_CODE 12
#define TOO_MANY_PARAM_ERR_CODE 13

void print_err_code(int err_code);

int main(int argc, char* argv[], char* env[])
{
    if (argc == 1) {
        print_err_code(NO_PARAM_ERR_CODE);
        return NO_PARAM_ERR_CODE;
    }

    bool silent = (strcmp(argv[1], "/S") == 0 || strcmp(argv[1], "/s") == 0);

    if (silent) {
        if (argv[2] == NULL) return NO_PARAM_ERR_CODE;
        else if (argv[3] != NULL) return TOO_MANY_PARAM_ERR_CODE;
        else if (!isdigit(*argv[2]) || strlen(argv[2]) != 1) return NOT_DIGIT_ERR_CODE;
        else return atoi(argv[2]);
    }
    else {
        if (argv[2] != NULL) {
            print_err_code(TOO_MANY_PARAM_ERR_CODE);
            return TOO_MANY_PARAM_ERR_CODE;
        }
        else if (!isdigit(*argv[1]) || strlen(argv[1]) != 1) {
            print_err_code(NOT_DIGIT_ERR_CODE);
            return NOT_DIGIT_ERR_CODE;
        }
        else {
            print_err_code(atoi(argv[1]));
            return atoi(argv[1]);
        }
    }
}

void print_err_code(int err_code)
{
    std::cout << "Kod powrotu: " << err_code << std::endl;
}
