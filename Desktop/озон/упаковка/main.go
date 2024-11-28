package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type Data struct {
	num    int
	degree float64
	count  int
}

func minTransportations(car int, max_weight float64, len_arr int, data []Data) int {
	count := 0
	const_car := car
	for i := 0; i < len_arr; i++ {

		weight := data[i].degree
		free_weight := max_weight

		if data[i].count > 0 {
			free_weight -= weight
			data[i].count--

			if free_weight == 0 {
				car--
				if car == 0 {
					count++
					car = const_car
				}
			} else if data[int(free_weight)].count > 0 {
				data[int(free_weight)].count--
				car--
				if car == 0 {
					count++
					car = const_car
				}
			} else {
				loss := float64(0)
				was_weight := free_weight

				for free_weight > 0 {
					if data[int(free_weight)].count > 0 {
						data[int(free_weight)].count--
						free_weight = loss
						loss = 0

					} else {
						free_weight -= 1
						loss += 1
					}
				}

				if was_weight != loss+1 {
					car--
					if car == 0 {
						count++
						car = const_car
					}
				}
			}

		}

	}
	if car != const_car {
		count++
	}
	return count
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	scanner.Scan()
	t, _ := strconv.Atoi(scanner.Text())

	// Создаем срез для хранения структур Data
	dataSlice := make([]Data, 30) // 30 элементов от 29 до 0

	// Заполняем срез
	for i := 29; i >= 0; i-- {
		dataSlice[29-i] = Data{
			num:    i,
			degree: math.Pow(2, float64(i)), // 2^i
			count:  0,
		}
	}

	for i := 0; i < t; i++ {
		scanner.Scan()
		params := strings.Split(scanner.Text(), " ")
		car, _ := strconv.Atoi(params[0])
		max_weight, _ := strconv.ParseFloat(params[1], 64)

		scanner.Scan()
		count_el, _ := strconv.Atoi(scanner.Text())
		scanner.Scan()
		boxStrs := strings.Split(scanner.Text(), " ")

		for j := 0; j < count_el; j++ {
			num, _ := strconv.Atoi(boxStrs[j])
			dataSlice[num].count++
		}

		result := minTransportations(car, max_weight, count_el, dataSlice)
		fmt.Fprintln(writer, result)
	}
}
