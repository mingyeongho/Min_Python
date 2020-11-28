#include <iostream>

using namespace std;

class Base {
	int a;
protected:
	void setA(int a) {
		this->a = a;
	}
public:
	void showA() {
		cout << a;
	}
};

class Derived : protected Base {
	int b;
protected:
	void setB(int b) {
		this->b = b;
	}
public:
	void showB() {
		cout << b;
	}
	void setAA(int a) {
		setA(a);
	}
	void showAA() {
		showA();
	}
	void setBB(int b) {
		setB(b);
	}
};

int main() {
	Derived x;
	// x.a = 5;
	x.setAA(10);
	x.showAA();
	// x.b = 5;
	x.setBB(10);
	x.showB();
}