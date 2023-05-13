#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - check the code for
 * @head: rt
 * Return: Always 0.
 */
int is_palindrome(listint_t **head)
{
int j, i = 0, h = 0, k = 0;
listint_t *hd = *head;
listint_t *hed = *head;
listint_t *heed = *head;
while (hd->next)
{
hd = hd->next;
i++;
}
i--;
if (i % 2 != 0)
{
j = (i / 2) + 1;
}
else
j = i / 2;
while (h <= j)
{
while (k <= i)
{
hed = hed->next;
k++;
}
if (heed->n != hed->n)
return (0);
h++;
heed = heed->next;
i--;
k = 0;
hed = *head;
}
return (1);
}
