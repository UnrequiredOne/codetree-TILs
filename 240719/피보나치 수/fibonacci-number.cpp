#include <iostream>
using namespace std;

int* fibo;

int fib(int n) {
	if (fibo[n] != 0) return fibo[n];
	fibo[n] = fib(n - 1) + fib(n - 2);
	return fibo[n];
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

	int N;
	cin >> N;
	fibo = new int[N + 2];
	fill_n(fibo, N, 0);
    fibo[1] = 1;
    fibo[2] = 1;
    int answer = fib(N);
	cout << answer << endl;

    return 0;
}