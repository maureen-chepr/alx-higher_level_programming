#!/usr/bin/node
/*
 * sorting second biggest integer
 */
const secondBiggestInteger = (arr = []) => {
  if (arr.length <= 1) {
    console.log(0);
    return;
  }

  let largestNum = arr[0];
  let secondLargestNum = arr[0];

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > largestNum) {
      secondLargestNum = largestNum;
      largestNum = arr[i];
    } else if (arr[i] > secondLargestNum && arr[i] !== largestNum) {
      secondLargestNum = arr[i];
    }
  }

  console.log(secondLargestNum);
};
const args = process.argv.slice(2).map(Number);
secondBiggestInteger(args);
