#include <stdio.h>
#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;

class Node
{
  public:
    int value;
    Node *next;

    Node()
    {
        next = nullptr;
    }
};

class LinkedList
{
    Node *head, *tail, *curr;

  public:
    int size;

    LinkedList()
    {
        head = nullptr;
        tail = nullptr;
        size = 0;
    }

    void append(int val)
    {
        Node *temp = new Node();
        temp->value = val;
        temp->next = nullptr;

        if (head == nullptr)
        {
            head = temp;
            tail = temp;
            temp = nullptr;
        }
        else
        {
            tail->next = temp;
            tail = temp;
        }
        size++;
    }

    void insert(int pos, int val)
    {
        Node *pre = new Node();
        Node *cur = new Node();
        Node *tmp = new Node();
        cur = head;

        for (int i = 0; i < pos; i++)
        {
            pre = cur;
            cur = cur->next;
        }

        tmp->value = val;
        pre->next = tmp;
        tmp->next = cur;

        size++;
    }

    void display()
    {
        Node *temp = new Node;
        temp = head;
        while (temp != NULL)
        {
            cout << temp->value << "\t";
            temp = temp->next;
        }
    }
};

int curPos = 0;
int nextPos = 0;
int stepSize = 371;

int findNextPos(int size)
{
    return ((curPos + stepSize) % size) + 1;
}

int main(void)
{
    auto start = high_resolution_clock::now();
    Node node;
    LinkedList list;

    list.append(0);

    for (int i = 1; i < 50000001; i++)
    {
        int pos = findNextPos(list.size);
        list.insert(pos, i);
        curPos = pos;
    }
    list.display();

    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<milliseconds>(stop - start);
    cout << "Took: " << duration.count() << "ms" << endl;
}
