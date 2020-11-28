#include <iostream>

using namespace std;

void max_min(int& a, int& b) {
	if (a > b) {
		cout << "Max: " << a << ", Min: " << b;
	}
	else {
		cout << "Max: " << b << ", Min: " << a;
	}
}

void max_min(double& a, double& b) {
	if (a > b) {
		cout << "Max: " << a << ", Min: " << b;
	}
	else {
		cout << "Max: " << b << ", Min: " << a;
	}
}

void max_min(int a[], int size) {
	for (int i = 0; i < size; i++) {
		for (int j = size-1; j > i; j--) {
			if (a[j - 1] > a[j]) {
				int temp = a[j];
				a[j] = a[j - 1];
				a[j - 1] = temp;
			}
		}
	}
	cout << "Max: " << a[size - 1] << ", Min: " << a[0];
}

int main() {
	int array[5] = { 1,9,-2,8,6 };
	int a = 2, b = 3;
	max_min(a, b);
	cout << endl;
	max_min(array, 5);
}