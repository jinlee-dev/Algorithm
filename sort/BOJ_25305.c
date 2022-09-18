#include <iostream>

int Partition(int arr[], int left, int right)
{
	int pivot = arr[right];
	int small = left - 1;
	for (int i = left; i < right; i++)
	{
		if (arr[i] < pivot)
		{
			small++;
			int tmp = arr[i];
			arr[i] = arr[small];
			arr[small] = tmp;
		}
	}

	int tmp = arr[small + 1];
	arr[small + 1] = arr[right];
	arr[right] = tmp;
	return small + 1;
}

void QuickSort(int arr[], int left, int right)
{
	if(left < right)
	{
		int pivot = Partition(arr, left, right);
		QuickSort(arr, left, pivot - 1);
		QuickSort(arr, pivot + 1, right);
	}
}

int main()
{
	int count = 0;
	int cutLine = 0;
	scanf("%d %d", &count, &cutLine);
	int* pInput = new int[count];
	for (int i = 0; i < count; i++)
	{
		scanf("%d", &pInput[i]);
	}

	QuickSort(pInput, 0, count - 1);
	printf("%d", pInput[count - cutLine]);
	return 0;
}