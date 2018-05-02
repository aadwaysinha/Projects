#include<iostream>
#include<vector>
#include<pthread.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;

int contestantID = 0;
vector<string> allPossibleAnswers;

struct contestant{ string answers; double timeTaken; int contestantID;};

int compare (const void * a, const void * b)
{
    contestant *contestantA = (contestant*)a;
    contestant *contestantB = (contestant*)b;
    return contestantA->timeTaken - contestantB->timeTaken;
}

void* contestantPlays(void *arg)
{
    contestant *argContestant = (contestant*)arg;
    int chosenOption = rand()%24;
    argContestant->answers = allPossibleAnswers[chosenOption];
    argContestant->timeTaken = rand()%30;
    argContestant->contestantID = contestantID++;
    pthread_exit(0);
}

int main()
{
    string question;
    question = "This is a test question with a question mark at the end?\n\n";
    cout<<question<<endl;
    cout<<"A) OptionOne\t\tB)OptionTwo"<<endl;
    cout<<"C) OptionThree\t\tD)OptionFour"<<endl<<endl;
    cout<<"Provide correct answer sequence for the given question\n\n";
    string correctAnswers;
    cin>>correctAnswers;

    ///All possible answer sequences
    string s = "abcd";
    sort(s.begin(), s.end());
    do
    {
        allPossibleAnswers.push_back(s);
    }while(next_permutation(s.begin(), s.end()));

    pthread_t tids[10];
    contestant contestants[10];

    for(int i=0; i<10; i++)
    {
        pthread_attr_t attr;
        pthread_attr_init(&attr);
        pthread_create(&tids[i], &attr, contestantPlays, &contestants[i]);
    }

    for(int i=0; i<10; i++)
    {
        pthread_join(tids[i], NULL);
    }

    for(int i=0; i<10; i++)
    {
        cout<<"Contestant ID: "<< contestants[i].contestantID<<endl;
        cout<<"Contestant answer: "<< contestants[i].answers<<endl;
        cout<<"Contestant timeTaken: "<< contestants[i].timeTaken<<endl;
    }

    vector<contestant> contestantsWithCorrectAns;

    cout<<endl<<endl<<"Contestants with correctAnswers are: "<<endl<<endl;

    for(int i=0; i<10; i++)
    {
        bool flag = true;
        for(int j=0; j<4; j++)
        {

            if(correctAnswers[j]!=contestants[i].answers[j])
            {
                flag = false;
                break;
            }
        }
        if(flag == true)
          contestantsWithCorrectAns.push_back(contestants[i]);
    }

    int noOfCorrectContestants = contestantsWithCorrectAns.size();

    for(int i=0; i<noOfCorrectContestants; i++)
    {

        cout<<"Contestant ID: "<< contestantsWithCorrectAns[i].contestantID<<endl;
        cout<<"Contestant answer: "<< contestantsWithCorrectAns[i].answers<<endl;
        cout<<"Contestant timeTaken: "<< contestantsWithCorrectAns[i].timeTaken<<endl;
        cout<<endl;
    }

    contestant rightBoys[noOfCorrectContestants];
    for (int i=0; i<noOfCorrectContestants; i++)
    {
        rightBoys[i] = contestantsWithCorrectAns[i];
    }

    if(noOfCorrectContestants==0)
        cout<<"Nobody got it right\n\n";
    else
    {
        //Sorting wrt to the time taken by the contestants
        qsort(rightBoys, noOfCorrectContestants, sizeof(contestant), compare);

        //The contestant at the 0th index would be the winner
        cout<<"The winner is contestant number: "<<rightBoys[0].contestantID+1<<endl<<endl;
    }
}
