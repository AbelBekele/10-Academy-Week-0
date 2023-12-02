import { useState, useEffect } from "react";
import {
  Button,
  Card,
  BarChart,
  Flex,
  TabGroup,
  Tab,
  TabList,
  Bold,
  Divider,
  List,
  ListItem,
  Metric,
  Text,
  Title,
} from "@tremor/react";
import {
  HiArrowRight,
  HiOutlineChartBar,
  HiOutlineViewList,
} from "react-icons/hi";

const SentimentCard = () => {
  const [selectedIndex, setSelectedIndex] = useState(0);
  const [channelSentimentData, setChannelSentimentData] = useState([]);

  useEffect(() => {
    // Fetch data from Flask app when the component mounts
    const fetchData = async () => {
      try {
        const response = await fetch("http://127.0.0.1:5000/channel_messages_sentiment");
        const data = await response.json();

        // Rounding sentiment score
        const formattedData = data.average_sentiment_per_channel.map((item) => ({
          ...item,
          average_sentiment_score: item.average_sentiment_score.toFixed(3),
        }));

        setChannelSentimentData(formattedData);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []); // Empty dependency array ensures the effect runs only once on mount

  return (
    <Card className="max-w-full mx-auto" backgroundColor="white">
      <Flex className="space-x-8 flex-col lg:flex-row">
        <Title>Overview</Title>
        <TabGroup index={selectedIndex} onIndexChange={setSelectedIndex}>
          <TabList variant="solid">
            <Tab icon={HiOutlineChartBar}>Chart</Tab>
            <Tab icon={HiOutlineViewList}>List</Tab>
          </TabList>
        </TabGroup>
      </Flex>
      <Text className="mt-4"></Text>
      <Metric>Sentiment Score</Metric>
      <Divider />
      <Text className="-mt-4">
        Positive sentiment: A score closer to 1 indicates a more positive sentiment.
      </Text>
      <Text>Neutral sentiment: A score around 0 suggests a neutral sentiment.</Text>
      <Text>Negative sentiment: A score closer to -1 indicates a more negative sentiment.</Text>

      {selectedIndex === 0 && channelSentimentData.length > 0 ? (
      <div style={{ width: "100%", height: "300px" }}>
        {
          <BarChart
            data={channelSentimentData}
            xKey="channel"
            yKey="average_sentiment_score"
            xLabel="Channel"
            yLabel="Sentiment Score"
            yTicks={[-1, -0.5, 0, 0.5, 1]}
            yDomain={[-1, 1]}
            fill={(dataPoint) => {
              const score = dataPoint.average_sentiment_score;
              const color = `hsl(${score * 120}, 100%, 50%)`;
              return color;
              }} // Use a function to return a gradient of colors from blue to green based on sentiment score
              className="mt-2"
            />
          }
        </div>
      ) : (
        <>
          <Flex className="mt-4" justifyContent="between">
            <Text className="truncate">
              <Bold>Channels</Bold>
            </Text>
            <Text>Message Sentiment score</Text>
          </Flex>
          {/* Apply styles for a scrollable list with a fixed height */}
          <div className="mt-4 px-2" style={{ maxHeight: "300px", overflowY: "auto" }}>
            <List>
              {/* Render only the first 5 items in the list */}
              {channelSentimentData.slice(0, 50).map((channel) => (
                <ListItem key={channel.channel}>
                  <Text>{channel.channel}</Text>
                  <Flex className="space-x-2" justifyContent="end">
                    <Text>{` ${channel.average_sentiment_score}`}</Text>
                  </Flex>
                </ListItem>
              ))}
            </List>
          </div>
        </>
      )}
      <Flex className="mt-6 pt-4 border-t">
        <Button
          size="xs"
          variant="light"
          icon={HiArrowRight}
          iconPosition="right"
        >
          View more
        </Button>
      </Flex>
    </Card>
  );
};

export default SentimentCard;
