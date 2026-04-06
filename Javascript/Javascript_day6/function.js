// 함수(Function)
// 입력 값을 받아서 데이터를 처리하고, 결과를 반환하는 코드 뭉치
// -> 코드를 재사용하기 위해 만들어놓은 구조

// 함수 정의 -> "~ 기능을 하는 코드 덩어리"를 X라는 이름으로 부르겠다
// Return -> 결과 값을 반환, 함수 종료
// 입력 -> 함수 동작 -> 출력
function add(n1, n2) {
    // 함수 동작 구현부
    let result = n1 + n2;

    // 함수를 호출한 곳으로 함수의 실행 결과를 돌려준다
    return result; // 함수 안에서 선언된 result는 함수 안에서만 사용됨.
    // console.log(result); : 이렇게 내부에서 배로 출력도 가능. 대신 return result; 없이 출력만 찍을 경우 반환값이 사라지므로 아래 함수 호출에서 undefined 출력.
}


// 함수 호출(call) -> 함수를 사용한다 
add(1, 2);
let return_value = add(1, 2);
console.log(return_value);

