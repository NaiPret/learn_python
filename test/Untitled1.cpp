#include <stdio.h>
#define MAX 4
int find( int a[MAX][MAX], int x, int r1, int c1, int r2, int c2 ) {
 if ( x < a[r1][c1] || x > a[r2][c2] ) return 0;
 if ( x == a[r1][c1] || x == a[r2][c2] ) return 1;
 int _r1 = r1, _c1 = c1, _r2 = r2, _c2 = c2;
 int mRow = ( r1 + r2 ) / 2;
 int mCol = ( c1 + c2 ) / 2;
 while ( ( mRow != r1 || mCol != c1 ) && ( mRow != r2 || mCol != c2 ) ) {
 if ( x == a[mRow][mCol] ) return 1;
 if ( x < a[mRow][mCol] ) { r2 = mRow; c2 = mCol; }
 else { r1 = mRow; c1 = mCol; }
 mRow = ( r1 + r2 ) / 2;
 mCol = ( c1 + c2 ) / 2;
 }
 int b = 0;
 if ( mRow < MAX - 1 )
 b = find( a, x, mRow + 1, _c1, _r2, mCol );
 if ( !b && mCol < MAX - 1 )
 b = find( a, x, _r1, mCol + 1, mRow, _c2 );
 return b;
}
int main() {
 int a[MAX][MAX] = { { 1, 2, 8, 9 },
 { 2, 4, 9, 12 },
 { 4, 7, 10, 13 },
 { 6, 8, 11, 15 } };
 int x = 7;
 printf( "[%d] %s\n", x,
 find( a, x, 0, 0, MAX - 1, MAX - 1 ) ? "found" : "not found" );
 return 0;
}
