#include<bits/stdc++.h>
using namespace std;

struct Packet
{
  int arrivalTime;
  int endTime;
  int atByte = 0;
  int size;
  bool sent;
};

struct Queue
{
  int atPacket = 0;
  int weight;
  int size;
  bool allSent;
  vector<Packet> packets;
};


int main()
{
	//Enter number of queues;
	int noQ;
	cin>>noQ;

	vector<Queue> Q(noQ);
		
	for(int i=0; i<noQ; i++)
	{
		//enter number of packets in a q
		int noP;
		cin>>noP;
		vector<Packet> packets(noP);

		//enter packets
		for (int j = 0; j < noP; j++)
		{
			cout << "Insert arival time of packet number " << j << endl;
			cin >> Q[i].packets[j].arrivalTime;
			cout << "Insert size of packet number " << j << endl;
			cin >> Q[i].packets[j].endTime;
			Q[i].packets[j].size = Q[i].packets[j].endTime; - Q[i].packets[j].arrivalTime;
		}



	}

}