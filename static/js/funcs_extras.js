////# FUNÇÕES AUXILIARES #////

function jsonCopy(src) {
  return JSON.parse(JSON.stringify(src))
}

var percentColors = [
    { pct: 0.0, color: { r: 0, g: 255, b: 0 } },
    { pct: 0.5, color: { r: 255, g: 255, b: 0 } },
    { pct: 1.0, color: { r: 255, g: 0, b: 0 } } ];

var getColorForPercentage = function(pct) {
    for (var i = 1; i < percentColors.length - 1; i++) {
        if (pct < percentColors[i].pct) {
            break;
        }
    }
    var lower = percentColors[i - 1];
    var upper = percentColors[i];
    var range = upper.pct - lower.pct;
    var rangePct = (pct - lower.pct) / range;
    var pctLower = 1 - rangePct;
    var pctUpper = rangePct;
    var color = {
        r: Math.floor(lower.color.r * pctLower + upper.color.r * pctUpper),
        g: Math.floor(lower.color.g * pctLower + upper.color.g * pctUpper),
        b: Math.floor(lower.color.b * pctLower + upper.color.b * pctUpper)
    };
    return 'rgb(' + [color.r, color.g, color.b].join(',') + ')';
    // or output as hex if preferred
}
