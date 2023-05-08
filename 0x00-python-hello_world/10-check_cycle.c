#include "lists.h"
/**
 * check_cycle - check the code
 * @list: list
 * Return: Always 0.
 */
int check_cycle(listint_t *list)
{
listint_t *temp = list;
listint_t *tmp = list;
if (list == NULL)
return (0);
else
{
while(tmp && temp)
{
if (tmp->next == temp->next->next)
{
return (1);
break;
}
else
temp = temp->next->next;
tmp = tmp->next;
}
}
return (0);
}
