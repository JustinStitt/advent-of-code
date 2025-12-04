package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	lines := []string{}
	for scanner.Scan() { // for each line
		lines = append(lines, scanner.Text())
	}

	for _, line := range lines {
		solve(line)
	}
}

func solve(line string) {
	res := 0

	for i, v := range line {
		nidx := (i + len(line)/2) % len(line)
		if byte(v) == line[nidx] {
			res += int(v - '0')
		}
	}

	fmt.Println(res)
}
