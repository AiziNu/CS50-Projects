// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    uint8_t header[HEADER_SIZE];

// Read header from input file and write to output file
fread(header, sizeof(uint8_t), HEADER_SIZE, input);
fwrite(header, sizeof(uint8_t), HEADER_SIZE, output);

// Prepare to read 16-bit (2 byte) samples from the input file
int16_t buffer;

// Continue reading until there are no more samples
while (fread(&buffer, sizeof(int16_t), 1, input))
{
    // Scale sample by factor and write to output file
    buffer *= factor;
    fwrite(&buffer, sizeof(int16_t), 1, output);
}



    // TODO: Copy header from input file to output file

    // TODO: Read samples from input file and write updated data to output file

    // Close files
    fclose(input);
    fclose(output);
}
