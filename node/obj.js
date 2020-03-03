const square = function(x) {
  return x*x;
};

function hasValue(obj, key, value) {
    return obj.hasOwnProperty(key) && obj[key] === value;
};

const getNestedObject = (nestedObj, pathArr) => {
    return pathArr.reduce((obj, key) =>
        (obj && obj[key] !== 'undefined') ? obj[key] : undefined, nestedObj);
};

const isUndefined = (obj) => {
  return typeof obj === 'undefined';
};

const isNull = (obj) => {
  return obj === null;
}

function isEmpty(obj) {
  return (!obj || 0 === obj.length);
//    for(var key in obj) {
//        if(obj.hasOwnProperty(key))
//            return false;
//    }
//    return true;
}

const isBlank = (str) => {
  return isNull(str) || isUndefined(str) || Object.keys(str).length == 0;
}



function isNullOrUndefined(obj)
{
 return obj === 'null' && obj === 'undefined';
}

var obj = {
    "groupId": "663f20df-016e-1000-d7f7-53ff38541a84",
    "id": "9f76a885-7574-3fc7-759e-9082b73e03b5",
    "type": "Connection",
    "details": {
        "Source Name": "GenerateAAAA",
        "Destination Name": "LogAAAA",
        "Id": "9f76a885-7574-3fc7-759e-9082b73e03b5",
        "Group Id": "663f20df-016e-1000-d7f7-53ff38541a84",
        "Name": "AAAA"
    },
    instances: [
        {
            "id": "nifi-instance-id",
            "label": "NiFi",
            "snapshots" : [
                {
                    "timestamp": "2019-11-13T21:17:26.750Z",
                    "statusMetrics": {
                        "inputBytes": 0,
                        "outputCount": 3,
                        "backpressureEstimate": -1,
                        "queuedCount": 584,
                        "queuedBytes": 584,
                        "outputBytes": 3,
                        "inputCount": 0
                    }
                },
                {
                    "timestamp": "2019-11-13T21:18:26.760Z",
                    "statusMetrics": {
                        "inputBytes": 0,
                        "outputCount": 6,
                        "backpressureEstimate": -1,
                        "queuedCount": 581,
                        "queuedBytes": 581,
                        "outputBytes": 6,
                        "inputCount": 0
                    }
                }
            ]
        }    
    ]
};

var obj1 = {
    "groupId": "663f20df-016e-1000-d7f7-53ff38541a84",
    "id": "9f76a885-7574-3fc7-759e-9082b73e03b5",
    "type": "Connection",
    "details": {
        "Source Name": "GenerateAAAA",
        "Destination Name": "LogAAAA",
        "Id": "9f76a885-7574-3fc7-759e-9082b73e03b5",
        "Group Id": "663f20df-016e-1000-d7f7-53ff38541a84",
        "Name": "AAAA"
    },
    instances: [
        {
            "id": "nifi-instance-id",
            "label": "NiFi",
            "snapshots" : []
        }    
    ]
};
//console.log(obj)
//console.log(JSON.stringify(obj, null, 4))
//console.log("====");
//console.log("\n")
//console.log("====");
//console.log(obj.instances)
//console.log("====");
//console.log(obj.instances[0])
//console.log("====");
val = ((((obj1.instances[0] || {}).snapshots[0] || {}).statusMetrics || {}).backpressureEstimate || {})
console.log(val);
console.log(isNull(val));
console.log(isUndefined(val));
console.log(isEmpty(val));
if (isBlank(val)) {
  console.log("val is blank");
} else {
  console.log(val);
}

val = ((((obj.instances[0] || {}).snapshots[0] || {}).statusMetrics || {}).backpressureEstimate || {})
console.log(val);
console.log(isNull(val));
console.log(isUndefined(val));
console.log(isEmpty(val));

//if (isBlank(val)) {
//  console.log("val is blank");
//} else {
//  console.log(val);
//}



//obj1.instances[0].snapshots[0].statusMetrics.backpressureEstimate = 1234;
//val = obj1.instances[0].snapshots[0].statusMetrics.backpressureEstimate
//console.log(val);

//console.log('keys: ' + Object.keys(obj1));
//console.log();

//if (obj1.hasOwnProperty('instances')) {
////  inst = getNestedObject(obj, ['instances', 0]);
////  if (inst.hasOwnProperty('snapshots')) {
////    snaps = getNestedObject(inst, ['snapshots', 0]);
////    if (snaps.hasOwnProperty('statusMetrics')) {
////      console.log(snaps.statusMetrics.backpressureEstimate);
////    }
////  }
//}
//snaps = obj1.instances[0].snapshots
//console.log(snaps)
//if (obj1.instances.hasOwnProperty('snapshots')) {
//  console.log("YEA");
//}

//if ("backpressureEstimate" in obj) {
//  console.log("found backpressureEstimate");
//} else {
//  console.log("did not find estimate");
//}

//console.log(obj.hasOwnProperty('backpressureEstimate'));
//console.log();
//console.log(obj['instances.snapshots'])

//console.log(Object.values(obj));

//console.log('instances' in Object.keys(obj));



//console.log('estimate: ' + getNestedObject(obj, ['groupId']));

//var test = [{name : "joey", age: 15}, {name: "hell", age: 12}];
//console.log(test.some(function(boy) { return hasValue(boy, "age", 12); }));

const user = {
    id: 101,
    email: 'jack@dev.com',
    personalInfo: {
        name: 'Jack',
        address: {
            line1: 'westwish st',
            line2: 'washmasher',
            city: 'wallas',
            state: 'WX'
        }
    }
};

//// pass in your object structure as array elements
//const name = getNestedObject(user, ['personalInfo', 'name']);
//console.log('name: ' + name);

//// to access nested array, just pass in array index as an element the path array.
//const city = getNestedObject(user, ['personalInfo', 'address', 'city']);
//// this will return the city from the first address item.
//console.log('city: ' + city);

