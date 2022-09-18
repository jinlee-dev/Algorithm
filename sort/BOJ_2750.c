#include <iostream>

void BubbleSort(int* arr, int count)
{
    for (int i = 0; i < count; i++)
    {
        int bubbleCnt = count - i - 1;
        for (int j = 0; j < bubbleCnt; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                int tmp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = tmp;
            }
        }
    }
}

int main()
{
    int count = 0;
    scanf("%d", &count);
    int* pInput = new int[count];
    for (int i = 0; i < count; i++)
    {
        scanf("%d", &pInput[i]);
    }
    BubbleSort(pInput, count);

    for (int i = 0; i < count; i++)
    {
        printf("%d\n", pInput[i]);
    }
    return 0;
}