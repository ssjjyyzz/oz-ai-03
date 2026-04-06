// 함수를 값처럼 다루기
// 1) 함수를 변수에 할당할 수 있다

// 함수 정의 -> 설명서/설계도
function sayHello() {
    console.log("Hello");
};


// 함수 호출 -> 기능 실제로 사용
sayHello(); // Hello

// 함수 -> 기능 그 자체
sayHello
console.log(sayHello); // [Function: sayHello]

// 1) 함수를 변수에 저장할 수 있다
const f = sayHello; 
console.log(f); // [Function: sayHello]
f(); // Hello

// 2) 함수를 다른 함수의 인자로 전달할 수 있다
function run(fn) {
    console.log("sart function run...")
    fn();
    console.log("end function run...")
}

run(sayHello); // Hello

// (기본) 함수를 선언한 곳에서 직접 호출
// (응용) 함수를 선언한 곳과 호출하는 곳이 달라질 수 있다


