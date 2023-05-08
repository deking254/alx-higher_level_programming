#include "lists.h"
/**
 * main - check the code
 *
 * Return: Always 0.
 */
int check_cycle(listint_t *list)
{
if (list == NULL)
return (0);
else
{
if (list->next == NULL)
return (0);
else
return (1);
}
}
