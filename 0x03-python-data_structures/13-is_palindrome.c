#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - check if a linked list is a palindrome
 * @head: head address of the linked list
 * Return: I if it's a palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	int arr[10000];
	int i, n = 0;
	listint_t *traverse;

	if (head == NULL)
		return (0);

	traverse = *head;
	while (traverse)
	{
		arr[n++] = traverse->n;
		traverse = traverse->next;
	}

	for (i = 0; i < n / 2; i++)
	{
		if (arr[i] != arr[n - i - 1])
			return (0);
	}
	return (1);
}
