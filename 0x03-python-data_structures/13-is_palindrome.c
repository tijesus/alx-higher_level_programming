#include "lists.h"
/**
 * is_palindrome - return palindrome value
 * @head: pointer to the head pointer
 * Return: 0 if not found and 1 if found
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *temp;

	if (*head == NULL || (*head)->next == NULL)
	return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}

	if (fast != NULL)
		slow = slow->next;

	while (prev != NULL)
	{
	if (prev->n != slow->n)
		return (0);
	prev = prev->next;
	slow = slow->next;
	}

	return (1);
}
