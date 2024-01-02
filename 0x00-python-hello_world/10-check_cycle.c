#include "lists.h"
/**
 * check_cycle - check cycle for singly linked list
 * @list: list
 * Return: 0 on success
*/
int check_cycle(listint_t *list)
{
	listint_t *slowptr = list;
	listint_t *fastptr = list;

	while (slowptr != NULL && fastptr != NULL && fastptr->next != NULL)
	{
		slowptr = slowptr->next;
		fastptr = fastptr->next->next;

		if (slowptr == fastptr)
			return (1);
	}
	return (0);
}
