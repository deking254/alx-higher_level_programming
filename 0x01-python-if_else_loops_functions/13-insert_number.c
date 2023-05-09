#include "lists.h"
#include <stdio.h>
int getsumofnodes(listint_t **head);
listint_t *getnodeatposition(listint_t **head, int position);
int *getpositiontoinsert(listint_t **head, int number);
/**
 * insert_node - check the code for
 * @head: head
 * @number: n
 * Return: Always 0.
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *temp = *head;
listint_t *lastpart;
listint_t *positionpart = getnodeatposition(head, getpositiontoinsert(head, number));
temp = malloc(sizeof(int) + sizeof(*head));
temp->n = number;
temp->next = positionpart->next;
*head = 
return temp;
}
/**
 * getsumofnodes - check the code for
 * @head: head
 * Return: Always 0.
 */
int getsumofnodes(listint_t **head)
{
int i = 0;
listint_t *tmp = *head;
while (tmp)
{
tmp = tmp->next;
i++;
}
return (i);
}
/**
 * getpositiontoinsert - check the code for
 * @head: head.
 * @number: numb
 * Return: Always 0.
 */
int *getpositiontoinsert(listint_t **head, int number)
{
int p = 0;
listint_t *tmp = *head;
while (tmp)
{
if (tmp->n < number)
p++;
else
break;
tmp = tmp->next;
}
return (p);
}
/**
 * getnodeatposition - check the code for
 * @head: head.
 * @number: position
 * Return: Always 0.
 */
listint_t *getnodeatposition(listint_t **head, int position)
{
listint_t *tmp = *head;
int i = 0;
while (i <= position;)
tmp = tmp->next;
return (tmp);
}
