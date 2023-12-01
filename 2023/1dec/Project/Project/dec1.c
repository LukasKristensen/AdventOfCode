#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main() {
    char* filename = "input.txt";
    FILE* file = fopen(filename, "r");

    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    int part_one = 0;
    int part_two = 0;
    char line[256];
    char nums_spelled[9][6] = { "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };

    while (fgets(line, sizeof(line), file)) {
        int p1_first_digit = 0;
        int p1_last_digit = 0;
        int p2_first_digit = 0;
        int p2_last_digit = 0;

        for (int i = 0; line[i] != '\0'; i++) {
            if (isdigit(line[i])) {
                char digit_str[2] = { line[i], '\0' };
                int current_digit = atoi(digit_str);

                if (p1_first_digit == 0) {
                    p1_first_digit = current_digit;
                    p2_first_digit = current_digit;
                }
                else {
                    p1_last_digit = current_digit;
                    p2_last_digit = current_digit;
                }
            }
        }

        for (int b = 0; b < 9; b++) {
            char* found = line;
            while ((found = strstr(found, nums_spelled[b])) != NULL) {
                int current_digit = b + 1;
                if (p2_first_digit == 0) {
                    p2_first_digit = current_digit;
                }
                else {
                    p2_last_digit = current_digit;
                }
                found++;
            }
        }

        if (p1_last_digit == 0) {
            p1_last_digit = p1_first_digit;
        }

        part_one = part_one + p1_first_digit * 10 + p1_last_digit;
        part_two = part_two + p2_first_digit * 10 + p2_last_digit;
    }

    printf("Part A) %d\n", part_one);
    printf("Part B) %d\n", part_two);
    fclose(file);

    return 0;
}

