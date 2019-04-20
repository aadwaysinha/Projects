#include <bits/stdc++.h>
using namespace std;

struct Packet
{
  int arrivalTime;
  int size;
  bool sent;
  int partSent;
  int endAt;
  int totalSize;
  int origAT;
};

struct Queue
{
  int atPacket = 0;
  int weight;
  int size;
  bool allSent;
  vector<Packet> packets;
};

int findPossibleMin(vector<Queue> &Q, int sendingFrom)
{
  vector<int> ats;
  for (int i = 0; i < Q.size(); i++)
  {
    for (int j = 0; j < Q[i].packets.size(); j++)
    {
      if (Q[i].packets[j].origAT > sendingFrom)
        ats.push_back(Q[i].packets[j].origAT);
      if (Q[i].packets[j].origAT + Q[i].packets[j].size > sendingFrom)
        ats.push_back(Q[i].packets[j].origAT + Q[i].packets[j].size);
    }
  }

  cout << "ATSATSATSATS: ";
  for (int time : ats)
    cout << time << " ";
  cout << endl;

  int minDist = INT_MAX;
  for (int i = 0; i < ats.size(); i++)
    minDist = min(ats[i], minDist);
  return minDist;
}

bool allPacketsSent(vector<Queue> Q)
{
  for (int i = 0; i < Q.size(); i++)
  {
    for (int j = 0; j < Q[i].packets.size(); i++)
      if (!Q[i].packets[j].sent)
        return false;
  }
  return true;
}

int main()
{
  cout << "Insert number of queues" << endl;
  int numberOfQueues;
  cin >> numberOfQueues;
  vector<Queue> Q(numberOfQueues);

  for (int i = 0; i < numberOfQueues; i++)
  {
    cout << "Insert number of packet(s) for queue number " << i << endl;
    int numberOfPackets;
    cin >> numberOfPackets;
    Q[i].size = numberOfPackets;
    vector<Packet> ps(numberOfPackets);
    Q[i].packets = ps;
    for (int j = 0; j < numberOfPackets; j++)
    {
      cout << "Insert arival time of packet number " << j << endl;
      cin >> Q[i].packets[j].arrivalTime;
      cout << "Insert size of packet number " << j << endl;
      cin >> Q[i].packets[j].size;
    }
  }
  cout << "Alright, now assign priorities\n";
  for (int i = 0; i < numberOfQueues; i++)
  {
    cout << "What is the weight for queue number " << i << "?" << endl;
    cin >> Q[i].weight;
  }

  for (int i = 0; i < Q.size(); i++)
  {
    cout << "In queue: " << i << endl;
    for (int j = 0; j < Q[i].packets.size(); j++)
    {
      Q[i].packets[j].origAT = Q[i].packets[j].arrivalTime;
      //Q[i].packets[j].totalSize = Q[i].packets[j].arrivalTime + Q[i].packets[j].size
    }
  }

  int sendingFrom = 0;
  bool allSent = false;
  int test = 10;

  for (int i = 0; i < Q.size(); i++)
  {
    cout << "In queue: " << i << endl;
    for (int j = 0; j < Q[i].packets.size(); j++)
    {
      cout << "Packet starts from " << Q[i].packets[j].arrivalTime << " and ends at " << Q[i].packets[j].arrivalTime + Q[i].packets[j].size << endl;
      //Q[i].packets[j].totalSize = Q[i].packets[j].arrivalTime + Q[i].packets[j].size
    }
  }

  while (test--)
  {
    cout << "lol inf loop baby\n";
    int sendTill = findPossibleMin(Q, sendingFrom);
    cout << "Sending till: " << sendTill << endl;
    int sendingInterval = sendTill - sendingFrom;
    for (int i = 0; i < numberOfQueues; i++)
    {
      if (!Q[i].allSent && Q[i].packets[Q[i].atPacket].arrivalTime == sendingFrom)
      {
        int sendBytes = Q[i].weight * sendingInterval;
        cout << "interval from " << sendingFrom << " to " << sendTill << endl;
        Q[i].packets[Q[i].atPacket].partSent += sendBytes;
        cout << sendingInterval << " data sent from packet number " << Q[i].atPacket << " from queue number " << i << endl;
        if (Q[i].packets[Q[i].atPacket].partSent >= Q[i].packets[Q[i].atPacket].arrivalTime + Q[i].packets[Q[i].atPacket].size)
        {
          Q[i].packets[Q[i].atPacket].sent = true;
          Q[i].atPacket++;
        }
        Q[i].packets[Q[i].atPacket].arrivalTime += min(sendBytes, Q[i].packets[Q[i].atPacket].size);
        cout << "Size of this packet is: " << Q[i].packets[Q[i].atPacket].size << endl;
        cout << "new arrival time for packet " << Q[i].atPacket << ": " << Q[i].packets[Q[i].atPacket].arrivalTime << endl;
        if (Q[i].atPacket == Q[i].size)
          allSent = true;
      }
    }
    sendingFrom += sendingInterval;
    if (allPacketsSent(Q))
      break;
    //Sleep(100);
  }
}

/*

4

3
12 13  50 12  75 12

3
0 25  50 12  87 13

2
0 12  62 25

3
0 12  37 25  75 25

1 1 1 1

*/