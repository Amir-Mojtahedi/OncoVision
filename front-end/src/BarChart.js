import React from "react";
import * as d3 from "d3";

// Will vary from barcharts to other graphs depending on the dataset
function BarChart({ data }) {

  const maxValue = Math.max(...data, 0);
  const scale = d3.scaleLinear().domain([0, maxValue]).range([0, 200]);

  return (
    <div className="chart-container">
      <h2>React-DOM Bar Chart</h2>
      <div className="bar-chart">
        {data.map((value, i) => {
          const barHeight = scale(value);
          return (
            <div key={i} className="bar" style={{ height: `${barHeight}px` }}>
              <span className="bar-label">{value}</span>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default BarChart;