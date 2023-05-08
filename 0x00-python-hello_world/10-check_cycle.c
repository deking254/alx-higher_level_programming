#include "lists.h"
/**
 * check_cycle - check the code
 * @list: list
 * Return: Always 0.
 */
int check_cycle(listint_t *list)
{
listint_t *temp = list;
if (list == NULL)
return (0);
else
{
while(temp->next)
{
if (list == temp->next)
{
return (1);
break;
}
else
temp = temp->next;
}
}
return (0);
}
