#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code
 *
 * Return: Always EXIT_SUCCESS.
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
dlistint_t *new;
new = malloc(sizeof(dlistint_t));
if (new)
{
new->n = n;
new->next = *head;
new->prev = NULL;
}
*head = new;
return (new);
}
