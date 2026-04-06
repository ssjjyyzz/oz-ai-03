// 동등 비교 연산자
// Python: a == b (동등비교 : 값, 타입을 같이 비교)
// JS: a == b

console.log(10 == 10);

let a = 10;
console.log(a == 10);

// Python: 숫자 10 == 문자열 10 -> false (type이 다르면 false)
// JS: == -> 값만 비교 (내부에서 두개를 같은 타입으로 맞춘 후 비교)
console.log(10 == "10");

// JS: === -> JS에서 type까지 비교하고 싶은 경우 (값 & 타입 비교)
console.log(10 === "10");