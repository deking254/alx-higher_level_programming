#include <stdio.h>
#include "lists.h"

/**
 * main - check the code
 *
 * Return: Always EXIT_SUCCESS.
 */
size_t dlistint_len(const dlistint_t *h)
{
int i = 0;
while (h)
{
h = h->next;
i++;
}
return (i);
}
