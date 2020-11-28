#include <iostream>
#include <string>
using namespace std;

// 형 변환으로 인한 모호성
float square(float a) {
	return a * a;
}

double square(double a) {
	return a * a;
}

// 참조 매개 변수로 인한 모호성
int add(int a, int *b) {
	return *b;
}

int add(int a, int& b) {
	b += a;
	return b;
}

// 디폴트 매개 변수로 인한 모호성
void msg(int id, string s = "") {
	cout << id << ": " << s << endl;
}
int main() {
	// 형 변환으로 인한 모호성
	cout << square(3.0) << endl;
	cout << square(3.0f) << endl;
	// float로 줄 값에 f를 붙여줌

	// 참조 매개 변수로 인한 모호성
	int s = 10, t = 20;
	cout << add(s, &t) << endl;
	cout << add(s, t) << endl;

	// 디폴트 매개 변수로 인한 모호성
	msg(5, "Good Morning");
	msg(6);
	// 디폴트 매개 변수를 사용하여 함수 오버로딩을 없애줌
}