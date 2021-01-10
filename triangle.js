/*
Determine if a triangle is equilateral, isosceles, or scalene.

An equilateral triangle has all three sides the same length.

An isosceles triangle has at least two sides the same length. (It is sometimes specified as having exactly two sides the same length, but for the purposes of this exercise we'll say at least two.)

A scalene triangle has all sides of different lengths.

*/

triangle1 = [1, 2, 3]
triangle2 = [2, 2, 4]
triangle3 = [3, 3, 3]

function checkTriangle(triangle) {
  // Check equilateral
  if (triangle[0] === triangle[1] && triangle[1] === triangle[2]) {
    console.log("Triangle is equilateral")
    return
  }
  // Check isosceles
  if (triangle[0] === triangle[1] || triangle[0] === triangle[2] || triangle[1] === triangle[2]) {
    console.log("Triangle is isosceles")
    return
  }
  // Else: scalene
  else {
    console.log("Triangle is scalene")
  }
}

checkTriangle(triangle1)
checkTriangle(triangle2)
checkTriangle(triangle3)
