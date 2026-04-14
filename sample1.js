function test() {
    var x = null;

    if (x == null) {
        console.log("x is null");
    }

    try {
        let result = 10 / 0;
    } catch (e) {
        console.log("error occurred");
    }
}