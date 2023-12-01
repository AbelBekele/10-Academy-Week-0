import AreaChartCard from "./AreaChartCard";
import TableCard from "./TableCard";

const LeftColumn = () => {
  return (
    <div className="w-full flex flex-col justify-between p-2 mt-4">
      <div className="flex-auto w-full">
        <AreaChartCard />
        <TableCard />
      </div>
    </div>
  );
};

export default LeftColumn;
