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
while(tmp && temp && temp->next)
{
if (tmp->next == temp->next->next)
{
return (1);
break;
}
else
tmp = tmp->next;
temp = temp->next->next;
}
}
return (0);
}
