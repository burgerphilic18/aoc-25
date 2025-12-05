package main

import (
	"bufio"
	"fmt"
	"os"
)

func maxJoltage(line string) int {
	best := -1
	for i := range line {
		for j := range line {
			if j > i {
				v := int(line[i]-'0')*10 + int(line[j]-'0')
				if v > best {
					best = v
				}
			}
		}
	}
	return best
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	sum := 0
	for scanner.Scan() {
		line := scanner.Text()
		if len(line) > 0 {
			sum += maxJoltage(line)
		}
	}
	fmt.Println("answer is", sum)
}
