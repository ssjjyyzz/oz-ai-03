// 조건문
// Python: if / else
 // if is is_student:
 //     print(Hello student)


 let age = 20;
 
 if (age >= 19) {
    console.log("성인");
 } else if (age >= 8) {
    console.log("학생");
 } else {
    console.log("어린이");
 };


// true로 판단되는 값 : 50, 1, -1, "100", "0" , [] -> truthy
// false로 판단되는 값 : 0, "", null, undefined, NaN, false -> falsy (무조건 여기 있는 6개만 JS에서 false로 판단 !ㅊ)
 let score = 50;
 if (score) {
    console.log("점수" + score);
 } else {
    console.log("점수 없음");
 };

