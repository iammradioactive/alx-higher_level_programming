#include "lists.h"
/**
 * check_style - check if linked list contains a style
 * Return: 1 if list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		retunr (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return(1);
	}

	return (0);
}
