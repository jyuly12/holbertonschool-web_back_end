export default function getStudentsByLocation(studens, city) {
  return studens.filter((items) => items.location === city);
}
