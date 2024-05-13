#include <stdio.h>
#include <stdbool.h>

int main() {

	int a;
	bool cnt[42] = { false, };

	int res = 0;

	for (int i = 0; i < 10; i++) {
		scanf("%d", &a);
		
		cnt[a % 42] = true;
	}

	for (int i = 0; i < 42; i++) {
		if (cnt[i]) res++;
	}

	printf("%d", res);
	

	return 0;
}