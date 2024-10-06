export const emptyTable = {
  columns: [],
  rows: [],
  isLoading: true,
  totalRecordCount: 0
}

export const emptyChart = {
    labels: [],
    datasets: []
}

export const chartOptions = {
    responsive: true,
    maintainAspectRatio: true,
}

export const emptyApexChartOptions = {
  chart: {
    type: 'bar',
    height: 350,
    width: "100%",
    stacked: true,
    stackType: "100%"
  },
  plotOptions: {
    bar: {
      horizontal: true,
      dataLabels: {
        total: {
          offsetX: 0,
          style: {
            fontSize: '13px',
            fontWeight: 900
          }
        }
      }
    },
  },
  stroke: {
    width: 1,
    colors: ['#fff']
  },
  xaxis: {
    categories: [],
  },
  fill: {
    opacity: 1
  },
  legend: {
    position: 'top',
    horizontalAlign: 'left',
    offsetX: 40
  },
};

export const chartFilterOptions = [
    {
      id: 0,
      period: 'Today',
      value: 0,
    },
    {
      id: 1,
      period: 'Last 7 days',
      value: 7
    },
    {
      id: 2,
      period: 'Last 30 days',
      value: 30,
    },
    {
      id: 3,
      period: 'Last 12 Months',
      value: 365
    },
    {
      id: 4,
      period: 'All Time',
      value: -1
    }
  ]