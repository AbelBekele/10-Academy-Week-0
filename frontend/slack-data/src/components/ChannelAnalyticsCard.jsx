import { useEffect, useState } from 'react';
import { BarList, Card, Title, Bold, Flex, Text } from "@tremor/react";

const WebAnalyticsCard = () => {
  const [channelData, setChannelData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/channel_activity');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        
        const sortedData = data.channel_activity.slice(0, 6).sort((a, b) => b.value - a.value);
        setChannelData(sortedData);
      } catch (error) {
        console.error('Error fetching channel data:', error);
      }
    };

    fetchData();
  }, []);
  return (
    <Card className="max-w-full my-4">
      <Title>Channel Analytics</Title>
      <Flex className="mt-4">
        <Text>
          <Bold>Source</Bold>
        </Text>
        <Text>
          <Bold>Messages count</Bold>
        </Text>
      </Flex>
      <BarList data={channelData} className="mt-2" />
    </Card>
  );
};

export default WebAnalyticsCard;
