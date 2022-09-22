#include <stdio.h>
#include <stdlib.h>

char arr[6562][6562];

void Star(int x, int y, int size)
{
	int next = size / 3;
	int xMax = x + size;
	int yMax = y + size;

	for (int i = x; i < xMax; i = i + next)
	{
		for (int j = y; j < yMax; j = j + next)
		{
			if (((i / next) % 3 == 1) && ((j / next) % 3 == 1))
			{
				for (int k = 0; k < next; k++)
				{
					for (int l = 0; l < next; l++)
					{
						arr[j + k][i + l] = ' ';
					}
				}
			}
			else if (3 == size)
			{
				for (int k = 0; k < next; k++)
				{
					for (int l = 0; l < next; l++)
					{
						arr[j + k][i + l] = '*';
					}
				}
			}
			else
			{
				Star(i, j, next);
			}
		}
	}
}

int main()
{
	int count = 0;
	scanf("%d", &count);
	Star(0, 0, count);

	for (int i = 0; i < count; i++)
	{
		for (int j = 0; j < count; j++)
		{
			printf("%c", arr[j][i]);
		}
		printf("\n");
	}

	return 0;
}