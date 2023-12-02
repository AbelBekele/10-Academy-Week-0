import SentimentCard from "./SentimentCard";
import ChannelAnalyticsCard from "./ChannelAnalyticsCard";

const RightColumn = () => {
  return (
    <div className="w-full p-2 mt-3">
      <ChannelAnalyticsCard />
      <SentimentCard />
    </div>
  );
};

export default RightColumn;
