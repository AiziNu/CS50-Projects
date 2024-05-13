#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }

    // Remember filenames
    char *infile = argv[1];

    // Open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // Buffer for data
    unsigned char buffer[512];
    int imageCount = 0;

    FILE *outptr = NULL;

    while (fread(buffer, 512, 1, inptr) == 1)
    {
        // Check if start of a new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Close current JPEG file
            if (outptr != NULL)
            {
                fclose(outptr);
            }

            // Create filename
            char filename[8];
            sprintf(filename, "%03i.jpg", imageCount);

            // Open a new JPEG file for writing
            outptr = fopen(filename, "w");
            if (outptr == NULL)
            {
                return 3;
            }

            imageCount++;
        }

        // If already found a JPEG, write to file
        if (outptr != NULL)
        {
            fwrite(buffer, 512, 1, outptr);
        }
    }

    // Close any remaining files
    if (outptr != NULL)
    {
        fclose(outptr);
    }

    // Close infile
    fclose(inptr);

    // Success
    return 0;
}
