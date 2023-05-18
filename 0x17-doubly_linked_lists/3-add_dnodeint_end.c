#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code
 *
 * Return: Always EXIT_SUCCESS.
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
dlistint_t *new;
dlistint_t *ne = *head;
new = malloc(sizeof(dlistint_t));
if (*head == NULL)
{
new->n = n;
new->prev = NULL;
new->next = NULL;
*head = new;
}
else
{
while (ne)
{
ne = ne->next;
}
new->n = n;
new->prev = *head;
new->next = NULL;
while (new)
{
*head = new;
new = new->prev;
}
}
return (new);
}
