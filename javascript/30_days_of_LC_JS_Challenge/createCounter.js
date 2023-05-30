var createCounter = function(n) {
    
    let count = n;
    return function() {
        let result = count;
        count += 1;
        return result;
    };
    
};
