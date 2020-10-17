#include <iostream>
#include <algorithm>

bool is_silent(char* arg);

int main(int argc, char* argv[], char* env[])
{
    bool silent_mode = false;

    for (int i = 1; i < argc; i++) {
        if (i == 1 && is_silent(argv[i])) silent_mode = true;

        int env_idx = 0;
        std::string arg_str(argv[i]);
        bool found_any = false;

        while (env[env_idx] != nullptr) {
            std::string env_str(env[env_idx]);
            std::size_t pos = env_str.find("=");
            std::string env_name = env_str.substr(0, pos+1);

            if (env_name.find(arg_str) != std::string::npos) {
                found_any = true;
                std::replace(env_str.begin(), env_str.end(), ';', '\n');
                std::cout << env_str << std::endl;
            }
            env_idx++;
        }

        if (!found_any && !silent_mode) {
            std::cout << argv[i] << " = NONE" << std::endl;
        }
    }

    return 0;
}

bool is_silent(char* arg) 
{
    return (strcmp(arg, "/S") == 0 || strcmp(arg, "/s") == 0);
}