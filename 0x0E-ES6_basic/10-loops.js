export default function appendToEachArrayValue(array, appendString) {
  const newArray = array;
  for (const idx of array) {
    const value = array.indexOf(idx);
    newArray[value] = appendString + idx;
  }

  return newArray;
}
