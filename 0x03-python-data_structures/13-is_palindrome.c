#include "lists.h"

/**
 * is_palindrome - check if a linked list is a palindrome
 * @head: head address of the linked list
 * Return: I if it's a palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *cur = *head;
	int tab[2048], i = 0, j = 0;

	if (*head)
	{
		while (cur)
		{
			tab[i] = cur->n;
			cur = cur->next;
			i++;
		}

		while (j < i / 2)
		{
			if (tab[j] == tab[i - j - 1])
				j++;
			else
				return (0);
		}
	}
	return (1);
}
