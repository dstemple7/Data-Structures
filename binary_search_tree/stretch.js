Array = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

var printArray = function(arr) {
    if ( typeof(arr) == "object") {
        for (var i = 0; i < arr.length; i++) {
            printArray(arr[i]);
        }
    }
    else document.write(arr);
}

printArray(Array);