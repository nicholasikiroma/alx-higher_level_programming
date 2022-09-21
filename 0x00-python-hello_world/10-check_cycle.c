#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to singly-linked list
 * Return: 1 if cycle is detected, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow_p, *fast_p;

	if (list == NULL || list->next == NULL)
		return (0);
	slow_p = list;
	fast_p = list;

	while (slow_p && fast_p && fast_p->next)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;
		if (slow_p == fast_p)
		return (1);
	}
	return (0);
}
