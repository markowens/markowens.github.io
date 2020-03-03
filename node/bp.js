
var predictions = [
            { label: 'object', timeToBackPressure: -1 },
            { label: 'size', timeToBackPressure: -1 },
        ];

var actualQueuePercents = [
            { label: 'object', percent: 0 },
            { label: 'size', percent: 0 }
        ];

var maxActual = _.maxBy(actualQueuePercents, 'percent');
if (maxActual.percent >= 100) {
  // currently experiencing back pressure
  return 'now (' + maxActual.label + ')';
}

console.log(maxActual)

