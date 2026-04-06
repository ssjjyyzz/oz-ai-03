// 실습 1: 콘솔 계산기
console.log("===== 콘솔 계산기 =====")
// 1. 숫자 두 개를 변수로 선언
let a = 8;
let b = 12;

// 2. 연산자를 문자열로 정함 ("+", "-", "*", "/")
let operator = "+"; 

// 3. 연산자에 따라 계산 결과 출력
let result;

if (operator === "+") {
  result = a + b;
} else if(operator === "-") {
  result = a - b;
} else if(operator === "*") {
  result = a * b;  
} else if(operator === "/") {
  result = a / b;  
} else {
  result = "지원하지 않는 연산자입니다";
}

console.log(`입력받은 값: ${a}, ${b}`);
console.log(`연산자: ${operator}`);
console.log(`결과: ${a} ${operator} ${b} = ${result}`);


console.log("\n===== 최종 합격 판정 프로그램 =====");

let score = 90;       // 점수 입력
let attendance = 10;  //출석률 입력
let submitted = true; // 제출: true, 미제출: false 

// -- 합격 기준 --
// 1. 점수(score) 70 이상
// 2. 출석률(attendance) 80이상
// 3. 과제 제출 여부(submitted) true
// 단, 점수 90 이상이면 출석률은 무시하고 합격
if((submitted && score >= 70 && attendance >= 80) || 
    submitted && score >= 90){
        console.log("결과: 최종 합격")
    } else{
        console.log("결과: 불합격");
    }