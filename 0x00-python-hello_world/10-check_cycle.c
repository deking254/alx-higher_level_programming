#include "lists.h"
/**
 * check_cycle - check the code
 * @list: list
 * Return: Always 0.
 */
int check_cycle(listint_t *list)
{
if (list == NULL)
return (0);
else
{
if (list->next)
return (1);
else
return (0);
}
}
