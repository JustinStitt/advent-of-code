package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	lines := []string{}
	mat := map[complex128]rune{}

	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	for r, str := range lines {
		for c, ch := range str {
			mat[complex(float64(r), float64(c))] = ch
		}
	}

	solve2(mat)
}

func solve(mat map[complex128]rune) {
	res := 0

	deltas := [...]complex128{-1 - 1i, -1 + 0i, 1 - 1i, 0 - 1i, 0 + 1i, 1 + 1i, -1 + 1i, 1 + 0i}
	for k, v := range mat {
		if v != '@' {
			continue
		}

		surr := 0
		for _, delta := range deltas {
			if mat[k+delta] == '@' {
				surr += 1
			}
		}
		if surr < 4 {
			res += 1
		}
	}

	fmt.Println(res)
}

func solve2(mat map[complex128]rune) {
	res := 0

	deltas := [...]complex128{-1 - 1i, -1 + 0i, 1 - 1i, 0 - 1i, 0 + 1i, 1 + 1i, -1 + 1i, 1 + 0i}

	for {
		changed := false
		for k, v := range mat {
			if v != '@' {
				continue
			}

			surr := 0
			for _, delta := range deltas {
				if mat[k+delta] == '@' {
					surr += 1
				}
			}
			if surr < 4 {
				res += 1
				mat[k] = '.'
				changed = true
			}
		}
		if changed == false {
			break
		}
	}

	fmt.Println(res)
}
