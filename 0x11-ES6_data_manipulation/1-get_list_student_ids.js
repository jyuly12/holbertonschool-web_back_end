export default function getListStudents(value) {
  if (Array.isArray(value)) {
    return value.map((idValue) => idValue.id);
  }
  return [];
}
