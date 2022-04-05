export default function getStudentIdsSum(data) {
  return data.reduce((previousValue, currentValue) => previousValue + currentValue.id, 0);
}
